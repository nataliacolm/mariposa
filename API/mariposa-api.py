# This code follows structure found in chalice documentation for a simple api application
from chalice import Chalice
import boto3
import json
import logging
from datetime import datetime
from botocore.exceptions import ClientError
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getend('PASSWORD')

app = Chalice(app_name = 'mariposa_api')

BUCKET_NAME = "mariposa-bucket"
REGION = 'us-east-1'
s3_client = boto3.client('s3')

# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
@app.route("/submit_job", methods = ['GET'])
def create_index(user_id):
    datetime_obj = datetime.now()
    try:
        response = s3_client.generate_presigned_url('put_object', Params={'Bucket' : BUCKET_NAME, 'Key' : datetime_obj, "ContentType" : "application/json"}) # Key for the filename

    except ClientError as e:
        print('Error creating S3 presigned url')
        return None
    
    return json.dumps({'job_id' : datetime_obj + user_id, 'response' : response})

@app.route("/query_job")
def query_job():
    db = mysql.connector.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    sql = 'SELECT result FROM Requests WHERE ready = true'

    try:
        st = cursor.execute(sql)
        return st # return result for st
    except:
        db.rollback()
    

