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

    mainClock = pg.time.Clock()

    myfont = pg.font.SysFont("Arial", 20)
    label = myfont.render(" Unesite broj osoba =>",1, (255,255,0))
    labelReady = Button(150,170,70,50,(255,0,0),"READY!")
    labelReturn = Button(150,170,70,50,(255,255,0),"RETURN!")
    dropButton = Button(350,70,170,25,(40,40,40),"CHOSE A REAL CITY")

    win = menuScreen.makeDisplay()

    textBoxes = []
    textBoxO = TextBox(168,29,100,50,6)
    textBox1 = TextBox(390,100,100,50,3)
    textBoxes.append(textBoxO)
    textBoxes.append(textBox1)
    running = True
    

    while running:
        menuScreen.screenUpdate()
        tempScreen.screenUpdate()
        mousePos = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()

        dropButton.drawButton(menuScreen.returnTitle())
        tempDropButton = dropButton.isOver(mousePos, mouseClick)
        
        
        if tempDropButton:
            b = 110
            i = 0
            for i in range(5):
                b += 30
                textBox1 = TextBox(390,20,100,50,4)
                textBoxes.append(textBox1)
                textBox1.draw(menuScreen.returnTitle())
                if i == 0:
                    city = myfont.render("novi sad",1,(255,255,0))
                if i == 1:
                    city = myfont.render("valjevo",1,(255,255,0))
                if i == 2:
                    city = myfont.render("wuhan",1,(255,255,0))
                if i == 3:
                    city = myfont.render("new york",1,(255,255,0))
                if i == 4:
                    city = myfont.render("milano",1,(255,255,0))
                menuScreen.returnTitle().blit(city,(400,b-30))

        
        
        #keys = pg.key.get_pressed()

        if menuScreen.checkUpdate():
            tempScreenButton = labelReady.isOver(mousePos,mouseClick)
            labelReady.drawButton(menuScreen.returnTitle(),True)
            menuScreen.returnTitle().blit(label,(0,40))
            textBoxO.draw(menuScreen.returnTitle())
            textBox1.draw(menuScreen.returnTitle())
            if tempScreenButton:
                win = tempScreen.makeDisplay()
                menuScreen.endCurrent()

        elif tempScreen.checkUpdate():
            returnButton = labelReturn.isOver(mousePos,mouseClick)
            labelReturn.drawButton(tempScreen.returnTitle())

            if returnButton:
                win = menuScreen.makeDisplay()
                tempScreen.endCurrent()
        
        """if labelReady.collidepoint((mouseClick)):
            if Click:
                simulationPlay()"""
        
        """pg.draw.rect(menuScreen.returnTitle(), (255,0,0), labelReady)"""
        #Click = False
            #event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


            if event.type == pg.MOUSEBUTTONDOWN:
                for box in textBoxes:
                    box.checkClick(pg.mouse.get_pos())
                if event.button == 1:
                    Click = True    

            if event.type == pg.KEYDOWN:
                for box in textBoxes:
                    if box.active:
                        box.addText(event.key)
                        
            #draw
        
        
        
        #menuScreen.blit(labelReady,(151,179))
        
        
        

        pg.display.update()
        mainClock.tick(60)