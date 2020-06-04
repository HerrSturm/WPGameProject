import pygame, sys

scale = 10 # Skalierung der Größenangaben, alle Angaben werden mit dieser multipliziert um die Objekte mit festen Abständen erzeugen zu können


#Basisklasse der Objekte, neue Klassen werden mittels Vererbung erstellt
#Es werden alle nötigen Funktion, sowie die Initialisierung der Box für Treffer vorgegeben.
class GameObject:
    def __init__(self, pos, size, type):
        global scale
        self.box = [pos[0]*scale,pos[1]*scale,size[0]*scale,size[1]*scale]
        self.type = type
        self.screen = pygame.display.get_surface()

    #Update-Funktion, die in jedem Zyklus aufgerufen wird, diese kann weitere Funktionen (z.B. Move-Funktionen) aufrufen
    #Es kann mittels des gameManager auf den GameManager zugegriffen werden. Dies ermöglicht das Erzeugen neuer Objekte oder das Löschen von bestehenden Objekten
    def update(self, gameManager):
        pass


    #Funktion, die die Zeichnungen durchführt
    def draw(self):
        pass

    #Funktion, die aufgerufen wird, wenn eine Kollision vorliegt
    #Die Funktion bekommt das Objekt, das kollidiert übergeben, somit können Eigenschaften dieses Objektes abgefragt werden (z.B. mit obj.type könnte der Typ des Objektes abgefragt werden)
    def collision(self, obj):
        pass

    #Funktion, die die Position nue setzt
    def changePos(self, newPos):
        self.box[0] = newPos[0]
        self.box[1] = newPos[1]


    """Getter Methoden für die Position, Laenge und Breite eines Objektes
       Ermöglicht es mit .x die x Position des Objekte, mit .y die y-Position des Objektes und mit .width und .height Laenge und Breite zu bekommen
       Es sind keine Klammer nötig (wegen des @property)
    """
    @property
    def x(self):
        return self.box[0]

    @property
    def y(self):
        return self.box[1]

    @property
    def width(self):
        return self.box[2]

    @property
    def height(self):
        return self.box[3]

    """Setter Methoden um komfortabel Werte des Objektes aendern zu koennen
       Aufruf mit .setX(wert) usw.
    """
    @x.setter
    def setX(self, val):
        self.box[0] = val

    @y.setter
    def setY(self, val):
        self.box[1] = val

    @x.setter
    def setWidth(self, val):
        self.box[2] = val

    @x.setter
    def setHeight(self, val):
        self.box[3] = val
