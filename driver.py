'''
Code is modified from Github https://github.com/J0ANMM/carbon-calculator to calculate quota, points reducted,
and determine how transportation modes affect carbon emissions.
'''

from geopy.geocoders import Nominatim
import geocoder
from geopy.distance import geodesic
import math
import random
from carbon_car import CarbonCar
from server import Server


class Driver:
    def testTool(self):
        print("Welcome!")

        locale = input(
            "Type number of desired location from list:\n1) KMPG, 2) Expedia, 3) Amazon, 4) Dell\n"
        )

        # grab current latitude and longitude
        geolocator = Nominatim(user_agent="My App")

        my_location = geocoder.ip("me")

        latitude = my_location.geojson["features"][0]["properties"]["lat"]
        longitude = my_location.geojson["features"][0]["properties"]["lng"]
        userCoords = (latitude, longitude)
        # FIXME: add options for all desired locations
        # calculate distance to selected location
        if locale == "1":
            officeAddress = "111 Congress Ave, Austin, TX 78701"
            print("Destination Choice: KPMG Austin Office")
        elif locale == "2":
            officeAddress = "11920 Alterra Pkwy, Austin, TX 78758"
            print("Destination Choice: Expedia Austin Office")
        elif locale == "3":
            officeAddress = "11501 Alterra Pkwy, Austin, TX 78758"
            print("Destination Choice: Amazon Austin Office")
        else:
            officeAddress = "9715 Burnet Road, Austin, TX 78758"
            print("Destination Choice: Dell Austin Office")

        officeLocation = geolocator.geocode(officeAddress)
        officeCoords = (officeLocation.latitude, officeLocation.longitude)
        distance = math.trunc(geodesic(userCoords, officeCoords).km)

        print(
            "Based on current geolocation, trip distance is ",
            distance,
            " kilometers \n",
        )

      
        startRange = input(
            "Please input desired arrival range start time: (in format HH:MM , using military time, from [05 to 19]) "
        )
        endRange = input(
            "Please input desired arrival range end time: (in format HH:MM , using military time, from [05 to 19]) "
        )
        hourStart = int(startRange.split(":", 1)[0])
        hourEnd = int(endRange.split(":", 1)[0])

        while((hourStart < 5 )or (hourStart > 19)):
            print("Start Range is out of business hours, please input a new time")
            startRange = input("Please input desired arrival range start time: (in format HH:MM , using military time, from [05 to 19]) ")
            hourStart = int(startRange.split(":", 1)[0])

        while(hourEnd < 5 or hourEnd > 19):
            hourEnd = int(endRange.split(":", 1)[0])
            print("End Range is out of business hours, please input a new time")
            endRange = input("Please input desired arrival range end time: (in format HH:MM , using military time, from [05 to 19])")
       

        # Generate Shuttle Options + Emissions for each
        print(
            "Thank you! Travel options within this time range are as follows. To select an option, type the choice's number"
        )
        print("  Transport Options:")
        ## run through list of avg use over time slots, generating carbon emissions for each slot (remove unavailable times)
        numOptions = Server.calcShuttleSlots(
            startRange, endRange, Server.processData(2), distance
        )
        print("  ", numOptions + 1, ". Bike, Walk, Scooter\n    Carbon Emission Points: 0")
        # FIXME:  call car carbon emission
        trip_type = "one-way"

        co2_car_petrol_1 = CarbonCar().calculate_co2(
            dist_km=distance,
            fuel_type="petrol",
            fuel_consumption=8,
            electricity_consumption=None,
            electricity_country_code=None,
            pax_in_car=1,
            trip_type=trip_type,
        )
        
        print(
            "\n  ",
            numOptions + 2,
            ". Personal Vehicle (Honda City Petrol)\n    Carbon Emission Points: ", co2_car_petrol_1,
        )
        number = input("\nWhich transport option would you like to select? (Input # or 0 to book none): ")
        if((int(number) == 0) or (int(number) > numOptions + 2)):
            print("No options have been booked. Thank you!")
        else:
            print("Option ", number, " has now been scheduled. Thank you!")



if __name__ == "__main__":
    drive = Driver()
    drive.testTool()
