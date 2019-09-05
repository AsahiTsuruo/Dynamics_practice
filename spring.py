import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 0.5
k = 1000
state0 = [0.0,0.1]

t0 = 0
tf = 1
dt = 0.005
t = np.arange(t0,tf+dt,dt)

def func(state,t,m,k):
    x1,x2 = state
    dx2dt = -(k/m)*x1
    return [x2,dx2dt]

sol = odeint(func,state0,t,args=(m,k))

omega = np.sqrt(k/m)
v_equation = (-1 * state0[0] * omega * np.sin(omega * t) + state0[1] * np.cos(omega * t))

# フォントの種類とサイズを設定する。
plt.rcParams["font.size"] = 14
plt.rcParams["font.family"] = "Times New Roman"
# 目盛を内側に
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# グラフの上下左右に目盛線
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
# 軸のラベルを設定
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Velocity [m/s]")
# データの範囲と刻み目盛を明示
ax1.set_xticks(np.arange(0,2,0.2))
ax1.set_yticks(np.arange(-1,1,0.1))
ax1.set_xlim(0,1)
ax1.set_ylim(-0.2,0.2)
# データプロット
ax1.plot(t,sol[:,1],label="Python odeint [x0=0, v0=0.1]",c="b",marker="o",linestyle="None")
ax1.plot(t,v_equation,label="v_equation",c="r")

fig.tight_layout()
plt.legend(loc="upper left")
# グラフ表示
plt.show()


