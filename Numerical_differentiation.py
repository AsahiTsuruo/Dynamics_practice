import numpy as np
import matplotlib.pyplot as plt

def nummerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
def sample_func(x):
    return x**2
x = np.arange(-7.0, 7.0, 0.1)
x2 = np.arange(-1.0, 7.0, 0.1)
k = 2

y = sample_func(x)
d = nummerical_diff(sample_func,k)
y2 = d * x2 + sample_func(k) - d*k

plt.plot(x,y)
plt.plot(x2,y2)
plt.show()