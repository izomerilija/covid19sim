#potrebne biblioteke
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

#podaci za koriscenje
podaci = np.array([1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])
redovi = math.ceil(len(podaci) * 0.8)

#skalirani podaci
scaler = MinMaxScaler(feature_range = (0,1))
skalirani_podaci = scaler.fit_transform(podaci.reshape(-1,1))

#podaci za treniranje
trenazni_podaci = skalirani_podaci[0:redovi,:]
x_train = []
y_train = []

for i in range(3,len(trenazni_podaci)):
    x_train.append(trenazni_podaci[i - 3:i,0])
    y_train.append(trenazni_podaci[i,0])

x_train = np.array(x_train)
y_train = np.array(y_train)
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

#Kreacija LSTM modela
model = Sequential()
model.add(LSTM(50,return_sequences = True,input_shape = (x_train.shape[1],1)))
model.add(LSTM(50,return_sequences = False))
model.add(Dense(25))
model.add(Dense(1))

#trening modela
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=1, epochs=100)

#kreacije podataka za testiranje
test_data = skalirani_podaci[redovi - 3: , : ]
x_test = []

for i in range(3,len(test_data)):
    x_test.append(test_data[i-3:i,0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))

#pravimo predikcije
predictions = model.predict(x_test) 
predictions = scaler.inverse_transform(predictions)

#kreacija podataka za plotovanje
train = podaci[:redovi]
valid = podaci[redovi - 1:]
valid2 = predictions
time = [i for i in range(15)]

#plotovanje
plt.figure(figsize=(8,5))
plt.title('Fibonacijev niz')
plt.xlabel('Redni broj', fontsize=18)
plt.ylabel('Vrednost', fontsize=18)
plt.plot(time[:redovi],train)
plt.plot(time[redovi - 1:],valid)
plt.plot(time[redovi:],valid2)
plt.show()

#poslednja tri
pod = podaci[-3:]
skal_pod = scaler.transform(pod.reshape(-1,1))
X_test = []
X_test.append(skal_pod)
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
pred = model.predict(X_test)
pred = scaler.inverse_transform(pred)
print(pred)