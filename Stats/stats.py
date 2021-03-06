#uvoz potrebnih biblioteka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint as rand
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from base import *

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
pred = []
network = []
br = 1

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
    if infected != 0:  #ovo valja ako odmah u simulaciji krece od jedan
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
funkcija za plotovanje samo inficiranih za parametre prima broj inficiranih, dane i "vreme", tj. iteraciju u petlji
ova funkcija je vama nebitna koristi se samo da se skrati kod kasnije za prikaz realnog sveta
"""
def show_infected_plot(infected,days,vreme):
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.plot(days[0:vreme],infected[0:vreme],color = 'red')
    plt.fill_between(days[0:vreme],infected[0:vreme],color = 'red')
    plt.show()

#funkcija za plotovanje za novi sad
def show_ns(vreme):
    plt.figure(2)
    plt.title("Odnos zarazenih vremenom - Novi Sad")
    show_infected_plot(ns_infected,serbia_days,vreme)

#funkcija za plotovanje za valjevo
def show_valjevo(vreme):
    plt.figure(3)
    plt.title("Odnos zarazenih vremenom - Valjevo")
    show_infected_plot(valjevo_infected,serbia_days,vreme)

#funkcija za plotovanje za new york
def show_ny(vreme):
    plt.figure(4)
    plt.title("Odnos zarazenih vremenom - New York")
    show_infected_plot(ny_infected,ny_days,vreme)

#funkcija za plotovanje za milano
def show_milano(vreme):
    plt.figure(5)
    plt.title("Odnos zarazenih vremenom - Milano")
    show_infected_plot(milano_infected,milano_days,vreme)

#funkcija za plotovanje za svet
def show_world(vreme):
    plt.figure(6)
    plt.title("Odnos zarazenih vremenom - Svet")
    show_infected_plot(world_infected,world_days,vreme)

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

#funkcija za pravljenje neuronske mreze, potreban parametar samo lista zarazenih. Vama nebitna.
def make_model(infected):
    infected = np.array(infected)
    broj_treninga = len(infected)

    scaler = MinMaxScaler(feature_range = (0,1))
    skalirani_podaci = scaler.fit_transform(infected.reshape(-1,1))
    trenazni_podaci = skalirani_podaci[0:broj_treninga,:]

    x_train = []
    y_train = []

    for i in range(20,len(trenazni_podaci)):
        x_train.append(trenazni_podaci[i - 10:i,0])
        y_train.append(trenazni_podaci[i,0])

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

    model = Sequential()
    model.add(LSTM(50,return_sequences = True,input_shape = (x_train.shape[1],1)))
    model.add(LSTM(50,return_sequences = False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=30)
    return model

#funkcija za predikciju broja zarazenih, potrebni parametri lista zarazenih i vreme,tj. iteracija u petlji
def predict_infected(inf,vreme):
    global pred
    global network

    if not pred:
        network = make_model(inf)
    
    podaci = np.array(inf[-10 : ])
    scaler = MinMaxScaler(feature_range = (0,1))
    skalirani_podaci = scaler.fit_transform(podaci.reshape(-1,1))

    x_test = []
    x_test.append(skalirani_podaci)
    x_test = np.array(x_test)

    prediction = network.predict(x_test)
    prediction = scaler.inverse_transform(prediction)
    pred.append(prediction[0,0])

    plt.figure(1)
    plt.plot(time[vreme - len(pred) + 1:],pred,color = 'yellow')
    plt.show()
    
"""
#pokusaj druge funkcije za predikciju
def predict_infected2(inf,vreme):
    global pred
    global network
    global br
    if not np.array(pred).any():
        network = make_model(inf)

        scaler = MinMaxScaler(feature_range = (0,1)) 
        test_data = scaler.fit_transform(np.array(inf[math.ceil(len(inf) * 0.8) - 10:]).reshape(-1,1))
        x_test = []

        for i in range(10,len(test_data)):
            x_test.append(test_data[i - 10:i,0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))

        predictions = network.predict(x_test)
        predictions = scaler.inverse_transform(predictions)

        print(predictions[:,0])
        pred = predictions[:,0]

    plt.figure(1)
    plt.plot(time[vreme:],pred[0:br],color = 'yellow')
    br += 1 
"""

#funkcija za plotovanje situacije iz baze podataka, jedini parametar je redni broj simulacije
def plot_base(i):
    plt.figure(8)
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    case = get_case(i)
    vreme = [i + 1 for i in range(case[4])]
    plt.stackplot(vreme,case[2],case[1],case[3],case[0], labels = label, colors = color)
    plt.legend(loc = 'upper left')
    plt.show()

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

    if i >= 130:
        show_ny(i-130)
    
    if i == 10:
        plot_base(1) 
    
    show_plot(zbir,d,h,i,pop)

#ovo postoji da ne bi odmah nakon zavrsetka plotovanja izaslo
nesto = input()
"""