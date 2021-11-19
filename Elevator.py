# this class represnt the elevator that in the building

class elevator :
    def __init__(self, id, speed, minFloor, maxFloor , closeTime , openTime , startTime , stopTime):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self._position =minFloor

    #this function returns the elevator min floor
    def getMinFloor(self):
        return self._minFloor
    #this function returns the elevator max floor
    def getMaxFloor(self):
        return self._maxFloor
    #this function returns the time to close the elevator door
    def getCloseTime(self):
        return self._closeTime
    #this function returns the time to open the elevator door
    def getOpenTime(self):
        return self._openTime
    #this function returns the time to start the elevator door
    def getStartTime(self):
        return self._startTime
    #this function returns the time to end the elevator door
    def getStopTime(self):
        return self._stopTime
    # this function returns the position of the elevator
    def getPosition(self):
        return self._position
    # this function moves the elevator to the given floor
    def goto(self, floor):
        self._position = floor
    #this function returns the elevator id
    def getID(self):
        return self._id
    #this function returns the elevator speed
    def getspeed(self):
        return self._speed


