from Object import *

class Stab(GameObject):

    def __init__(self, pos, size):
        super().__init__(self.box) 
        

    def update(self, gameManager):
        self.move
        self.draw

    def draw(self,screen):
        pygame.draw.rect(screen, (255, 255, 255), self.box)

    def move(self):
        pass
