from Object import *

class Ball(GameObject):

    def __init__(self, pos, size, type, direction):
        #super().__init__(.....) Nutze die Vererbung. Die Klasse erbt von GameObject
        directionx = direction[0]
        directiony = direction[1]
        directionMemory = []

    def update(self, gameManager):
        move()

    def draw(self,screen):
        pygame.draw.rect(screen, (0, 0, 255), self.box)

    def move(self):
        self.x += directionx
        self.y += directiony
        if self.x > 1400 or self.x <0:
            directionx = directionx * -1
        directionmemory()

    def collision(self, obj, gameManager):
        directiony = directiony * -1

    def directionmemory(self):
        ory.append((self.x,self.y))
