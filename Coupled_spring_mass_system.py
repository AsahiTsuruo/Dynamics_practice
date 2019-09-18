from scipy.integrate import odeint
import matplotlib.pyplot as plt

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
m1,m2 = 1.0,1.5

# Spring constants
k1,k2 = 8.0,40.0

# Natural lengths
L1,L2 = 0.5,1.0

# Friction coefficients
b1,b2 = 0.8,0.5

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1,y1 = 0.5,0.0
x2,y2 = 2.25,0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2, L1, L2, b1, b2]
w0 = [x1, y1, x2, y2]

# Call the ODE solver.
wsol = odeint(vectorfield, w0, t, args=(p,),atol=abserr, rtol=relerr)

plt.plot(t,wsol[:,0],label="x1")
plt.plot(t,wsol[:,2],label="x2")
plt.xlabel("t")
plt.title("coupled spring mass system")
plt.legend()
plt.grid()
plt.show()