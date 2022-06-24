import numpy as np

def nth_power(n, fn = lambda x: x**3):
    '''calculates power for number upto n
    args:
        n: highest number in the list of numbers
        power: power for numbers to false, default is 2'''
    return [fn(i) for i in range(n)]


def sigmoid(x, a =1):
    return 1/(1+np.exp(a*x))

print(nth_power(10))

print(sigmoid(0,0))