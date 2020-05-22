import pygame as pg 


class Button:
    def __init__(self,x, y, sx, sy, color, text = '', colorB = (255,255,0), size = 20, font = "arial"):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy 
        self.color = color
        self.text = text
        self.current = False
        self.colorB = colorB
        self.size = size
        self.font = font

    def  drawButton(self,display,outline = None):
        if outline:
            pg.draw.rect(display,self.color, (self.x-2,self.y-2,self.sx+4,self.sy+4))
        pg.draw.rect(display,self.color, (self.x,self.y,self.sx,self.sy))

        if self.text != "":
            font = pg.font.SysFont(self.font,self.size)
            text = font.render(self.text, 1, self.colorB)
            display.blit(text, (self.x + (self.sx / 2 - text.get_width()/2), self.y + (self.sy / 2 - text.get_height()/2)))

    def isOver(self, pos, click):
        if pos[0] > self.x and pos[0] < self.x + self.sx:
            if pos[1] > self.y and pos[1] < self.y + self.sy:
                self.current = True
                return click[0]
        else:
            self.current = False
            return False
    
