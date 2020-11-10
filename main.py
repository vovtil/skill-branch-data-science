import numpy as np
import matplotlib.pyplot as plt
from numpy import *

delta = 0.001

def derivation(x, f):
    return round((f(x) - f(x - delta)) / delta, 2)

def gradient(x1, x2, f):
    return (round(diffx1(x1, x2, f), 2), round(diffx2(x1, x2, f), 2))

def diffx1(x1, x2, f):
    return (f(x1 + delta, x2) - f(x1, x2)) / delta
def diffx2(x1, x2, f):
    return (f(x1, x2 + delta) - f(x1, x2)) / delta

def gradient_optimization_one_dim(x, f):
    for i in range(50):
        x = x - delta * derivation(x, f)
    return x

def gradient_optimization_multi_dim(x1, x2, f):
    for i in range(50):
        x1 = x1 - delta * diffx1(x1, x2, f)
        x2 = x2 - delta * diffx1(x1, x2, f)
    return (x1, x2)

x = 10

def f(x):
    return (cos(x) + (0.05 * (x ** 3)) + math.log2(x ** 2))

print(derivation(x, f))

def f(x1, x2):
    return (x1 ** 2) * cos(x2) + 0.05 * x2 ** 3 + 3 * x1 ** 3 * math.log(2,x2 ** 2)

x1 = 1
x2 = 10

print(gradient(x1, x2, f))

def f(x):
    return cos(x) + 0.05* x ** 3 + math.log(2, x ** 2)

x = 10
print(gradient_optimization_one_dim(x, f))


def f(x1, x2):
    return x1 * cos(x2) + 0.05 * x2 ** 3 + 3 * x1 ** 3 * math.log(2, x2 ** 2)

print(gradient_optimization_multi_dim(4, 10, f))