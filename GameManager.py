import pygame, sys
import Level


"""Klasse, die das Spiel und die Objekte verwaltet"""
class GameManager:
    def __init__(self):
        self.init()
        self.clock = pygame.time.Clock()
        self.currentLevel = Level.Level()
        self.markedForDestruction = []
        self.loop()

    #Initialisiert Pygame
    def init(self):
        self.screenSize = (1400, 800)
        self.screen = pygame.display.set_mode(self.screenSize)

    """markiert ein gegebenes Objekt zum Löschen
       Beispiel für das Löschen eines Objektes durch Kollision: gameManager.deleteObj(self)
    """
    def deleteObj(self, obj):
        self.markedForDestruction.append(obj)

    #Fuegt ein Objet der Liste der Levelobjekte hinzu
    def addObj(self,obj):
        self.currentLevel.objects.append(obj)

    #Löscht alle markierten Objekte aus der Liste
    def deleteMarkedObjects(self):
        for i in self.markedForDestruction:
            self.currentLevel.objects.remove(i)
        self.markedForDestruction = []


    #ruft von allen Objekten die update Funktion und die draw Funktion auf
    def updateLevelObjects(self):
        self.deleteMarkedObjects()
        self.currentLevel.update(self.screen, self)

    #Überprüft Kollisionen von allen Obbjekten mit einander
    #ruft im Falle einer Kollision die Kollisionsfunktion des Objektes auf
    def collisionChecker(self):
        for i in range(len(self.currentLevel.objects)):
            for j in range(i+1,len(self.currentLevel.objects)):
                if self.overlap(self.currentLevel.objects[i], self.currentLevel.objects[j]):
                    self.currentLevel.objects[i].collision(self.currentLevel.objects[j],self)
                    self.currentLevel.objects[j].collision(self.currentLevel.objects[i],self)

    #Funktion, die überprüft, ob zwei Objekte kollidieren
    def overlap(self,obj1,obj2):
        if obj1.box[0] <= obj2.box[0]+obj2.box[2] and obj1.box[0] + obj1.box[2] >= obj2.box[0]:
            if obj1.box[1] <= obj2.box[1]+obj2.box[3] and obj1.box[1] + obj1.box[3] >= obj2.box[1]:
                return True
        return False

    #Funktion für die Behandlung auftretender Events
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    #Hauptfunktion, die das Spiel am Laufen hält
    def loop(self):
        while True:
            self.handleEvent()
            self.screen.fill((0,0,0))
            self.updateLevelObjects()
            self.collisionChecker()
            pygame.display.flip()
            self.clock.tick(30)
