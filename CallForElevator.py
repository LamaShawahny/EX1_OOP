# this class represnt the call that we want to allocate
class CallForElevator :
    def __init__(self ,Time,Src,Dest):
        self._Time=float(Time)
        self._Src=int(Src)
        self._Dest= (Dest)
        if  Dest>Src:
            self._Type= 1
        else:
            self._Type=-1

    # this function return the src of the call
    def getSrc(self):
        return int(self._Src)
    # this function return the time of the call
    def getTime(self):
        return float(self._Time)

    # this function return the dest of the call
    def getDest(self):
        return int(self._Dest)

    # this function return the type of the call up or down
    def getType(self):
        return self._Type




