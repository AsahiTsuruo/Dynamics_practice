import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import funcs

name = "non-auto"

f = funcs.NonAuto
#parameter setting
gamma,omega = 0.1,np.sqrt(3.0)
eps,omega2 = 1.0,np.sqrt(3.0)
args = (gamma,omega,eps,omega2)

#initial condition
initset = np.array([1.0,0])#変位、速度の初期値

#integration
dt = 0.01
t = np.arange(0,30,dt)
trajectory = odeint(f,initset,t,args,Dfun=None)
print(trajectory)
print(trajectory[0])


plt.plot(t,trajectory[:,0])#変位の表示
plt.show()