import pygame as pg
vec = pg.math.Vector2

class TextBox:
    def __init__(self,x,y,sirina,visina,border = 0):
        self.x = x
        self.y = y
        self.visina = visina
        self.sirina = sirina
        self.pos = vec(x,y)
        self.size = vec(sirina,visina)
        self.image = pg.Surface((sirina,visina))
        self.bg_colour = (124,124,124)
        self.active_colour = (255,255,255)
        self.active = False
        self.text = ""
        self.font = pg.font.SysFont("arial",22)
        self.textColour = (0,0,0)
        self.border = border
        self.borderColour = (0,0,0)
        self.number = [48,49,50,51,52,53,54,55,56,57]
        self.specialCharacter = [8,32,13]



    def draw(self,screen):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.bg_colour)
            else:
                self.image.fill(self.borderColour)
                pg.draw.rect(self.image,self.bg_colour,(self.border,self.border,
                self.sirina - self.border*2,self.visina -self.border*2))


            text = self.font.render(self.text,False, self.textColour)
            textVisina = text.get_height()
            textSirina = text.get_width()
            self.image.blit(text,(self.border*2,(self.visina - textVisina)//2))
        else:
            if self.border == 0:
                self.image.fill(self.active_colour)
            else:
                self.image.fill(self.borderColour)
                pg.draw.rect(self.image,self.active_colour,(self.border,self.border,
                self.sirina - self.border*2,self.visina -self.border*2))

        text = self.font.render(self.text,False, self.textColour)
        textVisina = text.get_height()
        textSirina = text.get_width()
        if textSirina < self.sirina - self.border*2:
            self.image.blit(text,(self.border*2,(self.visina - textVisina)//2))
        else:
            self.image.blit(text,((self.border*2) + (self.sirina - textSirina - self.border*3),
            (self.visina - textVisina)//2))
        
        screen.blit(self.image,self.pos)

    def addText(self,key):
        try:
            if chr(key).isalpha():
                text = list(self.text)
                text.append(chr(key))
                self.text = ''.join(text)
                print(self.text)
            elif key == 8:
                text = list(self.text)
                text.pop()
                self.text = ''.join(text)
            elif key == 32:
                text = list(self.text)
                text.append(' ')
                self.text = ''.join(text)
            elif key == 48:
                text = list(self.text)
                text.append('0')
                self.text = ''.join(text)
            elif key == 49:
                text = list(self.text)
                text.append('1')
                self.text = ''.join(text)
            elif key == 50:
                text = list(self.text)
                text.append('2')
                self.text = ''.join(text)
            elif key == 51:
                text = list(self.text)
                text.append('3')
                self.text = ''.join(text)
            elif key == 52:
                text = list(self.text)
                text.append('4')
                self.text = ''.join(text)
            elif key == 53:
                text = list(self.text)
                text.append('5')
                self.text = ''.join(text)
            elif key == 54:
                text = list(self.text)
                text.append('6')
                self.text = ''.join(text)
            elif key == 55:
                text = list(self.text)
                text.append('7')
                self.text = ''.join(text)
            elif key == 56:
                text = list(self.text)
                text.append('8')
                self.text = ''.join(text)
            elif key == 57:
                text = list(self.text)
                text.append('9')
                self.text = ''.join(text)
              
            else:
                print("not a valid key")
        except:
            print(key)

    def checkClick(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.sirina:
            if pos[1] > self.y and pos[1] < self.y + self.visina:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False
    
    def returnValue(self):
        return self.text
            
