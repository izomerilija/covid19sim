import numpy as np

class neural_network:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2 * np.random.random((3,1)) - 1
    
    def __sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def think(self, inputs):
        return self.__sigmoid(np.dot(inputs,self.weights))

    def train(self,inputs,outputs,num):
        for it in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = np.dot(inputs.T,error * output * (1 - output))
            self.weights += adjustment

network = neural_network()
inputs = np.array([[1,1,1],[1,0,1],[0,1,1]])
outputs = np.array([[1,1,0]]).T
network.train(inputs,outputs,10000)

#ispisuje koliko je neuronska mreza sigurna u svoje resenje od 0 do 1
print(network.think(np.array([1,0,0])))
