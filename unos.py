import pygame as pg
import math
import random
from TextBox_class import *
#from simulation1 import *
vec = pg.math.Vector2

pg.init()

screen = pg.display.set_mode((400,300))
mainClock = pg.time.Clock()

myfont = pg.font.SysFont("Arial", 20)
label = myfont.render(" Unesite broj osoba =>",1, (255,255,0))
labelReady = myfont.render(" READY",1, (0,0,0))



textBoxes = []
textBoxO = TextBox(168,29,100,50,6)
textBoxes.append(textBoxO)


def simulationPlay():
    import pygame
    import math
    import random

    pygame.init()

    screen = pygame.display.set_mode((750, 790))
    clock = pygame.time.Clock()
    pygame.display.set_caption('simulator')
    font = pygame.font.SysFont('Arial', 20)


    alive = 0
    infected = 0
    dormant = 0
    immune = 0

    A = []
    on = 0
    k = 0
    B = []
    empty = 1
    running = True

    # buttons & grid

    for y in range(150):
        temp = []
        temper = []
        

        for x in range(150):    
            temp.append(0)
            temper.append(0)

            rect = pygame.Rect(x*5, y*5, 5, 5) #grid
            pygame.draw.rect(screen, (100, 100, 100), rect)
        A.append(temp)
        B.append(temper)


    rect = pygame.Rect(450, 750, 771, 771)
    pygame.draw.rect(screen, (255, 255, 0), rect)
    textsurface = font.render("Alive: ", True, (0, 0, 0))
    screen.blit(textsurface, (455, 750))
    textsurface = font.render("Immune: ", True, (0, 0, 0))
    screen.blit(textsurface, (575, 770))
    textsurface = font.render("Dormant: ", True, (0, 0, 0))
    screen.blit(textsurface, (575, 750))
    textsurface = font.render("Infected: ", True, (0, 0, 0))
    screen.blit(textsurface, (455, 770))


    rect = pygame.Rect(0, 771, 225, 20)
    pygame.draw.rect(screen, (253, 106, 2), rect)
    textsurface = font.render("Reset", True, (0, 0, 0))
    screen.blit(textsurface, (93, 769))

    rect = pygame.Rect(226, 771, 225, 20)
    pygame.draw.rect(screen, (50, 50, 255), rect)
    textsurface = font.render("Save/Load", True, (0, 0, 0))
    screen.blit(textsurface, (300, 769))

    rect = pygame.Rect(0, 750, 225, 20)
    pygame.draw.rect(screen, (30, 255, 30), rect)
    textsurface = font.render("Start", True, (0, 0, 0))
    screen.blit(textsurface, (95, 749))

    rect = pygame.Rect(226, 750, 225, 20)
    pygame.draw.rect(screen, (255, 30, 30), rect)
    textsurface = font.render("Stop", True, (0, 0, 0))
    screen.blit(textsurface, (320, 749))

    pygame.display.flip()



    class Osoba:
        def __init__(self, x, y, age, id):
            self.x = x
            self.y = y
            self.age = age
            self.status = 1
            self.dtl = 10000
            infec = random.randint(0, 100)

            rect = pygame.Rect(x * 5, y * 5, 4, 4)
            pygame.draw.rect(screen, (14, 77, 200), rect)
            A[x][y] = 1
            B[x][y] = id

            if infec <= 10:
                self.status = 3
                self.dtl = 20
                A[x][y] = 3
                pygame.draw.rect(screen, (229, 83, 0), rect)

            pygame.display.flip()
        def move(self, dir):
            if self.status > 0:
                x = self.x
                y = self.y
                if dir == 0 and A[(x + 1) % 150][y] == 0:
                    A[(x + 1) % 150][y] = A[x][y]
                    A[x][y] = 0
                    B[(x + 1) % 150][y] = B[x][y]
                    B[x][y] = -1

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)
                    pygame.draw.rect(screen, (100, 100, 100), rect)
                    x = (x + 1) % 150

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)

                    if A[x][y] == 1:
                        pygame.draw.rect(screen, (14, 77, 200), rect)

                    elif A[x][y] == 2:
                        pygame.draw.rect(screen, (178, 34, 34), rect)

                    elif A[x][y] == 3:
                        pygame.draw.rect(screen, (229, 83, 0), rect)

                    elif A[x][y] == 4:
                        pygame.draw.rect(screen, (0, 175, 0), rect)

                    self.x = x
                    self.y = y

                elif dir == 1 and A[(x - 1) % 150][y] == 0:
                    A[(x - 1) % 150][y] = A[x][y]
                    A[x][y] = 0
                    B[(x - 1) % 150][y] = B[x][y]
                    B[x][y] = -1

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)
                    pygame.draw.rect(screen, (100, 100, 100), rect)
                    x = (x - 1) % 150

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)

                    if A[x][y] == 1:
                        pygame.draw.rect(screen, (14, 77, 200), rect)

                    elif A[x][y] == 2:
                        pygame.draw.rect(screen, (178, 34, 34), rect)

                    elif A[x][y] == 3:
                        pygame.draw.rect(screen, (229, 83, 0), rect)

                    elif A[x][y] == 4:
                        pygame.draw.rect(screen, (0, 175, 0), rect)

                    self.x = x
                    self.y = y

                elif dir == 2 and A[x][(y+1)%150] == 0:
                    A[x][(y+1)%150] = A[x][y]
                    A[x][y] = 0
                    B[x][(y+1)%150] = B[x][y]
                    B[x][y] = -1

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)
                    pygame.draw.rect(screen, (100, 100, 100), rect)
                    y = (y + 1) % 150

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)

                    if A[x][y] == 1:
                        pygame.draw.rect(screen, (14, 77, 200), rect)

                    elif A[x][y] == 2:
                        pygame.draw.rect(screen, (178, 34, 34), rect)

                    elif A[x][y] == 3:
                        pygame.draw.rect(screen, (229, 83, 0), rect)

                    elif A[x][y] == 4:
                        pygame.draw.rect(screen, (0, 175, 0), rect)

                    self.x = x
                    self.y = y

                elif dir == 3 and A[x][(y-1)%150] == 0:
                    A[x][(y-1)%150] = A[x][y]
                    A[x][y] = 0
                    B[x][(y-1) % 150] = B[x][y]
                    B[x][y] = -1

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)
                    pygame.draw.rect(screen, (100, 100, 100), rect)
                    y = (y - 1) % 150

                    rect = pygame.Rect(x * 5, y * 5, 4, 4)

                    if A[x][y] == 1:
                        pygame.draw.rect(screen, (14, 77, 200), rect)

                    elif A[x][y] == 2:
                        pygame.draw.rect(screen, (178, 34, 34), rect)

                    elif A[x][y] == 3:
                        pygame.draw.rect(screen, (229, 83, 0), rect)

                    elif A[x][y] == 4:
                        pygame.draw.rect(screen, (0, 175, 0), rect)

                    self.x = x
                    self.y = y

        def infect(self, radius, infec):
            x = int(self.x - radius) % 150
            y = int(self.y - radius) % 150
            for j in range(y, y + radius * 2):
                for i in range(x, x + radius):
                    i = i % 150
                    j = j % 150
                    id = B[i][j]
                    if O[id].status == 1 and x != self.x and y != self.y:
                        tempint1 = random.randint(0, 100)
                        if tempint1 <= (infec / 2 + ((101 - O[id].age) / 100) * infec):
                            if O[id].dtl > 20:
                                O[id].dtl = 20
                                O[id].status = 3
                                A[O[id].x][O[id].y] = 3
                                rect = pygame.Rect(O[id].x * 5, O[id].y * 5, 4, 4)
                                pygame.draw.rect(screen, (229, 83, 0), rect)

        def heal(self, health):
            tempint1 = random.randint(0, 100)
            if tempint1 <= (health/2 + ((101 - O[i].age) / 100) * health):
                O[i].status = 4
                A[O[i].x][O[i].y] = 4
                O[i].dtl = 1000
                rect = pygame.Rect(O[i].x * 5, O[i].y * 5, 4, 4)
                pygame.draw.rect(screen, (0, 175, 0), rect)



    random.seed()


    n = 0
    n2 = 0
    O = [None] * 22500


    n = int(textBoxO.returnValue())  #broj osoba

    if n >= 22500:
        for y in range(150):
            for x in range(150):
                tempint3 = random.randint(0, 100)
                O[y150+x] = Osoba(x, y, tempint3, y150+x)
    else:
        n2 = n - 1
        inf = 0
        while n != 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pygame.display.flip()

            tempint1 = random.randint(0, 149)
            tempint2 = random.randint(0, 149)
            tempint3 = random.randint(0, 100)

            if A[tempint1][tempint2] == 0:
                n -= 1
                O[n2-n] = Osoba(tempint1, tempint2, tempint3, n2-n)
                if O[n2-n].status == 3:
                    inf = inf + 1

            rect = pygame.Rect(450, 750, 771, 771)
            pygame.draw.rect(screen, (255, 255, 0), rect)
            textsurface = font.render("Alive: ", True, (0, 0, 0))
            screen.blit(textsurface, (455, 750))
            textsurface = font.render(str(n2+1), True, (0, 0, 0))
            screen.blit(textsurface, (500, 750))
            textsurface = font.render("Infected: ", True, (0, 0, 0))
            screen.blit(textsurface, (455, 770))
            textsurface = font.render(str(inf), True, (0, 0, 0))
        


    while None in O:
        O.remove(None)

    n = len(O)

    for i in range(n):
        if O[i].status > 0:
            alive = alive + 1


    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                screen = pg.display.set_mode((400,300))
                mainClock = pg.time.Clock()

                myfont = pg.font.SysFont("Arial", 20)
                label = myfont.render(" Unesite broj osoba =>",1, (255,255,0))
                labelReady = myfont.render(" READY",1, (0,0,0))
            pygame.display.flip()

        if True:
            on = 1

            while on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        screen = pg.display.set_mode((400,300))
                        mainClock = pg.time.Clock()

                        myfont = pg.font.SysFont("Arial", 20)
                        label = myfont.render(" Unesite broj osoba =>",1, (255,255,0))
                        labelReady = myfont.render(" READY",1, (0,0,0))
                        on = 0

                clock.tick(10)

                """alive = 0
                infected = 0
                dormant = 0
                immune = 0"""

                for i in range(n):
                    tempint1 = random.randint(0, 100)
                    if tempint1 <= 50:
                        tempint1 = int(tempint1 / 12.5)
                        O[i].move(tempint1)

                    if O[i].status == 2:
                        O[i].heal(3)
                        if O[i].status == 4:
                            infected = infected - 1
                        if O[i].status == 2:
                            O[i].infect(5, 10)
                            if O[i].dtl == 0:
                                O[i].status = -1
                                alive = alive - 1
                                infected = infected - 1
                                if infected == 0:
                                    on = 0
                                rect = pygame.Rect(O[i].x * 5, O[i].y * 5, 4, 4)
                                pygame.draw.rect(screen, (0, 0, 0), rect)
                            else:
                                O[i].dtl = O[i].dtl - 1

                    if O[i].status == 3:
                        O[i].dtl = O[i].dtl - 1
                        if O[i].dtl == 13:
                            O[i].status = 2
                            infected = infected + 1
                            dormant = dormant - 1
                            A[O[i].x][O[i].y] = 2
                            rect = pygame.Rect(O[i].x * 5, O[i].y * 5, 4, 4)
                            pygame.draw.rect(screen, (178, 34, 34), rect)

                    if O[i].dtl == 19:
                        dormant = dormant + 1

                    if O[i].dtl == 1000:
                        immune = immune + 1
                        O[i].dtl = O[i].dtl + 1

                rect = pygame.Rect(450, 750, 771, 771)
                pygame.draw.rect(screen, (255, 255, 0), rect)
                textsurface = font.render("Alive: ", True, (0, 0, 0))
                screen.blit(textsurface, (455, 750))
                textsurface = font.render("Immune: ", True, (0, 0, 0))
                screen.blit(textsurface, (575, 770))
                textsurface = font.render("Dormant: ", True, (0, 0, 0))
                screen.blit(textsurface, (575, 750))
                textsurface = font.render("Infected: ", True, (0, 0, 0))
                screen.blit(textsurface, (455, 770))
                textsurface = font.render(str(alive), True, (0, 0, 0))
                screen.blit(textsurface, (525, 750))
                textsurface = font.render(str(immune), True, (0, 0, 0))
                screen.blit(textsurface, (650, 770))
                textsurface = font.render(str(dormant), True, (0, 0, 0))
                screen.blit(textsurface, (650, 750))
                textsurface = font.render(str(infected), True, (0, 0, 0))
                screen.blit(textsurface, (525, 770))
                pygame.display.flip()



def main():
    running = True
    Click = False   
    while running:
        screen.fill((54,54,54)) 
        mx,my = pg.mouse.get_pos()
        simulationButton = pg.Rect(150,170,70,50)

        if simulationButton.collidepoint((mx,my)):
            if Click:
                simulationPlay()
        
        pg.draw.rect(screen, (255,0,0), simulationButton)
        Click = False 
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
        
        
        screen.blit(label,(0,40))
        screen.blit(labelReady,(151,179))
        
        
        for box in textBoxes:
            box.draw(screen)

        pg.display.update()
        mainClock.tick(60)

main()