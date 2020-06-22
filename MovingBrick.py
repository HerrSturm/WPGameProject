from Brick import *

class MovingBrick(Brick):
    def __init__(self, pos, size, type, dir = [1,0]):
        super().__init__(pos, size, type)
        self.dir = dir

#bewegt den MovingBrick und fragt ab ob er mit dem Bildschirmrand kollidiert
#wenn er dies tut, bewegt er sich in die andere Richtung (nur auf der Achse, auf der es kollidiert)
    def move(self, gameManager):
        self.box[0] += self.dir[0]
        self.box[1] += self.dir[1]
        if self.box[0] > gameManager.screenSize[0] or self.box[0] < 0:
            self.dir[0] * (-1)
        if self.box[1] > gameManager.screenSize[1] or self.box[1] < 0:
            self.dir[1] * (-1)

#wenn der MovingBrick mit etwas kollidiert fragt er ab, was es ist
#ist es der Ball, so wird der MovingBrick auf die Liste markedForDestruction gesetzt
#kollidiert er mit einem anderen Objekt, so bewegt er sich zurrück
    def collision(self, obj, gameManager):
#        if obj.ObjectType == BALL:
#            gameManager.deleteObj(self)
#        else:
#            self.dir[0] * (-1)
#            self.dir[1] * (-1)
        self.dir[0] * (-1)
        self.dir[1] * (-1)

    def update(self, gameManager):
        self.move(gameManager)
