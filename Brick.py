from Object import *
cobble = pygame.image.load('Graphics/cobble.png')
class Brick(GameObject):

    def collision(self, obj, gameManager):
        gameManager.deleteObj(self)

    def draw(self, screen):
        screen.blit(cobble, self.box)
