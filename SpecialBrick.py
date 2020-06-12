from Object import *


class SpecialBrick(GameObject):

    def draw(self, screen):
        pygame.draw.rect(screen, (252, 105, 255), self.box)

    def collision(self, obj, gameManager):
        gameManager.deleteObj(self)
