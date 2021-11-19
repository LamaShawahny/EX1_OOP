# this class represnts the building that we want to allocate the calls in

from Elevator import elevator
class Building :
    def __init__(self,minFloor,maxFloor,elevators):
        self._minFloor = minFloor
        self._maxFloor =maxFloor
        self._elevators = elevators
        self._num = len(elevators)
    #this function return the MinFloor of the building
    def getMinFloor(self):
        return self._minFloor
    #this function return the MaxFloor of the building
    def getMaxFloor(self):
        return self._maxFloor
    #this function return the the elevator in the given index
    def getElevator(self,idx):
        if idx < len(self._elevators) :
            return self._elevators.__getitem__(idx)

    # this function return the the number of the elevators in the building
    def getNumElev(self):
        return self._num
