"""
    Run this file via the command file to test if the calculations are running as expected.

    > python3 tester.py
"""
from carbon_flight import CarbonFlight
from carbon_train import CarbonTrain
from carbon_bus import CarbonBus
from carbon_car import CarbonCar
from carbon_ferry import CarbonFerry
from geopy.geocoders import Nominatim
import geocoder
from geopy.distance import geodesic
import math
import random


class CarbonCalculatorTester(object):
    """Class to test all Carbon objects."""

    def compare_flight_ferry(self):
        """"""

        dist_km = 400
        pax_class = "economy-class"
        trip_type = "round-trip"

        co2_flight = CarbonFlight().calculate_co2(dist_km, pax_class, trip_type)

        vehicle_ferry = "without-vehicle"
        hours_trip = 8
        duration_in_minutes = hours_trip * 60

        co2_ferry = CarbonFerry().calculate_co2(
            duration_in_minutes, vehicle_ferry, trip_type
        )

        print(
            "---- Travel FLIGHT vs FERRY",
            dist_km,
            " km or ",
            hours_trip,
            " hours ",
            trip_type,
            "passenger ----",
        )
        print("Carbon footprint flying ", pax_class, ": ", co2_flight, "gCO2")
        print("Carbon footprint by ferry ", vehicle_ferry, ": ", co2_ferry, "gCO2")
        print()

    def compare_flight_train(self):
        """"""

        dist_km = 600 
        trip_type = "one-way"
        pax_class = "economy-class"

        co2_flight = CarbonFlight().calculate_co2(dist_km, pax_class, trip_type)

        train_energy = "electric"
        train_country = "DE"

        co2_train = CarbonTrain().calculate_co2(
            dist_km, train_energy, train_country, trip_type
        )

        print("---- Travel FLIGHT vs TRAIN", dist_km, " km", trip_type, "----")
        print("Carbon footprint flight ", pax_class, ": ", co2_flight, "gCO2")
        print(
            "Carbon footprint train ",
            train_energy,
            train_country,
            ": ",
            co2_train,
            "gCO2",
        )
        print()

    def compare_train_bus_car(self):
        """"""

        dist_km = 600
        trip_type = "round-trip"
        pax_qty = 1
        train_energy = "electric"
        train_country = "DE"

        co2_train = CarbonTrain().calculate_co2(
            dist_km, train_energy, train_country, trip_type
        )
        co2_bus = CarbonBus().calculate_co2(dist_km, trip_type)

        print("---- Travel TRAIN vs BUS vs CAR", dist_km, " km", trip_type, "----")
        print("Carbon footprint train", "electric", "DE", "=", co2_train, "gCO2")
        print("Carbon footprint bus", "=", co2_bus, "gCO2")
        print()

    def compare_trains(self):
        """"""

        dist_km = 500
        trip_type = "one-way"

        co2_train_e_at = CarbonTrain().calculate_co2(
            dist_km=dist_km,
            train_energy="electric",
            train_country="AT",
            trip_type=trip_type,
        )
        co2_train_e_de = CarbonTrain().calculate_co2(
            dist_km=dist_km,
            train_energy="electric",
            train_country="DE",
            trip_type=trip_type,
        )
        co2_train_d_de = CarbonTrain().calculate_co2(
            dist_km=dist_km,
            train_energy="diesel",
            train_country="DE",
            trip_type=trip_type,
        )
        co2_train_e_es = CarbonTrain().calculate_co2(
            dist_km=dist_km,
            train_energy="electric",
            train_country="ES",
            trip_type=trip_type,
        )

        print("---- Travel TRAINs", dist_km, " km", trip_type, "----")
        print("Carbon footprint train", "electric", "AT", ": ", co2_train_e_at, "gCO2")
        print("Carbon footprint train", "electric", "DE", ": ", co2_train_e_de, "gCO2")
        print("Carbon footprint train", "diesel", "DE", ": ", co2_train_d_de, "gCO2")
        print("Carbon footprint train", "electric", "ES", ": ", co2_train_e_es, "gCO2")
        print()

    def compare_cars(self, dist_km):
        """"""
        trip_type = "one-way"

        co2_car_petrol_1 = CarbonCar().calculate_co2(
            dist_km=dist_km,
            fuel_type="petrol",
            fuel_consumption=8,
            energy_consumption=None,
            electricity_country_code=None,
            pax_in_car=1,
            trip_type=trip_type,
        )

        print(
            "Carbon footprint car", "petrol 8l", "1 pax", "=", co2_car_petrol_1, "gCO2"
        )
        print()

    # def compare_cars(self):

    def testTool(self):

        useData = []
        # number of use statistic lists covering 24 hours
        dataLength = 30
        for i in range(0, dataLength):
            useData.append([])
            # append 24 hours
            for j in range(0, 24):
                useData[i].append(random.randrange(20))

        '''for hours in useData:
            print(hours, "\n")'''

        print("Welcome!")
        #FIXME NEED VALIDATION OF INPUTS
        startRange = input(
            "Please input desired arrival range start time: (in format HH:MM , using military time) "
        )
        endRange = input(
            "Please input desired arrival range end time: (in format HH:MM , using military time) "
        )
        #FIXME - parse

        location = input(
            "Type number of desired location from list:\n 1) KMPG Lake Nona, 2) Client 1, 3) Client 2, 4) Client 3\n"
        )
        # grab current latitude and longitude
        geolocator = Nominatim(user_agent="My App")

        my_location = geocoder.ip("me")

        latitude = my_location.geojson["features"][0]["properties"]["lat"]
        longitude = my_location.geojson["features"][0]["properties"]["lng"]
        userCoords = (latitude, longitude)
        # FIXME: add options for all desired locations
        # calculate distance from KPMG Orlando Office
        officeData = geolocator.geocode("9301 Lake Nona Blvd, Orlando, FL 32827")
        officeCoords = (officeData.latitude, officeData.longitude)

        distance = math.trunc(geodesic(userCoords, officeCoords).km)

        print(
            "Based on current geolocation, trip distance is ", distance, " kilometers"
        )

        # Generate Shuttle Options + Emissions for each
        calculateShuttles(useData, dataLength)
        print(
            "Thank you! Travel options within this time range are as follows. To select an option, type the choice's number"
        )
        print("Electric Shuttle Options:")

        print("7. Bike, Walk, Scooter\nCarbon Emission Points: 0")
        print("8. Personal Vehicle (Honda CRV 2012)\nCarbon Emission Points:")
        print("")


def calculateShuttles(useData, dataLength):
    averageUse = []
    #range based off of hours in day
    for j in range(0, 24):
        sum = 0
        #range can be increased as more data is collected
        for i in range(0, dataLength):
            sum = sum + useData[i][j]
        averageUse.append(math.ceil(sum / dataLength))
    '''hour = 0
    for people in averageUse:
        print("hour: ", hour, "people avg: ", people)
        hour = hour + 1'''


