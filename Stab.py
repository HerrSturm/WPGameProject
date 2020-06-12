from Object import *

class Stab(GameObject):

    def update(self, gameManager):
        self.move()


    def draw(self,screen):
        pygame.draw.rect(screen, (255, 255, 255), self.box)

    def move(self):
        pass
