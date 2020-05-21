
#Coding simple neuron
# A simply neuron is consist of some inputs multiplied by weights and an added bias
#Every input has a different attached to it

inputs = [1.2,2,3,4,5]
weights = [2,3,1]
bias = 2

#Output of neuron

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)
#Every neuron has only one ouput
#This output can be sent to many neurons in next layer