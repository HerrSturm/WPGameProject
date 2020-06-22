import pygame

class Stab(object):
    def __init__(self):
        self.position = (100, 100)
        self.laenge = 30
        self.breite = 15
        self.color = (50, 50, 50)

    def move(self):
        pygame.event.get()
        pygame.mouse.get_pressed()[0]
        position = pygame.mouse.get_pos()
        if position[1] != 100:
            position[1] = 100
        while self.position > position:
            self.position += 1
        while self.position < position:
            self.position -= 1


            


        
