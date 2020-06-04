from Brick import *

class MovingBrick(Brick):
    def __init__(self,pos,size,type, dir = [0,0]):
        super().__init__(pos,size, type)
        self.dir = dir

    def move(self):
        self.box[0] += self.dir[0]
        self.box[1] += self.dir[1]

    def collision(self,obj, gameManager):
        pass

    def update(self, gameManager):
        self.move()
