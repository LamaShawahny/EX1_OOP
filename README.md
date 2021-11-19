Elevator - Assignment 1
=======================

Task:
-----
Design and implement an elevator control system in PYTHON .

Design:
-------
The project has 4 main classes 'Elevator.java' and 'ElevatorControlSystem.java'.

#### Elevator.py
This class represents the Elevator in the building. its id ,speed floors...

  properties :
      id, speed, minFloor, maxFloor , closeTime , openTime , startTime , stopTime.
  constructor:
    def __init__(self, id, speed, minFloor, maxFloor , closeTime , openTime , startTime , stopTime)
  methods:
  def goto(self, floor): it moves the elevator to the given floor
  other get functions for the properties that I mentioned above.


#### CallForElevator.py 
 properties :
     Time,Src,Dest.
  constructor:
     def __init__(self ,Time,Src,Dest)
  methods:
   Get functions for the properties that I mentioned above.

#### Building.py
this class represnts the building that we allocate the calls in ...
 properties :
     * minFloor,maxFloor
     * elevators : list of elevators
  constructor:
     def __init__(self,minFloor,maxFloor,elevators):
  methods:
   Getter functions for the properties of the building.


#### ElevatorAlgo.py
This class  is the main one, it allocates the given calls to the elevators of the builidng .
properties :
      CallDic {} :  dictionary that contains the calls and thier suitable elevator
      CalList [] :  list that contains the calls
      NumOfCalls : number of calls
      building  :  the building that we load and work with
        
  constructor:
     def init(self)
     
  methods:
  allocateAnElevator(self,Call):this function returns the suitable elevator for the given call
  AllocateAll() : this is the main function that allocate our calls to there suitable elevator
  def dist(self ,src ,elev): this function returns the distance between the current position of the elevator and the src of the call
  def inrang(self, call , elve): this function checks if the call in the range of the elevator or not .
  LoadCalls() :  this function load  the calls from a csv file
  LoadBuilding() :  this function load  the building from a jason file
  def UpdateCSV(self): it creates a new file that contains call and the number of the elevator that it has been allocated to .
  
  other getter functions for the properties of the building.

```
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
```

Algorithm:
-------------------------------------
```
*   We put all of the calls into the data structure list .
*   Sorting the calls by time (sortest time first).
*   Taking the first call and use the method ALLOCATED TO (allocating it to the closest elevator).
*   By defult, all The elevators would be at their minimum floor.
*   After we allocate the call, we check if the next call can be executed in this elevator (if the elevator is going up, and the source of this call is less than the source of the original call)
*   we take the call with us, execute it, and remove it from the list.  
*   Do not assign the request to an elevator if it is under MAINTENANCE 
*   Now, among all elevators excluding above ones, find the closest elevator moving in direction of request .
    * Case I   -   There are 2 elevators, 1 above the requestFloor coming down and 1 below the requestFloor which is coming up:
                   Assign the request to the closest of these 2.
                   return true
    * Case II  -   There is only 1 elevator moving towards the requestFloor.
                   Assign the request to the given elevator.
                   return true
    * Case III -   No elevators were found eligible to serve the request. Can happen if all the elevators are under MAINTENANCE
                   return false as we could not schedule the request to any of the elevators in the system.
```
