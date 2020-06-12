from Object import *

class Ball(GameObject):

    def __init__(self, pos, size, type, direction):
        super().__init__(pos, size, type) #Nutze die Vererbung. Die Klasse erbt von GameObject
        self.directionx = direction[0]
        self.directiony = direction[1]
        self.directionMemory = []

    def update(self, gameManager):
        self.move()

    def draw(self,screen):
        pygame.draw.rect(screen, (0, 0, 255), self.box)

    def move(self):
        self.box[0] += self.directionx
        self.box[1] += self.directiony
        if self.x > 1400 or self.x <0:
            self.directionx = self.directionx * -1
        self.directionmemory()

    def collision(self, obj, gameManager):
        self.directiony = self.directiony * -1

    def directionmemory(self):
        self.directionMemory.append((self.x,self.y))
