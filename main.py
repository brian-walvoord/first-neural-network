import sys
import numpy as np
import matplotlib

'''
print("Python: ", sys.version)
print("Numpy: ", np.__version__)
print("Matplotlib: ", matplotlib.__version__)
'''

# input layer -- 2nd hidden layer -- 3rd hidden layer -- output layer
inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5


output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]
print(output)

'''
def compute():
    total = 0
    # total = bias  <---- this causes large decimal when removing lines 18 and 24
    i = 0
    while i < len(inputs):
        total += inputs[i] * weights[i]
        i += 1
    total += bias
    return total


output = compute()
print(output)
'''