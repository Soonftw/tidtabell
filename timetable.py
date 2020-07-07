#!/usr/bin/env python3
from tkinter import *
import time
import requests
import json
import os
import re
dateFormat = re.compile('[0-2][0-9]:[0-9][0-9]')
clear = lambda: os.system('cls')

class Trip():
    #Ordnar alla resor som objekt
    def __init__(self, line, fromStation, toStation, departureTime):
        self.line = line
        self.fromStation = fromStation
        self.toStation = toStation
        self.departureTime = departureTime
        self.depTimeMins = None
    def setMins(self, depTimeMins):
        self.depTimeMins = depTimeMins


def main():
    root = Tk()
    # root.geometry("800x600")
    root.attributes('-fullscreen', True)

    c = Canvas(root, bg="blue", height=800, width=600)
    filename = PhotoImage(file = r"stockholm2.gif")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(root, text="Roslags Näsby - Östra Station ", font=("Helvetica", 24), anchor=N, justify=CENTER)
    # title.grid(row=0,column=2)
    title.pack(side=TOP, fill=BOTH)
    timeNow = time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime())
    timeVar = StringVar()
    subtitle = Label(root, textvariable = timeVar, font=("Helvetica", 18), anchor=N, justify=CENTER)
    # subtitle.grid(row=1,column=2)
    subtitle.pack(side=TOP, fill=BOTH)
    timeVar.set(str(timeNow))

    tripList = callTime()
    trips = len(tripList)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()


    label1 = Label(root, textvariable=var1, font=("Helvetica", 18), anchor = W, width=18)
    # label1.grid(row=3)
    label1.pack(side=TOP, anchor=W)
    label2 = Label(root, textvariable=var2, font=("Helvetica", 18), anchor = W, width=18)
    # label2.grid(row=4)
    label2.pack(side=TOP, anchor=W)
    label3 = Label(root, textvariable=var3, font=("Helvetica", 18), anchor = W, width=18)
    # label3.grid(row=5)
    label3.pack(side=TOP, anchor=W)
    label4 = Label(root, textvariable=var4, font=("Helvetica", 18), anchor = W, width=18)
    # label4.grid(row=6)
    label4.pack(side=TOP, anchor=W)
    label5 = Label(root, textvariable=var5, font=("Helvetica", 18), anchor = W, width=18)
    # label4.grid(row=6)
    label5.pack(side=TOP, anchor=W)
    # label6 = Label(root, textvariable="aapappaapa\n\n\n\n\n\n\n", font=("Helvetica", 18), anchor = W, width=18)
    # label4.grid(row=6)
    # label6.pack(side=TOP, anchor=W)

    try:
        var1.set("\nLine: "+str(tripList[0].line)+"\nDeparts: "+str(tripList[0].depTimeMins)+" min\n"+"("+tripList[0].departureTime+")\n---------------------------")
        var2.set("Line: "+str(tripList[1].line)+"\nDeparts: "+str(tripList[1].depTimeMins)+" min\n"+"("+tripList[1].departureTime+")\n---------------------------")
        var3.set("Line: "+str(tripList[2].line)+"\nDeparts: "+str(tripList[2].depTimeMins)+" min\n"+"("+tripList[2].departureTime+")\n---------------------------")
        var4.set("Line: "+str(tripList[3].line)+"\nDeparts: "+str(tripList[3].depTimeMins)+" min\n"+"("+tripList[3].departureTime+")\n---------------------------")
        var5.set("Line: "+str(tripList[4].line)+"\nDeparts: "+str(tripList[4].depTimeMins)+" min\n"+"("+tripList[4].departureTime+")\n---------------------------")
        # var6.set("Line: "+str(tripList[5].line)+"\nDeparts: "+str(tripList[5].depTimeMins)+" minutes\n"+"("+tripList[5].departureTime+")"+"\n---------------------------")
        pass
    except IndexError as e:
        pass
    root.update()

    # one = Label(root, text = "one\nlol",anchor="w", bg = "red", fg = "white")
    # one.pack(fill=X)
    # two = Label(root, text = "two", bg = "blue", fg = "black")
    # two.pack(side = LEFT, fill=X)
    #
    # two = Label(root, text = "three", bg = "green", fg = "white")
    # two.pack(side = LEFT, fill=X)

    i = 0

    while True:
        time.sleep(1)
        i+=1
        timeNow = time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime())
        timeVar.set(str(timeNow))
        if (i==10):
            i=0
            tripList = callTime()
            trips = len(tripList)
            try:
                var1.set("\nLine: "+str(tripList[0].line)+"\nDeparts : "+str(tripList[0].depTimeMins)+" min\n"+"("+tripList[0].departureTime+")\n---------------------------")
                var2.set("Line: "+str(tripList[1].line)+"\nDeparts: "+str(tripList[1].depTimeMins)+" min\n"+"("+tripList[1].departureTime+")\n---------------------------")
                var3.set("Line: "+str(tripList[3].line)+"\nDeparts: "+str(tripList[2].depTimeMins)+" min\n"+"("+tripList[2].departureTime+")\n---------------------------")
                var4.set("Line: "+str(tripList[2].line)+"\nDeparts: "+str(tripList[3].depTimeMins)+" min\n"+"("+tripList[3].departureTime+")\n---------------------------")
                var5.set("Line: "+str(tripList[4].line)+"\nDeparts: "+str(tripList[4].depTimeMins)+" min\n"+"("+tripList[4].departureTime+")\n---------------------------")
                # var6.set("Line: "+str(tripList[5].line)+"\nDeparts: "+str(tripList[5].depTimeMins)+" minutes\n"+"("+tripList[5].departureTime+")"+"\n---------------------------")
                pass
            except IndexError as e:
                pass
        root.update()
    root.mainloop()


def callTime():
    tripList = []

    print(time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime()))
    response = requests.get("http://api.sl.se/api2/realtimedeparturesV4.Json?key=98550d23ca61456b98d230dadf0bd991&siteid=9633&timewindow=60&Bus=False")
    content = response.json()

    for category in content["ResponseData"]["Trams"]:
        if category["Destination"] == "Stockholms östra":

            line = category["LineNumber"]
            fromStation = category["StopAreaName"]
            toStation = category["Destination"]
            departure = category["ExpectedDateTime"].split("T")[1]
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
main()
