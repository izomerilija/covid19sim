import pygame as pg
import math
import random
from TextBox_class import *
from ButtonClass import *
vec = pg.math.Vector2
import time
import threading


pg.init()


<<<<<<< HEAD
=======
mapa = pg.image.load('proj\\mapa.png')
icon = pg.image.load('proj\\iconCorona.png')
coronaImage = pg.image.load('proj\\corona2.jpg')

>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
humansize = 1
odmeraj = 0.1
duzina = 500
rangelow = 3
rangehigh = duzina - rangelow
<<<<<<< HEAD

<<<<<<< HEAD
mapa = pg.image.load('mapa.png')  

black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
healthycolor = (0, 160, 110)
=======

black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
healthycolor = (255,77,0)
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
dormantcolor = (0, 50, 255)
infectedcolor = (220, 0, 0)

=======
stopClick = False
respiratortime = 30
respirators = 0


black = (0, 0, 0, 255)
white = (83, 83, 83, 255)
healthycolor = (255, 255, 0)
dormantcolor = (0, 255, 255)
infectedcolor = (255, 0, 0)

numsurvived = 0
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
numhealthy = 0
numdormant = 0
numinfected = 0
numdead = 0

<<<<<<< HEAD
<<<<<<< HEAD
buttonstop = False
=======
#buttonstop = False
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
=======
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129


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

<<<<<<< HEAD

stopClick = False
class Citizen:
    
    def sleepcheck(self):
        time.sleep(odmeraj)
        global stopClick
        if stopButton.isOver(mousePos,mouseClick):
            stopClick = True
            print("eee")
        while stopClick:
           time.sleep(odmeraj)
           
        
            
        if self.color == healthycolor:
            global numdormant
            if simScreen.returnTitle().get_at([self.x - 1, self.y]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x - 1, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x - 1, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y]) == infectedcolor:

                self.color = dormantcolor
                numdormant += 1
                self.begin = time.perf_counter()
                labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,15))
                simScreen.returnTitle().blit(labelDormant,(435,520))
    #probno - 10 sekundi samo da se vidi razlika
        elif self.color == dormantcolor and time.perf_counter() - self.begin > 10:
            self.color = infectedcolor
            global numinfected
            numinfected += 1
            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))
           

    def sleepcheck(self):
        time.sleep(odmeraj)
        while(buttonstop):
            time.sleep(odmeraj)
        if self.color == healthycolor:
            global numdormant
            if simScreen.returnTitle().get_at([self.x - 1, self.y]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x - 1, self.y + 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x + 1, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x - 1, self.y - 1]) == infectedcolor or \
            simScreen.returnTitle().get_at([self.x, self.y]) == infectedcolor:

                self.color = dormantcolor
                numdormant += 1
                self.begin = time.perf_counter()
    #probno - 10 sekundi samo da se vidi razlika
        elif self.color == dormantcolor and time.perf_counter() - self.begin > 10:
            self.color = infectedcolor
            global numinfected
            numinfected += 1

    def randompath(self, side):
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
=======
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
                timer = time.perf_counter()
                pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                while time.perf_counter() - timer < respiratortime:
                    time.sleep(odmeraj)
                respirators += 1

            choose = random.randint(1, 100)
            if choose <= chance:
                numsurvived += 1
                self.survived = True
                self.color = healthycolor
            else:
                numdead += 1
                self.move = False 
            
            numinfected -= 1
            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))

            labelDead = myfont2.render(str(numdead),1,(0,0,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,570,50,20))
            simScreen.returnTitle().blit(labelDead,(435, 570)) 
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
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x += 1
                
                elif availablesides[r] == "dole":
                    while mapa.get_at([self.x - 4, self.y]) == white:
