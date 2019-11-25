from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
def vectorfield(w,t,p):
    x1,y1,x2,y2 = w
    m1,m2,k1,k2,L1,L2,b1,b2 = p
    
    f = [y1,
        (-b1 * y1 - k1 * (x1-L1) + k2 * (x2 - x1 -L2)) / m1,
        y2,
        (-b2 * y2 - k2 * (x2 - x1 - L2)) / m2]
    return f

# Parameter values
# Masses:
m1,m2 = 30,10

# Spring constants
k1,k2 = 100.0,10.0

# Natural lengths
L1,L2 = 36,88

# Friction coefficients
b1,b2 = 1.0,1.0

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1,y1 = 0.5,0.0
x2,y2 = 2.25,0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

t = np.arange(0,50.02,0.02)

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2, L1, L2, b1, b2]
w0 = [x1, y1, x2, y2]

# Call the ODE solver.
wsol = odeint(vectorfield, w0, t, args=(p,),atol=abserr, rtol=relerr)
print(wsol)
plt.plot(t,wsol[:,0],label="x1")
plt.plot(t,wsol[:,2],label="x2")
plt.xlabel("t")
plt.title("coupled spring mass system")
plt.legend()
plt.grid()
plt.show()