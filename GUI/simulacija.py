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

    def setdestination(self):
        self.destx = random.randint(rangelow, rangehigh)
        self.desty = random.randint(rangelow, rangehigh)
        while screensurf.get_at([self.destx, self.desty]) != black:
            self.destx = random.randint(rangelow, rangehigh)
            self.desty = random.randint(rangelow, rangehigh)

    def goto(self):
        screensurf = pg.display.get_surface()
        pg.draw.rect(window, self.color, (self.x, self.y, humansize, humansize))
        pg.display.update()
        i = 1
        strana = ""
        time.sleep(odmeraj)
        while i < duzina:
            if self.x + i + 2 < duzina and screensurf.get_at([self.x + i, self.y]) != black and screensurf.get_at([self.x + i + 1, self.y]) != black and screensurf.get_at([self.x + i + 2, self.y]) != black and (screensurf.get_at([self.x + i + 1, self.y + 1]) != black or screensurf.get_at([self.x + i + 1, self.y - 1]) != black):
                strana = "desno"
                break
            elif self.x > i + 2 and screensurf.get_at([self.x - i, self.y]) != black and screensurf.get_at([self.x - i - 1, self.y]) != black and screensurf.get_at([self.x - i - 2, self.y]) != black and (screensurf.get_at([self.x - i - 1, self.y + 1]) != black or screensurf.get_at([self.x - i - 1, self.y - 1]) != black):
                strana = "levo"
                break
            elif self.y + i + 2 < duzina and screensurf.get_at([self.x, self.y + i]) != black and screensurf.get_at([self.x, self.y + i + 1]) != black and screensurf.get_at([self.x, self.y + i + 2]) != black and (screensurf.get_at([self.x + 1, self.y + i + 1]) != black or screensurf.get_at([self.x - 1, self.y + i + 1]) != black):
                strana = "dole"
                break
            elif self.y > i + 2 and screensurf.get_at([self.x, self.y - i]) != black and screensurf.get_at([self.x, self.y - i - 1]) != black and screensurf.get_at([self.x, self.y - i - 2]) != black and (screensurf.get_at([self.x + 1, self.y - i - 1]) != black or screensurf.get_at([self.x - 1, self.y - i - 1]) != black):
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

        elif strana == "levo":
            i = self.x - i
            while self.x > i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x - 1, self.y, humansize, humansize))
                pg.display.update()
                self.x -= 1
                time.sleep(odmeraj)
        elif strana == "dole":
            i += self.y
            while self.y < i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x, self.y + 1, humansize, humansize))
                pg.display.update()
                self.y += 1
                time.sleep(odmeraj)
        else:
            i = self.y - i
            while self.y > i:
                pg.draw.rect(window, black, (self.x, self.y, humansize, humansize))
                pg.draw.rect(window, self.color, (self.x, self.y - 1, humansize, humansize))
                pg.display.update()
                self.y -= 1
                time.sleep(odmeraj)
        pg.draw.rect(window, self.color, (self.x, self.y, humansize, humansize))
        pg.display.update()


    def __init__(self):
        self.color = healthycolor
        self.x = random.randint(rangelow, rangehigh)
        self.y = random.randint(rangelow, rangehigh)
        while screensurf.get_at([self.x, self.y]) != black:
            self.x = random.randint(rangelow, rangehigh)
            self.y = random.randint(rangelow, rangehigh)
        self.setdestination()
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
    screensurf = pg.display.get_surface()

    if __name__ == '__main__':
        threads = []
        #start = time.perf_counter()
        for _ in range(10000):
            t = threading.Thread(target=spawn)
            t.start()
            threads.append(t)
        

        for thread in threads:
            thread.join()
        