import pygame as pg
import math
import random
from TextBox_class import *
from ButtonClass import *
vec = pg.math.Vector2
import time
import threading


pg.init()


mapa = pg.image.load('covid19\\NEWMAP.png')
icon = pg.image.load('covid19\\iconCorona.png')
coronaImage = pg.image.load('covid19\\corona2.jpg')

humansize = 1
odmeraj = 0.1
duzina = 500
rangelow = 3
rangehigh = duzina - rangelow
stopClick = False
respiratortime = 30
respirators = 0


black = (0, 0, 0, 255)
white = (83, 83, 83, 255)
healthycolor = (255, 255, 0)
dormantcolor = (0, 255, 255)
infectedcolor = (255, 0, 0)

numsurvived = 0
numhealthy = 0
numdormant = 0
numinfected = 0
numdead = 0



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
    
    def endCurrent(self):
        self.current = False

    def checkUpdate(self):
        return self.current

    def screenUpdate(self):
        if self.current:
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.screen

class Citizen:
    
    def sleepcheck(self):
        if not self.move:
            return

        global stopClick

        while stopClick:
            time.sleep(odmeraj)
            for event in pg.event.get():
                pass
            mousePos = pg.mouse.get_pos()
            mouseClick = pg.mouse.get_pressed()
            startButtonSim = startButton.isOver(mousePos, mouseClick)
            if startButtonSim:
                stopClick = False

        if self.begin > 0:
            self.begin += 1

        time.sleep(odmeraj)
        for event in pg.event.get():
            pass
        mousePos = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()
        stopButtonSim = stopButton.isOver(mousePos,mouseClick)
        if stopButtonSim:
            stopClick = True


        if self.color == infectedcolor:
            #dodatno cekanje za inficirane
            time.sleep(odmeraj)

        global numinfected, numdormant, numhealthy, numsurvived, numdead
            
        if self.color == healthycolor and not self.survived and \
        (simScreen.returnTitle().get_at([self.x - 1, self.y]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x, self.y - 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x, self.y + 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y + 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x - 1, self.y + 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y - 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x - 1, self.y - 1]) == dormantcolor or \
        simScreen.returnTitle().get_at([self.x, self.y]) == dormantcolor or\
        simScreen.returnTitle().get_at([self.x - 1, self.y]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x, self.y - 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x, self.y + 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y + 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x - 1, self.y + 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x + 1, self.y - 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x - 1, self.y - 1]) == infectedcolor or \
        simScreen.returnTitle().get_at([self.x, self.y]) == infectedcolor):
            self.color = dormantcolor
            self.begin = 1
            numdormant += 1
            numhealthy -= 1
            labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,20))
            simScreen.returnTitle().blit(labelDormant,(435,520))

            labelHealthy = myfont2.render(str(numhealthy),1,(0,255,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (340,520,50,20))
            simScreen.returnTitle().blit(labelHealthy,(340,520))
    

        elif self.color == dormantcolor and self.begin > 150:
            self.color = infectedcolor
            numinfected += 1
            numdormant -= 1
            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))
            labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,20))
            simScreen.returnTitle().blit(labelDormant,(435,520))
        #150 odmeraja + 50 odmeraja
        elif self.color == infectedcolor and self.begin > 200:
            global respirators
            chance = 50
            if self.disease < 3:
                chance -= 20
            if self.years < 4:
                chance += 50
            elif self.years < 6:
                chance += 30
            elif self.years < 8:
                chance += 15
            elif self.years < 10:
                chance -= 10
            elif self.years == 10:
                chance -= 30
            if respirators > 0:
                chance += 30
                respirators -= 1
                labelRespirators = myfont4.render(str(respirators),1,(190,190,190)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (235,570,60,25))
                simScreen.returnTitle().blit(labelRespirators,(260,575))
                timer = time.perf_counter()
                pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                while time.perf_counter() - timer < respiratortime:
                    time.sleep(odmeraj)
                respirators += 1
                labelRespirators = myfont4.render(str(respirators),1,(190,190,190)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (235,570,60,25))
                simScreen.returnTitle().blit(labelRespirators,(260,575))
                

            choose = random.randint(1, 100)
            if choose <= chance:
                numsurvived += 1
                labelSurvived = myfont3.render(str(numsurvived),1,(255,255,255)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (160,551,50,43))
                simScreen.returnTitle().blit(labelSurvived,(170,560)) 
                self.survived = True
                self.color = healthycolor
            else:
                numdead += 1
                labelDead = myfont2.render(str(numdead),1,(0,0,0)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,570,50,20))
                simScreen.returnTitle().blit(labelDead,(435, 570)) 
                self.move = False 
            
            numinfected -= 1
            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))

            
            if numinfected == 0 and numdormant == 0:
                stopClick = True    



    def randompath(self, side):
        while(self.move):
            availablesides = []
            if side == "desno":
                
                if  self.x + 4 < duzina and mapa.get_at([self.x + 4, self.y]) == white:
                    availablesides.append("desno")
                if self.y + 4 < duzina and mapa.get_at([self.x, self.y + 4]) == white:
                    availablesides.append("dole")
                if self.y - 4 > 0 and mapa.get_at([self.x, self.y - 4]) == white:
                    availablesides.append("gore")

                if len(availablesides) > 0:
                    r = random.randint(0, len(availablesides) - 1)
                    if availablesides[r] == "desno":
                        while mapa.get_at([self.x, self.y - 4]) == white or  mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1
                    
                    elif availablesides[r] == "dole":
                        while mapa.get_at([self.x - 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                            pg.display.update()
                            self.y += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1

                    else:
                        while mapa.get_at([self.x - 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                            pg.display.update()
                            self.y -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1
                    
                    side = availablesides[r]
                    continue
                
                else:
                    side = "levo"
                    continue


            elif side == "levo":
                if  self.x - 4 > 0 and mapa.get_at([self.x - 4, self.y]) == white:
                    availablesides.append("levo")
                if self.y + 4 < duzina and mapa.get_at([self.x, self.y + 4]) == white:
                    availablesides.append("dole")
                if self.y - 4 > 0 and mapa.get_at([self.x, self.y - 4]) == white:
                    availablesides.append("gore")

                if len(availablesides) > 0:
                    r = random.randint(0, len(availablesides) - 1)
                    if availablesides[r] == "levo":
                        while mapa.get_at([self.x, self.y - 4]) == white or  mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
                    
                    elif availablesides[r] == "dole":
                        while mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                            pg.display.update()
                            self.y += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1
                        

                    else:
                        while mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                            pg.display.update()
                            self.y -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1
                    
                    side = availablesides[r]
                    continue
                
                else:
                    side = "desno"
                    continue

            
            
            elif side == "dole":
                if  self.y + 4 < duzina and mapa.get_at([self.x, self.y + 4]) == white:
                    availablesides.append("dole")
                if self.x + 4 < duzina and mapa.get_at([self.x + 4, self.y]) == white:
                    availablesides.append("desno")
                if self.x - 4 > 0 and mapa.get_at([self.x - 4, self.y]) == white:
                    availablesides.append("levo")

                if len(availablesides) > 0:
                    r = random.randint(0, len(availablesides) - 1)
                    
                    if availablesides[r] == "dole":
                        while mapa.get_at([self.x - 4, self.y]) == white or mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                            pg.display.update()
                            self.y += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1

                    elif availablesides[r] == "desno":
                        while mapa.get_at([self.x, self.y - 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1

                    else:
                        while mapa.get_at([self.x, self.y - 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
                    
                    side = availablesides[r]
                    continue
                
                else:
                    side = "gore"
                    continue

                
            elif side == "gore":
                if  self.y - 4 > 0 and mapa.get_at([self.x, self.y - 4]) == white:
                    availablesides.append("gore")
                if self.x + 4 < duzina and mapa.get_at([self.x + 4, self.y]) == white:
                    availablesides.append("desno")
                if self.x - 4 > 0 and mapa.get_at([self.x - 4, self.y]) == white:
                    availablesides.append("levo")

                if len(availablesides) > 0:
                    r = random.randint(0, len(availablesides) - 1)
                    
                    if availablesides[r] == "gore":
                        while mapa.get_at([self.x - 4, self.y]) == white or mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                            pg.display.update()
                            self.y -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1

                    elif availablesides[r] == "desno":
                        while mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x += 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1

                    else:
                        while mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x -= 1
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
                    
                    side = availablesides[r]
                    continue
                
                else:
                    side = "dole"
                    continue


    def goto(self):
        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y, humansize, humansize))
        pg.display.update()
        i = 1
        strana = ""
        self.sleepcheck()
        while i < duzina:
            if self.x + i + 2 < duzina and mapa.get_at([self.x + i, self.y]) != black:
                strana = "desno"
                break
            elif self.x > i + 2 and mapa.get_at([self.x - i, self.y]) != black:
                strana = "levo"
                break
            elif self.y + i + 2 < duzina and mapa.get_at([self.x, self.y + i]) != black:
                strana = "dole"
                break
            elif self.y > i + 2 and mapa.get_at([self.x, self.y - i]) != black:
                strana = "gore"
                break
            i += 1
        if strana == "desno":
            i += self.x
            while self.x < i:
                self.sleepcheck()
                pg.draw.rect(simScreen.returnTitle(), black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                pg.display.update()
                self.x += 1
            self.randompath("desno")

        elif strana == "levo":
            i = self.x - i
            while self.x > i:
                self.sleepcheck()
                pg.draw.rect(simScreen.returnTitle(), black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                pg.display.update()
                self.x -= 1
            self.randompath("levo")

        elif strana == "dole":
            i += self.y
            while self.y < i:
                self.sleepcheck()
                pg.draw.rect(simScreen.returnTitle(), black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                pg.display.update()
                self.y += 1
            self.randompath("dole")

        else:
            i = self.y - i
            while self.y > i:
                self.sleepcheck()
                pg.draw.rect(simScreen.returnTitle(), black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                pg.display.update()
                self.y -= 1
            self.randompath("gore")
    


    def __init__(self):
        self.survived = False
        self.years = random.randint(1, 10)
        #1 - 10 godina (3), 11 - 18 (2), 19 - 30 (2), 31 - 50 (2), 51 - 80(1)
        self.disease = random.randint(1, 10)
        #1 - 2 ima bolest, 3 - 10 nema
        self.begin = 0
        self.move = True
        self.x = random.randint(rangelow, rangehigh)
        self.y = random.randint(rangelow, rangehigh)
        while mapa.get_at([self.x, self.y]) != black:
            self.x = random.randint(rangelow, rangehigh)
            self.y = random.randint(rangelow, rangehigh)
    
def spawnfirst():
    c = Citizen()
    c.color = dormantcolor
    c.begin = 1
    c.goto()

def spawn():
    c = Citizen()
    c.color = healthycolor
    c.goto()



menuScreen = Screen("COVID 19",600,400)
tempScreen = Screen("temp screen",400,300)
simScreen = Screen("Simulator of COVID 19",500,600,(0,0,0))
mainClock = pg.time.Clock()

myfont = pg.font.SysFont("Arial", 20)
myfont2 = pg.font.SysFont("freesansbold.ttf", 15)
myfont3 = pg.font.SysFont("freesansbold.ttf", 40)
myfont4 = pg.font.SysFont("freesansbold.ttf", 22)
label = myfont.render("  Enter the number of people =>",1, (255,255,0))
labelReady = Button(405,170,120,70,(255,0,0),"READY!")
labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
labelCity = myfont.render("          Choose a real city =>",1, (255,255,0))
dropButton = Button(258,153,80,15,(40,255,40),"                               ")
myfont2 = pg.font.SysFont("Arial", 17)
labelSee = myfont2.render(" click to see",1, (0,0,0))
LabelGloves = myfont.render("     Percent of wear gloves =>",1,(255,255,0))
LabelMasks = myfont.render("     Percent of wear masks => ",1,(255,255,0))
LabelRespirator = myfont.render("Enter the number of respirators =>",1,(255,255,0))
LabelObedient = myfont4.render(" OBEDIENCE",1,(255,255,0))
LabelPercent = myfont3.render(" % ",1,(255,255,0))
LabelBoolMasks = myfont3.render("  MASKS ",1,(255,255,0))
LabelBoolGloves = myfont3.render(" GLOVES ",1,(255,255,0))

startButton = Button(10,500,145,40,(0,0,255),"START",(255,255,255))
stopButton = Button(165,500,145,40,(0,0,255),"STOP",(255,255,255))
redButton = Button(510,332,40,40,(255,0,0),"")
redButton2 = Button(510,270,40,40,(255,0,0),"")
refreshButton = Button(404,313,80,20,(255,0,0),"REFRESH")







win = menuScreen.makeDisplay()
    
textBoxes = []
textBoxO = TextBox(255,29,100,50,4)
textBox1 = TextBox(700,700,100,50,4)
textBoxGloves = TextBox(255,195,100,50,4)
textBoxMasks = TextBox(255,270,100,50,4)
textBoxRespirator = TextBox(255,338,100,50,4)
textBoxObedient = TextBox(426,60,90,50,4)
textBoxes.append(textBoxO)
textBoxes.append(textBox1)
textBoxes.append(textBoxGloves)
textBoxes.append(textBoxMasks)
textBoxes.append(textBoxRespirator)
textBoxes.append(textBoxObedient)
running = True


pg.display.set_icon(icon)

pg.display.flip()
while running:
    menuScreen.screenUpdate()
    tempScreen.screenUpdate()
    mousePos = pg.mouse.get_pos()
    mouseClick = pg.mouse.get_pressed()
    if textBoxO.returnValue() == '':
        n = 0
    else:
        n = int(textBoxO.returnValue())

    
            

    if menuScreen.checkUpdate():
        
        dropButton.drawButton(menuScreen.returnTitle())
        tempDropButton = dropButton.isOver(mousePos, mouseClick)
        if tempDropButton:
            menuScreen.returnTitle().blit(coronaImage,(0,0))
            x = 30
            i = 0
            for i in range(5):
                textBox1 = TextBox(255,100,100,50,4)
                textBoxes.append(textBox1)
                textBox1.draw(menuScreen.returnTitle())
                if i == 0:
                    city = myfont.render("Novi Sad, ",1,(255,255,0))
                    menuScreen.returnTitle().blit(city,(x,200))
                    x += 75
                elif i == 1:
                    city = myfont.render("New York, ",1,(255,255,0))
                    menuScreen.returnTitle().blit(city,(x,200))
                    x += 80
                elif i == 2:
                    city = myfont.render("Milano,",1,(255,255,0))
                    menuScreen.returnTitle().blit(city,(x,200))
                    x += 57
                elif i == 3:
                    city = myfont.render("Valjevo, ",1,(255,255,0))
                    menuScreen.returnTitle().blit(city,(x,200))
                    x += 60
                elif i == 4:
                    city = myfont.render("Svet.",1,(255,255,0))
                    menuScreen.returnTitle().blit(city,(x,200))
                    x += 75
        
        simScreenButton = labelReady.isOver(mousePos,mouseClick)
        if not tempDropButton:
            menuScreen.returnTitle().blit(coronaImage,(0,0))
            menuScreen.returnTitle().blit(LabelGloves, (0,210))
            menuScreen.returnTitle().blit(LabelMasks, (0,280))
            textBoxGloves.draw(menuScreen.returnTitle())
            textBoxMasks.draw(menuScreen.returnTitle())
        textBoxRespirator.draw(menuScreen.returnTitle())
        labelReady.drawButton(menuScreen.returnTitle(),True)
        menuScreen.returnTitle().blit(label,(0,40))
        menuScreen.returnTitle().blit(labelCity, (0,120))
        menuScreen.returnTitle().blit(LabelObedient,(418,40))
        menuScreen.returnTitle().blit(LabelPercent, (510,70))
        menuScreen.returnTitle().blit(LabelBoolMasks, (380,280))
        menuScreen.returnTitle().blit(LabelBoolGloves, (380,340))
        #greenButton.drawButton(menuScreen.returnTitle(),4)
        redButton.drawButton(menuScreen.returnTitle(),4)
        redButton2.drawButton(menuScreen.returnTitle(),4)
        redButtonClick = redButton.isOver(mousePos,mouseClick)
        redButtonClick2 = redButton2.isOver(mousePos,mouseClick)
        refreshButton.drawButton(menuScreen.returnTitle())
        refreshButtonClick = refreshButton.isOver(mousePos,mouseClick)

        if redButtonClick:
            redButton = Button(510,332,40,40,(0,255,0),"")
            
        elif redButtonClick2:
           redButton2 = Button(510,270,40,40,(0,255,0),"")

        if refreshButtonClick:
            redButton = Button(510,332,40,40,(255,0,0),"")
            redButton2 = Button(510,270,40,40,(255,0,0),"")

        textBoxObedient.draw(menuScreen.returnTitle())
        
        
        menuScreen.returnTitle().blit(LabelRespirator, (0,350))
            
        textBoxO.draw(menuScreen.returnTitle())
        textBox1.draw(menuScreen.returnTitle())
        
        menuScreen.returnTitle().blit(labelSee, (263,150))
   
        if simScreenButton:
            win = simScreen.makeDisplay()
                
            menuScreen.endCurrent()

    
    elif simScreen.checkUpdate:
        
        #simScreen.returnTitle().fill((0, 0, 0))
        simScreen.returnTitle().blit(mapa, (0, 0))
        
        startButtonSim = startButton.isOver(mousePos,mouseClick)
        stopButtonSim = stopButton.isOver(mousePos,mouseClick)
        
        startButton.drawButton(simScreen.returnTitle())
        stopButton.drawButton(simScreen.returnTitle())
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,550,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,550,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(5,550,210,45))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(225,550,85,45))

        labelSim = myfont2.render("Healthy: ",1,(0,255,0))
        simScreen.returnTitle().blit(labelSim,(332,502))
        labelSim = myfont2.render("Infected: ",1,(255,0,0))
        simScreen.returnTitle().blit(labelSim,(336,552))
        labelSim = myfont2.render("Dead: ",1,(0,0,0))
        simScreen.returnTitle().blit(labelSim,(430,552))
        labelSim = myfont2.render("Dormant: ",1,(70,70,70))
        simScreen.returnTitle().blit(labelSim,(422,502))
        labelSim = myfont2.render("Respiratori: ",1,(255,255,255))
        simScreen.returnTitle().blit(labelSim,(230,551))
        
        labelSim = myfont3.render("Survived: ",1,(255,255,255))
        simScreen.returnTitle().blit(labelSim,(15,560))
        

        if startButtonSim:
            if textBoxRespirator.returnValue() == "":
                respirators = 0
            else:
                respirators = int(textBoxRespirator.returnValue()) 
            #POCETAK
            threads = []
            f = threading.Thread(target=spawnfirst)
            if n == 0:
                numdormant = 0
            else:
                numdormant += 1

            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))

            labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,20))
            simScreen.returnTitle().blit(labelDormant,(435,520))

            labelSurvived = myfont3.render(str(numsurvived),1,(255,255,255)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (160,551,50,43))
            simScreen.returnTitle().blit(labelSurvived,(170,560)) 

            labelRespirators = myfont4.render(str(respirators),1,(190,190,190)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (235,570,60,25))
            simScreen.returnTitle().blit(labelRespirators,(260,575))

            labelHealthy = myfont2.render(str(numhealthy),1,(0,255,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (340,520,50,20))
            simScreen.returnTitle().blit(labelHealthy,(353,520))

            labelDead = myfont2.render(str(numdead),1,(0,0,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,570,50,20))
            simScreen.returnTitle().blit(labelDead,(435, 570))

            

            f.start()
            threads.append(f)
            for _ in range(n - 1):
                while stopClick:
                    time.sleep(odmeraj)
                
                numhealthy += 1
                labelHealthy = myfont2.render(str(numhealthy),1,(0,255,0)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (340,520,50,20))
                simScreen.returnTitle().blit(labelHealthy,(340,520))

                t = threading.Thread(target=spawn)   
                t.start()
                threads.append(t)

            for thread in threads:
                thread.join()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                win = menuScreen.makeDisplay()
                simScreen.endCurrent()
        
    
    Click = False
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            


        if event.type == pg.MOUSEBUTTONDOWN:
            for box in textBoxes:
                box.checkClick(pg.mouse.get_pos())
            if event.button:
                Click = True
            

        if event.type == pg.KEYDOWN:
            for box in textBoxes:
                if box.active:
                    box.addText(event.key)
                        

    pg.display.update()
