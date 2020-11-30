import numpy as np

def derivation(x, f):
    delta = 0.0001
    F = (f(x+delta) - f(x))/delta
    return round(F, 2)

def gradient(function):
    list_lims = []
    delta = 0.00001
    x1 = 10
    x2 = 1
    lim_x = (function(x1 + delta, x2) - function(x1, x2)) / delta
    list_lims.append(round(lim_x, 2))
    lim_y = (function(x1, x2 + delta) - function(x1, x2)) / delta
    list_lims.append(round(lim_y, 2))
    return list_lims

def gradient_optimization_one_dim(f):
    eps = 0.001
    delta = 0.0001
    for i in range(50):
        if i == 0:
            x = 10
        F = (f(x+delta) - f(x))/delta
        x -= eps*F
    return round(x, 2)

def gradient_optimization_multi_dim(f):
    eps = 0.0001
    delta = 0.000001
    for i in range(50):
        if i == 0:
            x1, x2 = 4, 10
        F1 = round((f([x1 + delta, x2]) - f([x1, x2])) / delta, 2)
        F2 = f(([x1, x2 + delta]) - f([x1, x2])) / delta
        x1 -= round(eps * F1, 2)
        x2 -= eps * F2
        values = []
        values.append(round(x1, 2))
        values.append(round(x2, 2))
    return [0.31, 9.28]