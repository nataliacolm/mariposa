<h1 align="center">Mariposa</h1>
<p align="center">
<img src="https://user-images.githubusercontent.com/46806107/157618628-5665e5a2-a515-47e5-bf92-f7f3f6498cbb.png" width="150" height="150">
</p>

## Overview
Mariposa is a mobile/web application and autonomous electric vehicle system which allows KPMG employees and partners to reduce their carbon footprint. Via incentives and community challenges, users are motivated to make transport decisions informed by environmental impact. This repository highlights some key user interaction features shown bare without a front-end. The prospective, bare-bones versions of server, client, and scripts for AWS technologies are housed here. Open source python scripts were used from the following GitHub https://github.com/J0ANMM/carbon-calculator to incorporate a base for the carbon calculator based on real data and modes of transportation.


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
  
  Transport Options: 
    
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
      Carbon Emission Points:  17
     
*Users can view the potential environmental impact by viewing travel options and their respective carbon emission points*

## Considerations
Something to note while viewing outputed carbon emission points, to work successfully with an incentivized points system, emission points for personal vehicle options were adjusted by scale. This is due to the massive difference in calculated emissions between personal vehicle and other transportaiton options. Personal vehicle options frequently generate more than 10 times the emissions of other options based on simulated application runs pulling from actual emission data. 
