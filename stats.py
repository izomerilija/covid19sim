#uvoz potrebnih biblioteka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as rand

#cini plotovanje interaktivnim
plt.ion()

#deklaracija i pocetna definicija pomocnih promenljivih
time = [0]
pom = 0
rez = [0]

#funkcija za plotovanje, prvi parametar je broj trenutno zarazenih, drugi je "vreme", tj. trenutna iteracija u petlji
def show_plot(infected,vreme):
    global time
    global pom
    global rez
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    plt.plot(time,rez, color = 'red')
    plt.fill_between(time,rez,0,color = 'red')
    plt.show()
    plt.pause(0.001)
    if vreme != 299:
        plt.clf()
    pom += 1
    time.append(pom)
    rez.append(infected)

#testiranje funkcije
"""
zbir = 0

for i in range(300):
    b = rand(1,10)
    if i <= 50 or i >= 250:
        if b > 8:
            a = rand(1,4)
        else:
            a = rand(1,10)
    else:
        if b > 3:
            a = rand(1,3)
        else:
            a = rand(1,8)

    zbir += a

    if i > 30 and i < 100:
        zbir -= rand(1,2)
    elif i >= 100 and i < 250:
        zbir -= rand(1,5)
    elif i >= 250:
        zbir -= rand(1,7)

    if zbir < 0:
        zbir = 0 

    show_plot(zbir,i)

#ovo postoji da ne bi odmah nakon zavrsetka plotovanja izaslo
nesto = input()
"""