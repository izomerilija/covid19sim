import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
plt.ion()

x1 = [1,2,3,4,5]
y1 = [1,1,2,3,5]
y2 = [1,2,4,8,16]

for i in range(50):
    plt.figure(1)
    plt.plot(x1,y1)
    plt.show()
    plt.figure(3)
    plt.plot(x1,y2)
    plt.show()
    plt.pause(0.001)
    if i !=49:
        plt.clf()
    x1.append(i+6)
    y1.append(y1[i+4]+y1[i+3])
    y2.append(y2[i+4]*2)
"""
"""
df = pd.read_excel('Stats/Real stats/Stats world.xlsx')

print(df)
"""

class neural_network():
    def __init__(self,num):
        np.random.seed(1)
        self.weights = 2 * np.random.random((num,1)) - 1

    def think(self,inputs):
        return np.dot(inputs,self.weights)

    def train(self,inputs,outputs,num):
        for it in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * np.dot(inputs.T,error)
            self.weights += adjustment

network = neural_network(3)
inputs = np.array([[1,1,2],[1,2,3],[2,3,5],[3,5,8]])
outputs = np.array([[3,5,8,13]]).T
network.train(inputs,outputs,10000)

#predvidja ispis, trenirana da radi na osnovu fibonacijevog niza
print(network.think(np.array([8,13,21])))

nesto = input()