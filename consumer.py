# Script ran in the EC2 instance to read from message queue and recieve user requests.
# assumes sqs instance is named mariposa-job-queue
# assumes property file with RDS MySQL login information

import boto3
import logging
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getend('PASSWORD')

sqs = boto3.resource("sqs")
q = sqs.get_queue_by_name(QueueName='mariposa-job-queue')
logger = logging.getLogger(__name__)

'''
message formatting:
{
    'curr_location' : '41.40338, 2.17403',
    'range_time' : '12:30, 15:55',
    'destination' : '1',
    'mode' : 'Autonomous vehicle',
    'distance' : '10',
    'timestamp' : '2021-07-03 16:21:12.357246',
    'job_id' : '189637awzxd',
    'avg_use' : '[13, 1, 4, 5, 7, 13, 3, 5, 6, 7, 2, 10, 11, 10, 9, 7]'
}
'''

def process_message(message):
    
    # do something
    # update records on call from certain days and times
    hourStart = int(message['range_time'][0].split(",",1)[0])
    hourEnd = int(message['range_time'][1].split(",",1)[0])

    res = Server.calcShuttleSlots(hourStart, hourEnd, message['avg_use'], message['distance'])

    # add message response to SQL:
    db = mysql.connector.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    sql = 'UPDATE Requests SET result = res WHERE message[job_id] = job_id'

    try:
        cursor.execute(sql)
    except:
        db.rollback()

    db.close()

if __name__ == 'main':
    # implement long polling
    while True:
        messages = q.receive_messages(WaitTimeSeconds=30)
        for message in messages:
            try:
                process_message(message)
                logger.info('Message %s received', message.message_id)
            except Exception as e:
                logger.exception('Error reading from SQS service.')
                continue
            message.delete()
                
