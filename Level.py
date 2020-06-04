from Object import *
from Brick import *
from MovingBrick import *

class Level:
    def __init__(self):
        self.objects = [
                Brick((10,10),(4,2),"Brick"),
                Brick((10,20),(4,2),"Brick"),
                MovingBrick((10,14),(2,4),"Brick",(1,0)),
                Brick((25,14),(4,2),"Brick")
            ]

    def deleteObj(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            print("Error: object not in list")
