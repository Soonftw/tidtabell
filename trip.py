def class Trip(line, fromStation, toStation, departureTime):
    def __init__(self, line, fromStation, toStation, departureTime):
        self.line = line
        self.fromStation = fromStation
        self.toStation = toStation
        self.departureTime = departureTime
        self.depTimeMins = 0

    def setMins(self, depTimeMins):
        self.depTimeMins = depTimeMins
