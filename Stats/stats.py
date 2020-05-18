#uvoz potrebnih biblioteka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as rand

#cini plotovanje interaktivnim
plt.ion()

#deklaracija i pocetna definicija pomocnih promenljivih
time = [0]
rez = [0]
mrtvi = [0]
zivi = [0]
izleceni = [0]
color = ['red','black','blue','green']
label = ['Zarazeni','Mrtvi','Izleceni','Zivi']

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
    global rez
    global mrtvi
    global zivi
    global izleceni
    zivi[vreme] = population - mrtvi[vreme] - izleceni[vreme] - rez[vreme]
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    plt.stackplot(time,rez,mrtvi,izleceni,zivi, labels = label, colors = color)
    plt.legend(loc = 'upper left')
    plt.show()
    plt.pause(0.001)
    if vreme != 299:
        plt.clf()
    time.append(vreme+1)
    rez.append(infected)
    mrtvi.append(dead)
    izleceni.append(healed)
    zivi.append(0)

#Uvoz statistike iz excel fajlova
df = pd.read_excel('Stats/Real stats/Stats Serbia.xlsx')
ns_infected = np.array(df['Novi Sad']).cumsum()
serbia_days = np.array(df['Dan'])
valjevo_infected = np.array(df['Valjevo']).cumsum()
"""
funkcija za plotovanje samo inficiranih za parametre prima broj inficiranih, dane, "vreme", tj. iteraciju u petlji i broj zapisanih dana
ova funkcija je vama nebitna koristi se samo da se skrati kod kasnije za prikaz realnog sveta
"""
def show_infected_plot(infected,days,vreme,broj_pod):
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    plt.plot(days[0:vreme],infected[0:vreme],color = 'red')
    plt.fill_between(days[0:vreme],infected[0:vreme],color = 'red')
    plt.show()
    plt.pause(0.001)
    if vreme != broj_pod - 1:
        plt.clf()

#funkcija za plotovanje za novi sad
def show_ns(vreme):
    show_infected_plot(ns_infected,serbia_days,vreme,55)

#funkcija za plotovanje za valjevo
def show_valjevo(vreme):
    show_infected_plot(valjevo_infected,serbia_days,vreme,55)

"""
#test funkcije za plotovanje za novi sad    
for i in range(55):
    show_ns(i)

nesto = input()

#test funkcije za plotovanje za valjevo
for i in range(55):
    show_valjevo(i)

nesto = input()
"""

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