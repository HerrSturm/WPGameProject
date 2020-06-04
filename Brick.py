from Object import *

class Brick(GameObject):

    def collision(self, obj, gameManager):
        gameManager.deleteObj(self)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.box)
