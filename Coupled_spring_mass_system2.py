from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
def vectorfield(w,t,p):
    x1,y1,x2,y2 = w
    m1,m2,k1,k2 = p
    
    f = [y1,
        (- k1 * x1 + k2 * (x2 - x1) + 3900.0 * np.sin(2.0 * np.pi * 2.4 * t)) / m1,
        y2,
        (- k2 * (x2 - x1)) / m2]
    return f

# Parameter values
# Masses:
m1,m2 = 600.0,60.0

# Spring constants
k1,k2 = 52000.0,55000.0


# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1,y1 = 0.0,0.0
x2,y2 = 0.0,0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6


t = np.arange(0.0,0.8,0.005)

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2]
w0 = [x1, y1, x2, y2]

# Call the ODE solver.
wsol = odeint(vectorfield, w0, t, args=(p,),atol=abserr, rtol=relerr)
print(wsol)
plt.plot(t,wsol[:,0],label="horse")
plt.plot(t,wsol[:,2],label="rider")
plt.xlabel("t")
plt.title("coupled spring mass system")
plt.legend()
plt.grid()
plt.show()