from Object import *

class Brick(GameObject):

    def collision(self, obj, gameManager):
        #        if obj.ObjectType == BALL:
        #            gameManager.deleteObj(self)
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.box)
