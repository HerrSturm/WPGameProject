from Object import *
import sys

class Ball(GameObject):

    def __init__(self, pos, size, type, direction):
        super().__init__(pos, size, type) #Nutze die Vererbung. Die Klasse erbt von GameObject
        self.directionx = direction[0]
        self.directiony = direction[1]
        self.directionMemory = []
        self.Centerx = 0
        self.Centery = 0
        self.Rage = 0

    def update(self, gameManager):
        self.move()

    def draw(self,screen):
        self.CenterRage()
        pygame.draw.circle(screen, (0, 225, 0), (self.Centerx, self.Centery), self.Rage)

    def move(self):
        self.box[0] += self.directionx
        self.box[1] += self.directiony
        if self.box[0] > 1400 or self.box[0] <0:
            self.directionx = self.directionx * -1
        if self.box[1] < 0:
            self.directiony = self.directiony * -1
        self.directionmemory()
        self.GameOver()

    def collision(self, obj, gameManager):
        self.directiony = self.directiony * -1

    def directionmemory(self):
        self.directionMemory.append((self.box[0],self.box[1]))

    def CenterRage(self):
        self.Centerx = self.box[0] + self.box[2]//2
        self.Centery = self.box[1] + self.box[3]//2
        self.Rage = self.box[2]//2

    def GameOver(self):
        if self.box[1] > 700:
            print("Game Over")
            sys.exit()            
