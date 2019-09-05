import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi
from matplotlib.animation import FuncAnimation

def func(state,t):
    dydt = np.zeros_like(state)
    dydt[0] = state[1]
    dydt[1] = -(G/L)*sin(state[0])
    return dydt

G = 9.8 #重力加速度
L = 1   #振り子の長さ
th1 = 30.0  #角度の初期値[deg]
w1 = 0.0    #角速度の初期値[deg]

#初期状態
state = np.ra