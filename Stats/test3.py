import numpy as np

class neural_network:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2 * np.random.random((2,1)) - 1

    def think(self,inputs):
        return(np.dot(inputs,self.weights))

    def train(self,inputs,outputs,num):
        for it in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * np.dot(inputs.T,error)
            self.weights += adjustment

network = neural_network()
inputs = np.array([[2,3],[1,1],[5,2],[12,3]])
outputs = np.array([[10,4,14,30]]).T
network.train(inputs,outputs,10000)

#ispisuje rezultat (a+b)*2
print(network.think(np.array([15,2])))