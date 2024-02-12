import sys
import numpy as np
import matplotlib

'''
print("Python: ", sys.version)
print("Numpy: ", np.__version__)
print("Matplotlib: ", matplotlib.__version__)
'''

# input layer -- 2nd hidden layer -- 3rd hidden layer -- output layer
inputs = [2.3, 4.5, 1.2]
weights = [6.6, 3.4, 1.2]
bias = 3


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
