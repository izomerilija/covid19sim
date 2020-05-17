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
mrtvi = [0]
zivi = [0]
izleceni = [0]
color = ['red','black','blue','green']

"""
funkcija za plotovanje
1. parametar - trenutan broj zarazenih
2. parametar - trenutan broj umrlih
3. parametar - trenutan broj ozdravljenih
4. parametar - iteracija u petlji, "vreme"
5. parametar - ukupno jedinki
"""
def show_plot(infected,dead,healed,vreme,population):
    global time
    global pom
    global rez
    global mrtvi
    global zivi
    global izleceni
    zivi[vreme] = population - mrtvi[vreme] - izleceni[vreme] - rez[vreme]
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    plt.stackplot(time,rez,mrtvi,izleceni,zivi, colors = color)
    plt.show()
    plt.pause(0.001)
    if vreme != 299:
        plt.clf()
    pom += 1
    time.append(pom)
    rez.append(infected)
    mrtvi.append(dead)
    izleceni.append(healed)
    zivi.append(0)

"""
#testiranje funkcije
zbir = 0
pop = 500
d = 0
h = 0

for i in range(300):
    b = rand(1,10)
    if i <= 50 or i >= 250:
        if b > 8:
            a = rand(1,5)
        else:
            a = rand(1,11)
    else:
        if b > 3:
            a = rand(1,3)
        else:
            a = rand(1,8)

    zbir += a

    if zbir < 0:
        zbir = 0
    if zbir + d + h > pop:
        zbir = pop - d - h
        h = pop - zbir - d
        d = pop - zbir - h
    
    if zbir > 100:
        d += rand(1,3)
        zbir -= d
        h += rand(1,7)
        zbir -= h

    show_plot(zbir,d,h,i,pop)

#ovo postoji da ne bi odmah nakon zavrsetka plotovanja izaslo
nesto = input()
"""