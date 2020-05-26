import pygame as pg
import math
import random
from TextBox_class import *
from ScreenClass import *
from ButtonClass import *
#from simulation1 import *
vec = pg.math.Vector2
import time
import multiprocessing
import threading

pg.init()



menuScreen = Screen("COVID 19",560,400)
tempScreen = Screen("temp screen",400,300)
simScreen = Screen("Simulator  of COVID 19",500,600,(0,0,0))
mainClock = pg.time.Clock()

myfont = pg.font.SysFont("Arial", 20)
label = myfont.render("    Enter the number of people =>",1, (255,255,0))
labelReady = Button(405,170,120,70,(255,0,0),"READY!")
labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
labelCity = myfont.render("          Choose a real city =>",1, (255,255,0))
dropButton = Button(248,153,80,15,(40,40,40),"                               ")
myfont2 = pg.font.SysFont("Arial", 17)
labelSee = myfont2.render(" click to see",1, (0,0,0))
LabelGloves = myfont.render("     Percent of wear gloves =>",1,(255,255,0))
LabelMasks = myfont.render("     Percent of wear masks => ",1,(255,255,0))
LabelRespirator = myfont.render(" Enter the number of respirators =>",1,(255,255,0))

startButton = Button(0,500,150,50,(0,0,255),"START",(0,0,0))
stopButton = Button(160,500,150,50,(0,0,255),"STOP",(0,0,0))

humansize = 1
odmeraj = 0.1
duzina = 500
rangelow = 3
rangehigh = duzina - rangelow

mapa = pg.image.load('covid19\\NEWMAP.png')  

black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
healthycolor = (0, 255, 170)

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
icon = pg.image.load('covid19\\iconCorona.png')
pg.display.set_icon(icon)
coronaImage = pg.image.load("covid19\\corona2.jpg")
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

        if startButtonSim:
            threads = []
            #start = time.perf_counter()
            for _ in range(n):
                
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
        #event
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
    mainClock.tick(60)
