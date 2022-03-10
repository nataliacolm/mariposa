import pandas as pd
import math
from carbon_car import CarbonCar


class Server:
    def processData(location):
        if location == 1:
            officeName = "KPMG"
        elif location == 2:
            officeName = "Expedia"
        elif location == 3:
            officeName = "Amazon"
        else:
            officeName = "Dell"
        df = pd.read_csv("Hub_to_" + officeName + ".csv")
        avgUse = []
        for hour in range(0, 15):
            sum = df.loc[df["HOUR"] == hour, "#OFOCCUPANTS"].mean()
            sum = math.ceil(sum)
            avgUse.append(sum)
        return avgUse

    def calcShuttleSlots(timeStart, timeEnd, avgUse, dist):
        hourStart = int(timeStart.split(":", 1)[0])

        hourEnd = int(timeEnd.split(":", 1)[0])
        trip_type = "one-way"
        i = 1
        for hour in range(hourStart, hourEnd):
            shuttleEmissions = CarbonCar().calculate_co2(
                dist_km=dist,
                fuel_type="electric",
                fuel_consumption=None,
                # Source: https://pdf.sciencedirectassets.com/271090/1-s2.0-S0360544217X00030/1-s2.0-S0360544217301081/Zhiming_Gao_Bus_Electrification_2017.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLWVhc3QtMSJGMEQCICCnceBnJPm3wGy2dHvDEpRFxYAPU5ojNAkVcx3M5OB0AiASo7QzHIDYtnbqZdkB4Mhl%2FlVPOJEvNG%2F1tLVntJMjmyqDBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAQaDDA1OTAwMzU0Njg2NSIMd4hq8XxG7ErJcOOpKtcDkuCDNvuhBip1HzpblZpbvzuMo75SMAr4BYKThGd%2FXvXQF1KFR6K8ivSBlDNdIwYQPE0womlfZct34ZORaaZdP8a6%2BZyApfPwwTNNC3EH7nVIaIUkKaquIU1GX9LSLEYqbYtZBUjAAoYU2TY%2FrcGlZqozmO15QHAORkCS2lC%2FjAbvO39vLUyJghTd67sCD0plnIpJ1Ixxi3hq3hKw%2FPr9ErusH6P%2F5%2FsYdfKTOVQ5i3UdugHl00eGLSIBj4sso2iwPxePy1Fbta9RjNgVFhkifoIwQ6dwrYwpJ3vfkMeNHPf%2FQOoaGKfNQjKPb8EFXcFFYJGtR4vSdItFoUjg6fkMw0148%2Fpf4oYJ3Okw5%2BSDLk6LyVLc%2BvVW1SD2Ltnkqbbimxph54rZKQppV4vlahgY%2Fbc3tsdvC4CCHE2rgT1vinZ2qDe9oxqHgcB1s57jYgWO5HGjM%2F%2BVIUTyErgwsCXQt3nRrdTDugIsvGHYqBreeQDEm6MBTjGGXd7Lw7BG7F9VpUVmnDb%2F244zx20P4NSfzv3I4Gjyjuro4bRhasEF4xUkFBOsvG6U40JlPQidJ2gDKPWkXhPT23tuo46NqiKQOksR5brH8bt8wR9OMAtVhNkJzmZHADDIMLLnpZEGOqYB4dBpxEeIOYu4EYOd8qJnjp9aYUeiKv%2BJoXkUCbn2OEH7yxB0m3EAxou9u61DK1YOZVmBQ9HbUvA8AJdxLdJeOhGjXNkbaBr%2FuBvdeEQ66o36SYHotpZOKnNoB%2BO0YeiAlSmk3LGNtQ9HIF7T%2Bw0h1Yh3I9egthjchgDOI5UVjYKbUoNYehTIlZYjoYtxMX6oGZ25MU3S8sk5hNDGi4umRO2DTpLqZw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220310T051516Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSEHLAA5H%2F20220310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f7e509993982497df807679299f6c199fa1b217c91a3eccb91e27d2a7a92166c&hash=9d27bb07206ada9978a9503f5095bb005a681be77e9801d5d62f19a2f024016a&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0360544217301081&tid=pdf-8276909d-f1b7-4d30-9bb1-211fea1561fd&sid=d85888ff1d77d347fc9a4c70964a54bcaaddgxrqa&type=client
                electricity_consumption=1.35,
                electricity_country_code="US",
                pax_in_car=avgUse[hour - 5],
                trip_type=trip_type,
            )
            print(
                "  Shuttle Option",
                i,
                "\n    Est. Arrival Time: ",
                hour + 1,
                "\n    Carbon Emission Points: ",
                shuttleEmissions,
                "\n    Est. # of Passengers: ",
                avgUse[hour - 5],
                "\n",
            )
            i = i + 1
        if hourStart == hourEnd:
            print("    No shuttle options within time range")
        return i - 1


if __name__ == "__main__":
    Server.calcShuttleSlots("9:35", "13:47", Server.processData(2), 16)
