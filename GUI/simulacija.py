import pygame as pg
import time
import random
import multiprocessing
import threading

pg.init()

humansize = 1
odmeraj = 0.1
duzina = 500
rangelow = 3
rangehigh = duzina - rangelow


black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
healthycolor = (0, 255, 170)

class Citizen:

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
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x += 1
                
                elif availablesides[r] == "dole":
                    while mapa.get_at([self.x - 4, self.y]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.y += 1

                else:
                    while mapa.get_at([self.x - 4, self.y]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
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
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x -= 1
                
                elif availablesides[r] == "dole":
                    while mapa.get_at([self.x + 4, self.y]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.y += 1

                else:
                    while mapa.get_at([self.x + 4, self.y]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.y -= 1
                
                self.randompath(availablesides[r])
                return
            
            else:
                self.randompath("desno")
                return

            
            
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
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.y += 1

                elif availablesides[r] == "desno":
                    while mapa.get_at([self.x, self.y - 4]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x += 1

                else:
                    while mapa.get_at([self.x, self.y - 4]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x -= 1
                
                self.randompath(availablesides[r])
                return
            
            else:
                self.randompath("gore")
                return

            
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
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.y -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.y -= 1

                elif availablesides[r] == "desno":
                    while mapa.get_at([self.x, self.y + 4]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x += 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x += 1

                else:
                    while mapa.get_at([self.x, self.y + 4]) == white:
                        pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                        pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                        pg.display.update()
                        time.sleep(odmeraj)
                        self.x -= 1
                    pg.draw.rect(window, white, (self.x, self.y, humansize, humansize))
                    pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                    pg.display.update()
                    time.sleep(odmeraj)
                    self.x -= 1
                
                self.randompath(availablesides[r])
                return
            
            else:
                self.randompath("dole")
                return


    def goto(self):
        pg.draw.rect(window, self.color, (self.x, self.y, humansize, humansize))
        pg.display.update()
        i = 1
        strana = ""
        time.sleep(odmeraj)
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
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x + 1, self.y, humansize, humansize))
                pg.display.update()
                self.x += 1
                time.sleep(odmeraj)
            self.randompath("desno")

        elif strana == "levo":
            i = self.x - i
            while self.x > i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                pg.display.update()
                self.x -= 1
                time.sleep(odmeraj)
            self.randompath("levo")

        elif strana == "dole":
            i += self.y
            while self.y < i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                pg.display.update()
                self.y += 1
                time.sleep(odmeraj)
            self.randompath("dole")

        else:
            i = self.y - i
            while self.y > i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                pg.display.update()
                self.y -= 1
                time.sleep(odmeraj)
            self.randompath("gore")
        


    def __init__(self):
        self.color = healthycolor
        self.x = random.randint(rangelow, rangehigh)
        self.y = random.randint(rangelow, rangehigh)
        while mapa.get_at([self.x, self.y]) != black:
            self.x = random.randint(rangelow, rangehigh)
            self.y = random.randint(rangelow, rangehigh)
        #self.setdestination()
        self.goto()

def spawn():
    c = Citizen()


window = pg.display.set_mode((duzina,duzina))
mapa = pg.image.load('proj\\mapa.png')
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill((0, 0, 0))
    window.blit(mapa, (0, 0))
    pg.display.update()

    if __name__ == '__main__':
        threads = []
        #start = time.perf_counter()
        for _ in range(1000):
            t = threading.Thread(target=spawn)
            t.start()
            threads.append(t)
    

        for thread in threads:
            thread.join()