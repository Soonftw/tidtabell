import requests
import json
import time
import os
import re
dateFormat = re.compile('[0-2][0-9]:[0-9][0-9]')
clear = lambda: os.system('cls')



def callTime():
    tripList = []

    print(time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime()))
    response = requests.get("http://api.sl.se/api2/realtimedeparturesV4.Json?key=98550d23ca61456b98d230dadf0bd991&siteid=9626&timewindow=60&Bus=False")
    content = response.json()

    for category in content["ResponseData"]["Trams"]:
        if category["Destination"] == "Stockholms östra":
            line = category["LineNumber"]
            fromStation = category["StopAreaName"]
            toStation = category["Destination"]
            departure = category["DisplayTime"]

            trip = Trip(line,fromStation,toStation,departure)

            print("-------------------------------")
            print("Linje: "+line)
            print("Från: "+fromStation)
            print("Till: "+toStation)
            if dateFormat.match(departure):
                hourAndMinutes = departure.split(":")
                hourDeparture = int(hourAndMinutes[0])
                minuteDeparture = int(hourAndMinutes[1])
                hourNow = time.localtime()[3]
                minuteNow = time.localtime()[4]
                if (hourDeparture > hourNow):
                    minuteDeparture += abs(hourDeparture - hourNow)*60
                    departure = abs(minuteDeparture - minuteNow)
                else:
                    departure = abs(minuteDeparture - minuteNow)
                print("Avgång: %d min"%departure, end = " ")
            else:
                print("Avgång: "+departure, end = " ")
            print("("+category["ExpectedDateTime"].split("T")[1]+")")
            trip.setMins(departure)
            tripList.append(trip)
    print("-------------------------------")

    return tripList
