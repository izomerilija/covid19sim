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
    plt.figure(1)
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
df2 = pd.read_csv('Stats/Real stats/Stats New York.csv')
ny_infected = np.array(df2['Cases'],dtype=int).cumsum()
ny_days = np.array(df2['DATE_OF_INTEREST'],dtype=str)
df3 = pd.read_excel('Stats/Real stats/Stats Milano.xlsx')
milano_infected = np.array(df3['Milano']).cumsum()
milano_days = np.array(df3['Dan'])
df4 = pd.read_excel('Stats/Real stats/Stats world.xlsx')
world_infected = np.array(df4['Broj']).cumsum()
world_days = np.array(df4['Dan'])

"""
funkcija za plotovanje samo inficiranih za parametre prima broj inficiranih, dane, "vreme", tj. iteraciju u petlji i broj zapisanih dana
ova funkcija je vama nebitna koristi se samo da se skrati kod kasnije za prikaz realnog sveta
"""
def show_infected_plot(infected,days,vreme,broj_pod):
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.plot(days[0:vreme],infected[0:vreme],color = 'red')
    plt.fill_between(days[0:vreme],infected[0:vreme],color = 'red')
    plt.show()

#funkcija za plotovanje za novi sad
def show_ns(vreme):
    plt.figure(2)
    plt.title("Odnos zarazenih vremenom - Novi Sad")
    show_infected_plot(ns_infected,serbia_days,vreme,55)

#funkcija za plotovanje za valjevo
def show_valjevo(vreme):
    plt.figure(3)
    plt.title("Odnos zarazenih vremenom - Valjevo")
    show_infected_plot(valjevo_infected,serbia_days,vreme,55)

#funkcija za plotovanje za new york
def show_ny(vreme):
    plt.figure(4)
    plt.title("Odnos zarazenih vremenom - New York")
    show_infected_plot(ny_infected,ny_days,vreme,79)

#funkcija za plotovanje za milano
def show_milano(vreme):
    plt.figure(5)
    plt.title("Odnos zarazenih vremenom - Milano")
    show_infected_plot(milano_infected,milano_days,vreme,7)

#funkcija za plotovanje za svet
def show_world(vreme):
    plt.figure(6)
    plt.title("Odnos zarazenih vremenom - Svet")
    show_infected_plot(world_infected,world_days,vreme,116)

"""
#test funkcije za plotovanje za novi sad    
for i in range(55):
    show_ns(i)

nesto = input()

#test funkcije za plotovanje za valjevo
for i in range(55):
    show_valjevo(i)

nesto = input()

#test funkcije za plotovanje za new york
for i in range(79):
    show_ny(i)

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

    if i > 30 and i < 200:
        show_milano(i-30)
    
    show_plot(zbir,d,h,i,pop)

#ovo postoji da ne bi odmah nakon zavrsetka plotovanja izaslo
nesto = input()
"""