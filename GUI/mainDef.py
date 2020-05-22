import pygame as pg
import math
import random
from TextBox_class import *
from ScreenClass import *
from ButtonClass import *
#from simulation1 import *
vec = pg.math.Vector2

pg.init()



def main():

    menuScreen = Screen("menu screen",600,400)
    tempScreen = Screen("temp screen",400,300)
    simScreen = Screen("Simulator",750,790)
    mainClock = pg.time.Clock()

    myfont = pg.font.SysFont("Arial", 20)
    label = myfont.render(" Enter a number of people =>",1, (255,255,0))
    labelReady = Button(220,210,70,50,(255,0,0),"READY!")
    labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
    labelCity = myfont.render(" Chose a real city =>",1, (255,255,0))
    dropButton = Button(199,156,80,15,(40,40,40),"                               ")
    myfont2 = pg.font.SysFont("Arial", 17)
    labelSee = myfont2.render(" click to see",1, (0,0,0))

    win = menuScreen.makeDisplay()
    mapa = pg.image.load("mapCovid.png")
    textBoxes = []
    textBoxO = TextBox(218,29,100,50,4)
    textBox1 = TextBox(700,700,100,50,4)
    textBoxes.append(textBoxO)
    textBoxes.append(textBox1)
    running = True
   
    while running:
        menuScreen.screenUpdate()
        tempScreen.screenUpdate()
        mousePos = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()

        tempDropButton = dropButton.isOver(mousePos, mouseClick)
        if tempDropButton:
            b = 170
            i = 0
            for i in range(5):
                b += 30
                textBox1 = TextBox(188,100,100,50,4)
                textBoxes.append(textBox1)
                textBox1.draw(menuScreen.returnTitle())
                if i == 0:
                    city = myfont.render(" novi sad",1,(255,255,0))
                if i == 1:
                    city = myfont.render(" new york",1,(255,255,0))
                if i == 2:
                    city = myfont.render("  milano",1,(255,255,0))
                if i == 3:
                    city = myfont.render("  valjevo",1,(255,255,0))
                if i == 4:
                    city = myfont.render("   svet",1,(255,255,0))
                menuScreen.returnTitle().blit(city,(206,b-30))

        if menuScreen.checkUpdate():
            tempScreenButton = labelReady.isOver(mousePos,mouseClick)
            if not tempDropButton:
                labelReady.drawButton(menuScreen.returnTitle(),True)
            menuScreen.returnTitle().blit(label,(0,40))
            menuScreen.returnTitle().blit(labelCity, (0,130))
            
            textBoxO.draw(menuScreen.returnTitle())
            textBox1.draw(menuScreen.returnTitle())
            dropButton.drawButton(menuScreen.returnTitle())
            menuScreen.returnTitle().blit(labelSee, (200,150))
   
            if tempScreenButton:
                simScreen.makeDisplay()
                simulationPlay(textBoxO,simScreen)
                menuScreen.endCurrent()

        elif tempScreen.checkUpdate():
            menuScreen.returnTitle().blit(mapa, (0,0))
            returnButton = labelReturn.isOver(mousePos,mouseClick)
            labelReturn.drawButton(tempScreen.returnTitle())

            if returnButton:
                win = menuScreen.makeDisplay()
                tempScreen.endCurrent()
        elif simScreen.checkUpdate:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    win = menuScreen.makeDisplay()
                    simScreen.endCurrent()
        
        """if labelReady.collidepoint((mouseClick)):
            if Click:
                simulationPlay()"""
        
        """pg.draw.rect(menuScreen.returnTitle(), (255,0,0), labelReady)"""
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

main()
