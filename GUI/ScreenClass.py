import pygame as pg

class Screen():
    def __init__(self, title, x, y, fill = (40,40,40)):
        self.title = title
        self.x = x
        self.y = y
        self.fill = fill
        self.current = False
    
    def makeDisplay(self):
        pg.display.set_caption(self.title)
        self.current = True
        self.screen = pg.display.set_mode((self.x, self.y))
        self.screen.fill(self.fill)
    
    def endCurrent(self):
        self.current = False

    def returnCurrent(self):
        return self.current

    def screenUpdate(self):
        if self.current:
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.screen

