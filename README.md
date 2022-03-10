# Mariposa

## Overview
Mariposa is a mobile/web application and autonomous electric vehicle system which allows KPMG employees and partners to reduce their carbon footprint. Via incentives and community challenges, users are motivated to make transport decisions informed by environmental impact. This repeository highlights some key user interaction features shown bare without a front-end. The prospective, bare-bones versions of server, client, and scripts for AWS technologies are housed here. 

## Interaction
To run a simulation of the client scripts and server scripts run the following on command line:
python3 driver.py
Make sure to first install all requirements mentioned within requirements.txt

## Output/Dialog Process
> Welcome!
> Type number of desired location from list:
> 1) KMPG, 2) Expedia, 3) Amazon, 4) Dell

Entered value: **1**

> Destination Choice: KPMG Austin Office
> Based on current geolocation, trip distance is  12  kilometers 
*Makes an API call to determine distance from location of mobile app request to destination*

> Please input desired arrival range start time: (in format HH:MM , using military time) 
**12:34** 

> Please input desired arrival range end time: (in format HH:MM , using military time) 
**14:22**

> Thank you! Travel options within this time range are as follows. To select an option, type the choice's number
  
  Electric Shuttle Options:
    1. Shuttle Option 1 
      Est. Arrival Time:  12 
      Carbon Emission Points:  9 
      Est. # of Passengers:  7 

    2. Shuttle Option 2 
      Est. Arrival Time:  13 
      Carbon Emission Points:  8 
      Est. # of Passengers:  8 

   3 . Bike, Walk, Scooter
    Carbon Emission Points: 0
   4 . Personal Vehicle (Honda City Petrol)
    Carbon Emission Points:  107_
    
    
*Users can view the potential environmental impact by viewing travel options and their respective carbon emission points*
