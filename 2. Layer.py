import numpy as np


inputs = [1.2,2.3,4]

#Number of lists in weights defines the number of neurons in a layer
weights = [[2,1,3],
          [1,2,3],
          [4,1,1]]
biases = [1,2,3]

'''
Weights would always be transposed in dot product because it is
multidimension list and on multiplication the values that would
origiinally be chosed are 2,1,4 which is wrong. These are first weights
of every neuron. Instead we need 2,1,3 to be chosen which is first
list. So we transpose the weights to form new matrix

'''
outputs = np.dot(inputs,np.transpose(weights)) + biases

#There are three outpuut shown which are outputs of 3 neurons respectively
print(outputs)
