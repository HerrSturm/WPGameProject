from Object import *

class Brick(GameObject):

    def collision(self, obj, gameManager):
        gameManager.deleteObj(self)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.box)
