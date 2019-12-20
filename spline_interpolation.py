import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

#Determine function
n = 11
f = lambda x: -1 + (2/(1 + 16 * x ** 2))
x = np.linspace(-1, 1, n)
y = f(x)

#Spline interpolation
xx = np.linspace(-1, 1, 200)
yy = interp.spline(x, y, xx)

#Plot data
plt.plot(x, y, 'ro') #Sampled data
#plt.hold(True)
plt.plot(xx, yy, 'm') #Polynominal interpolation
#plt.hold(True)
plt.plot(xx, f(xx)) #Original function
plt.xlabel('x')
plt.title('-1 + (2/(1 + 16 * x ** 2))')
plt.savefig('8_1_c.png', dpi=1200)