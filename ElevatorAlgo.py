import json
import csv
from Building import Building
from Elevator import elevator
from CallForElevator import CallForElevator
# this is the class that allocate the given calls to the elevators of the builidng
class ElevatorAlgo :

    def __init__(self):
        self.init()

    # this function init our lists and dictionary also the calls that we want to allocate and the building from
    # the json and csv given files
    def init(self):
        self._CallDic = {} # this dictionary contains the calls and her suitable elevator
        self._CalList = [] # this list contains the calls
        self.LoadCalls() #  this function load  the calls
        self._building=self.LoadBuilding() #  this function load  the building
        self.NumOfCalls = len(self._CalList)
        self.AllocateAll() # this is the main function that allocate our calls to there suitable elevator

    # this function return the building that we loads and work in
    def getBuilding(self):
        return self._building
    # this function return the suitable elevator for the given call
    def allocateAnElevator(self,Call):
        return self._CallDic[Call]
    # this function allocate all the calls to the suitable elevator
    def AllocateAll(self):
        ans =0
        while len(self._CalList) > 0 :
            call = self._CalList.__getitem__(0)
            for elev in range(self._building.getNumElev()):
                src = call.getSrc()
                if self.dist(src, elev) <self.dist(src, ans) and self.inrang(call,elev):
                    ans = elev
            self._CallDic[call]=ans
            my_dist = call.getDest()
            self._CalList.remove(call)
            if len(self._CalList)>0:
                call2 = self._CalList.__getitem__(0)
                if call2.getType()== call.getType() and self.inrang(call2,ans) and ans !=-1:
                    if call.getType()==1:
                        if call.getSrc() <= call2.getSrc() and call.getTime()+ abs(call.getSrc() - call2.getSrc())*self._building.getElevator(ans).getspeed():
                            self._CallDic[call2]=ans
                            my_dist=max(my_dist, call2.getDest())
                            self._CalList.remove(call2)
                    if call.getType()==-1:
                        if call.getSrc() >= call2.getSrc() and call.getTime()+ abs(call.getSrc() - call2.getSrc())*self._building.getElevator(ans).getspeed():
                            self._CallDic[call2]=ans
                            my_dist = min(my_dist, call2.getDest())
                            self._CalList.remove(call2)
            self._building.getElevator(ans).goto(my_dist)
    # this function return the distance between the current position of the elevator and the src of the call
    def dist(self ,src ,elev):
        Elev = self._building.getElevator(elev)
        pos = Elev.getPosition()
        speed = Elev.getspeed()
        floorTime = speed + Elev.getStopTime() + Elev.getStartTime() + Elev.getOpenTime() + Elev.getCloseTime()

        return abs(pos-int(src))*floorTime
    # this function check if the call is in the range of the elevator
    def inrang(self, call , elve):
        el = self._building.getElevator(elve)
        if el.getMinFloor() <= call.getSrc() and el.getMinFloor()<=call.getDest() and el.getMaxFloor() >= call.getDest() and el.getMaxFloor() >= call.getSrc():
            return True
        else:
            return False
    # this function load the building from a jison file
    def LoadBuilding(self):
        try:
            new_dic = {}
            with open("data/B5.json", 'r') as f:
                data = json.loads(f.read())
                building = Building(minFloor=data["_minFloor"], maxFloor=data["_maxFloor"],
                                    elevators=data["_elevators"])
                minFloor = data["_minFloor"]
                maxFloor = data["_maxFloor"]
                elevators = data["_elevators"]
                ElVList = []
                for v in elevators:
                    e = elevator(id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"],
                                 closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"],
                                 stopTime=v["_stopTime"])
                    ElVList.append(e)
                building = Building(minFloor, maxFloor, ElVList)
                return building

        except IOError as e:
            print(e)
    # this function load the calls from a jison file
    def LoadCalls(self):
        rows = []
        with open("data/Calls_d.csv", 'r') as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)
            for row in csv_reader:
                call = CallForElevator(Time=row[1], Src=row[2], Dest=row[3])
                self._CalList.append(call)
                rows.append(row)
    # this function create a new file that contain reach call and the number of the elevator that it been allocated to
    def UpdateCSV(self):
        op = open("data/Calls_d.csv", "r")
        csv_reader=csv.reader(op)
        header= next(csv_reader)
        dt = csv.reader(op)
        up_dt = []
        index=0
        list = []
        filename = 'B5_C4.csv'
        for k in self._CallDic:
            list.append(self._CallDic[k])
        with open(filename, 'w', newline="") as file:
            csv_writer = csv.writer(file)
            header[5] = 0
            csv_writer.writerow(header)
            for r in dt:
                r[5] = list[index]
                up_dt.append(r)
                csv_writer.writerow(r)
                index = index + 1
        op.close()










