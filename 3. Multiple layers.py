import numpy as np

#Lets use the same data from 2. Layers

inputs = [1.2,2.3,4]


class Layer_Dense:

    def __init__(self, n_inputs, n_neurons):

        #Weights are biases are defined by network
        #0.1 is multiplied by weights to normalize them in smaller range
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

#Shape of inputs is the number of instances/columns for first layer
layer1 = Layer_Dense(3,8)
layer1.forward(inputs)
print(layer1.output)

#Lets add another layer
#Shape of all other layers would be output shape of  previous layer
layer2 = Layer_Dense(8,3)
layer2.forward(layer1.output)
print(layer2.output)

#We can add batch of data

X = [[1.2,2.3,4],
    [1,2,0],
    [3,9,7]]

#Everything else remains same, just pass this data to layers
layer1 = Layer_Dense(3,8)
layer1.forward(X)
print(layer1.output)