=======
                    
                    elif availablesides[r] == "dole":
                        while mapa.get_at([self.x - 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                            pg.display.update()
                            self.y += 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    self.y += 1

                else:
                    while mapa.get_at([self.x - 4, self.y]) == white:
=======

                    else:
                        while mapa.get_at([self.x - 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                            pg.display.update()
                            self.y -= 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    self.y -= 1
                
                self.randompath(availablesides[r])
                return
            
            else:
                self.randompath("levo")
                return


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
=======
                    
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
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x -= 1
                
                elif availablesides[r] == "dole":
                    while mapa.get_at([self.x + 4, self.y]) == white:
=======
                    
                    elif availablesides[r] == "dole":
                        while mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                            pg.display.update()
                            self.y += 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    self.y += 1
                    

                else:
                    while mapa.get_at([self.x + 4, self.y]) == white:
=======
                        

                    else:
                        while mapa.get_at([self.x + 4, self.y]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                            pg.display.update()
                            self.y -= 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    self.y -= 1
=======
                    
                    side = availablesides[r]
                    continue
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                
                else:
                    side = "desno"
                    continue

            
            
<<<<<<< HEAD
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
=======
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
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        self.y += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    self.y += 1

                elif availablesides[r] == "desno":
                    while mapa.get_at([self.x, self.y - 4]) == white:
=======

                    elif availablesides[r] == "desno":
                        while mapa.get_at([self.x, self.y - 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x += 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x += 1

                else:
                    while mapa.get_at([self.x, self.y - 4]) == white:
=======

                    else:
                        while mapa.get_at([self.x, self.y - 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x -= 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x -= 1
=======
                    
                    side = availablesides[r]
                    continue
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                
                else:
                    side = "gore"
                    continue

<<<<<<< HEAD
            
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
=======
                
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
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        self.y -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    self.y -= 1

                elif availablesides[r] == "desno":
                    while mapa.get_at([self.x, self.y + 4]) == white:
=======

                    elif availablesides[r] == "desno":
                        while mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x += 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x += 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x += 1

                else:
                    while mapa.get_at([self.x, self.y + 4]) == white:
=======

                    else:
                        while mapa.get_at([self.x, self.y + 4]) == white:
                            self.sleepcheck()
                            pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                            pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                            pg.display.update()
                            self.x -= 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                        self.sleepcheck()
                        pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        self.x -= 1
<<<<<<< HEAD
                    self.sleepcheck()
                    pg.draw.rect(simScreen.returnTitle(), white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(simScreen.returnTitle(), self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    self.x -= 1
=======
                    
                    side = availablesides[r]
                    continue
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                
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
<<<<<<< HEAD
=======
        self.survived = False
        self.years = random.randint(1, 10)
        #1 - 10 godina (3), 11 - 18 (2), 19 - 30 (2), 31 - 50 (2), 51 - 80(1)
        self.disease = random.randint(1, 10)
        #1 - 2 ima bolest, 3 - 10 nema
        self.begin = 0
        self.move = True
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
        self.x = random.randint(rangelow, rangehigh)
        self.y = random.randint(rangelow, rangehigh)
        while mapa.get_at([self.x, self.y]) != black:
            self.x = random.randint(rangelow, rangehigh)
            self.y = random.randint(rangelow, rangehigh)
    
<<<<<<< HEAD
def spawninfected():
<<<<<<< HEAD
    c = Citizen()
    c.color = infectedcolor
=======
def spawnfirst():
    c = Citizen()
    c.color = dormantcolor
    c.begin = 1
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
    c.goto()

def spawn():
    c = Citizen()
    c.color = healthycolor
    c.goto()
<<<<<<< HEAD
=======
    c = Citizen()
    c.color = infectedcolor
    c.goto()

def spawn():
    c = Citizen()
    c.color = healthycolor
    c.goto()

def sleepCitizen(odmeraj):
    while True:
        time.sleep(odmeraj) 
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
=======

>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129


menuScreen = Screen("COVID 19",560,400)
tempScreen = Screen("temp screen",400,300)
<<<<<<< HEAD
<<<<<<< HEAD
simScreen = Screen("Simulator",500,600,(0,0,0))


myfont = pg.font.SysFont("Arial", 20)
label = myfont.render(" Enter the number of people:",1, (255,255,0))
labelReady = Button(220,210,70,50,(255,0,0),"READY!")
labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
labelCity = myfont.render(" Choose a real city =>",1, (255,255,0))
dropButton = Button(199,156,80,15,(40,40,40),"                               ")
=======
simScreen = Screen("Simulator  of COVID 19",500,600,(0,0,0))
mainClock = pg.time.Clock()

myfont = pg.font.SysFont("Arial", 20)
myfont2 = pg.font.SysFont("freesansbold.ttf", 15)
label = myfont.render("  Enter the number of people =>",1, (255,255,0))
labelReady = Button(405,170,120,70,(255,0,0),"READY!")
labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
labelCity = myfont.render("          Choose a real city =>",1, (255,255,0))
dropButton = Button(248,153,80,15,(40,40,40),"                               ")
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
=======
simScreen = Screen("Simulator of COVID 19",500,600,(0,0,0))
mainClock = pg.time.Clock()

myfont = pg.font.SysFont("Arial", 20)
myfont2 = pg.font.SysFont("freesansbold.ttf", 15)
label = myfont.render("  Enter the number of people =>",1, (255,255,0))
labelReady = Button(405,170,120,70,(255,0,0),"READY!")
labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
labelCity = myfont.render("          Choose a real city =>",1, (255,255,0))
dropButton = Button(248,153,80,15,(40,40,40),"                               ")
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
myfont2 = pg.font.SysFont("Arial", 17)
labelSee = myfont2.render(" click to see",1, (0,0,0))
LabelGloves = myfont.render("     Percent of wear gloves =>",1,(255,255,0))
LabelMasks = myfont.render("     Percent of wear masks => ",1,(255,255,0))
LabelRespirator = myfont.render("Enter the number of respirators =>",1,(255,255,0))
<<<<<<< HEAD

startButton = Button(0,500,150,50,(0,0,255),"START",(255,255,255))
stopButton = Button(160,500,150,50,(0,0,255),"STOP",(255,255,255))

<<<<<<< HEAD
startButton = Button(0,500,150,50,(0,0,255),"START", (255, 255, 255))
stopButton = Button(160,500,150,50,(0,0,255),"STOP", (255, 255, 255))

=======
=======

startButton = Button(0,500,150,50,(0,0,255),"START",(255,255,255))
stopButton = Button(160,500,150,50,(0,0,255),"STOP",(255,255,255))


>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129



<<<<<<< HEAD

>>>>>>> f942762401beaa9973464376db4637bc688a5b68
=======
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129

win = menuScreen.makeDisplay()
    
textBoxes = []
textBoxO = TextBox(240,29,100,50,4)
textBox1 = TextBox(700,700,100,50,4)
textBoxGloves = TextBox(240,195,100,50,4)
textBoxMasks = TextBox(240,270,100,50,4)
textBoxRespirator = TextBox(240,338,100,50,4)
textBoxes.append(textBoxO)
textBoxes.append(textBox1)
textBoxes.append(textBoxGloves)
textBoxes.append(textBoxMasks)
textBoxes.append(textBoxRespirator)
running = True

<<<<<<< HEAD
icon = pg.image.load('covid19\\iconCorona.png')
pg.display.set_icon(icon)
coronaImage = pg.image.load("covid19\\corona2.jpg")
=======

pg.display.set_icon(icon)

>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
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
                textBox1 = TextBox(240,100,100,50,4)
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
        
        
        menuScreen.returnTitle().blit(LabelRespirator, (0,350))
            
        textBoxO.draw(menuScreen.returnTitle())
        textBox1.draw(menuScreen.returnTitle())
        
        menuScreen.returnTitle().blit(labelSee, (248,150))
   
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,550,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,550,80,40))
        labelSim = myfont2.render("Healthy: ",1,(0,255,0))
        simScreen.returnTitle().blit(labelSim,(332,502))
        labelSim = myfont2.render("Infected: ",1,(255,0,0))
        simScreen.returnTitle().blit(labelSim,(336,552))
        labelSim = myfont2.render("Dead: ",1,(0,0,0))
        simScreen.returnTitle().blit(labelSim,(430,552))
        labelSim = myfont2.render("Dormant: ",1,(70,70,70))
        simScreen.returnTitle().blit(labelSim,(422,502))
        
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129

        if startButtonSim:
            respirators = int(textBoxRespirator.returnValue())
            #POCETAK
            threads = []
<<<<<<< HEAD
            numinfected += 1
            inf = threading.Thread(target=spawninfected)   
            inf.start()
            threads.append(inf)

            for _ in range(n):
                numhealthy += 1
=======
            f = threading.Thread(target=spawnfirst)
            numdormant += 1

            labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
            simScreen.returnTitle().blit(labelInfected,(355,570))
            labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
            pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,20))
            simScreen.returnTitle().blit(labelDormant,(435,520))

            f.start()
            threads.append(f)
            for _ in range(n - 1):
                while stopClick:
                    time.sleep(odmeraj)
                
                numhealthy += 1
                labelHealthy = myfont2.render(str(numhealthy),1,(0,255,0)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (340,520,50,20))
                simScreen.returnTitle().blit(labelHealthy,(340,520))

                labelDead = myfont2.render(str(numdead),1,(0,0,0)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,570,50,20))
                simScreen.returnTitle().blit(labelDead,(435, 570))
                
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
                t = threading.Thread(target=spawn)   
                t.start()
                threads.append(t)

            for thread in threads:
                thread.join()
<<<<<<< HEAD
=======
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(320,550,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,500,80,40))
        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(410,550,80,40))
        labelSim = myfont2.render("Alive: ",1,(0,255,0))
        simScreen.returnTitle().blit(labelSim,(343,502))
        labelSim = myfont2.render("Infected: ",1,(255,0,0))
        simScreen.returnTitle().blit(labelSim,(336,552))
        labelSim = myfont2.render("Dead: ",1,(0,0,0))
        simScreen.returnTitle().blit(labelSim,(430,552))
        labelSim = myfont2.render("Dormant: ",1,(70,70,70))
        simScreen.returnTitle().blit(labelSim,(422,502))
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
        
=======
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129

        if startButtonSim:
            for event in pg.event.get():
                stopClick = False
                threads = []
                numinfected += 1
                labelInfected = myfont2.render(str(numinfected),1,(255,20,0)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255),(337,570,50,20))
                simScreen.returnTitle().blit(labelInfected,(355,570))

                labelDormant = myfont2.render(str(numdormant),1,(70,70,70)) 
                pg.draw.rect(simScreen.returnTitle(),(0,0,255), (435,520,30,15))
                simScreen.returnTitle().blit(labelDormant,(435,520))

                inf = threading.Thread(target=spawninfected)
                inf.start()
                threads.append(inf)
                #start = time.perf_counter()
                for _ in range(n):
                    numhealthy += 1
                    if stopButtonSim:
                        #sleepCitizen(odmeraj)
                        pg.draw.rect(simScreen.returnTitle(),(0,0,255),(210,250,100,100))
                    #st = numhealthy.__str__()
                    labelHelathy = myfont2.render(str(numhealthy),1,(0,255,0)) 
                    pg.draw.rect(simScreen.returnTitle(),(0,0,255), (340,520,50,15))
                    simScreen.returnTitle().blit(labelHelathy,(340,520))
                    
                    
                    t = threading.Thread(target=spawn)   
                    t.start()
                    threads.append(t)

                for thread in threads:
                    thread.join()
                #print(numinfected)
            
            """if stopButtonSim:
                win = menuScreen.makeDisplay()
                simScreen.endCurrent()"""
            
                if event.type == pg.QUIT:
                    win = menuScreen.makeDisplay()
                    simScreen.endCurrent()
        
    
    Click = False
    
<<<<<<< HEAD
        #event
=======

>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
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
                        

<<<<<<< HEAD
<<<<<<< HEAD
    pg.display.update()
=======
    pg.display.update()
    #mainClock.tick(20)
>>>>>>> f942762401beaa9973464376db4637bc688a5b68
=======
    pg.display.update()
>>>>>>> dadc61726144af53a7a78caf2f0dc20d760ce129
