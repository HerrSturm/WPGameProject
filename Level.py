from Object import *
from Brick import *
from MovingBrick import *

class Level:
    def __init__(self):
        global level1
        self.objects = []
        self.levelList = [level1]
        self.currentLevel = 0
        self.loadLevel()

    def deleteObj(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            print("Error: object not in list")

    def loadLevel(self):
        self.objects = self.levelList[self.currentLevel]

    def update(self, screen):
        for obj in self.currentLevel.objects:
            obj.update(self)
            obj.draw(screen)

level1 = [
            Brick((10,10),(4,2),"Brick"),
            Brick((10,20),(4,2),"Brick"),
            MovingBrick((10,14),(2,4),"Brick",(1,0)),
            Brick((25,14),(4,2),"Brick")
        ]
