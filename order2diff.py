import numpy as np
import pylab
import scipy.integrate
import funcs

name = "non-auto"

f = funcs.NonAuto
#parameter setting
gamma,omega = 0.1,np.sqrt(3.0)
eps,omega2 = 1.0,np.sqrt(3.0)
args = (gamma,omega,eps,omega2)

#initial condition
sample = 5
x0 = np.linspace(0.0,1.0,sample)
x1 = np.zeros(sample)
initsets = [np.array(x) for x in zip(x0,x1)]
#print("initsets",initsets)

#integration
dt = 0.01
t = np.arange(0,30,dt)
"""
for x0 in initsets:
    print(x0)
"""
trajectories = [scipy.integrate.odeint(f,x0,t,args,Dfun=None) for x0 in initsets]
#print("trajectories",trajectories)

vcolors = pylab.cm.autumn_r(np.linspace(0.3, 1.0, sample)) # color parameters
for i,x in enumerate(trajectories):
    x = x.T
    pylab.plot(t,x[0],"-",lw=2) #,label='(%.f, %.f)' % (x0[i],x1[i]))
pylab.xlabel("time",fontsize=20)
pylab.ylabel("x",fontsize=20,rotation="horizontal")
pylab.savefig(name+".eps")
pylab.show()