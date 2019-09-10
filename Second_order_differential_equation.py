import numpy as np
from scipy.integrate import odeint

g = 9.8
m = 1.0
h = 10

def f(x,t):
    ret = [
        x[1],
        -g/m
    ]
    return ret

def main():
    x0 = [
        h,
        0
    ]

    t = np.arange(0,10,0.1)
    x = odeint(f,x0,t)
    print(x)

if __name__ == "__main__":
    main()