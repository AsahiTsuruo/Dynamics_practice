#sin waveをシンク関数に変更
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def ff_h(F_h,omega_h,t):
    return F_h * (0.5 * np.sin(omega_h * t)/(omega_h*t))

def ff_r(F_r,omega_r,gamma_r,t):
    return F_r * (0.5 * np.sin(omega_r * t))

def kin_f(z,t,p):
    z_h_eta = 1.24
    z_r_eta = 0.6
    k_r,k_h,c_r,c_h,m_r,m_h,F_h,F_r,gamma_r,omega_h,omega_r,g = p
    z_0,z_1,z_2,z_3 = z
    ips_h = (z_0 - z_h_eta)/z_h_eta
    ips_r = ((z_2 - z_0) - z_r_eta) / z_r_eta
    eta_h = 0.5 + 0.5 * np.tanh(- np.power(10,4)) * ips_h
    eta_r = 0.5 + 0.5 * np.tanh(- np.power(10,4))* ips_r
    #eta_h = 1
    #eta_r = 1
    f = [z_1,
        (-eta_h * c_h * z_1 - eta_r * c_r * (z_1 - z_3) - eta_h * k_h * ips_h + eta_r * k_r * ips_r - m_h * g + eta_h * ff_h(F_h,omega_h,t))/m_h,
        z_3,
        (-eta_r * c_r * (z_3 - z_1) - eta_r * k_r * ips_r - m_r * g + eta_r * ff_r(F_r,omega_r,gamma_r,t))/m_r]
     
    return f
def main():
    z_h,v_h = 1.24,0.0
    z_r,v_r = 0.6,0.0

    k_r = 9000.0
    k_h = 5200.0
    c_r = 3000.0
    c_h = 5000.0
    m_r = 60.0
    m_h = 600.0
    F_h = 9900.0
    Freq_h = 2.4
    F_r = 1200.0
    Freq_r = 1.2
    gamma_r = 0.0 * np.pi
    omega_h = 2.0 * np.pi * Freq_h
    omega_r = 2.0 * np.pi * Freq_r
    g = 9.8
    
    initset = np.array([z_h,v_h,z_r,v_r])#hの変位、速度の初期値、rの変位、速度の初期値
    p = (k_r,k_h,c_r,c_h,m_r,m_h,F_h,F_r,gamma_r,omega_h,omega_r,g)

    dt = 0.005
    t = np.arange(-0.835*12,0.835*12,dt)
    abserr = 1.0e-8
    relerr = 1.0e-6
    trajectory = odeint(kin_f,initset,t,args=(p,),Dfun=None,atol=abserr, rtol=relerr)
    #print(trajectory)

    ax=plt.subplot()
    #z_h = trajectory[:,0]
    #z_r = trajectory[:,2]
    #ax.set_ylim([-0.1,0.1])
    t = np.arange(0,0.835*6,dt)
    #z_h = trajectory[167*24:,0] - np.average(trajectory[167*24:,0])
    #z_r = trajectory[167*24:,2] - np.average(trajectory[167*24:,2])
    #z_h = trajectory[1670-167*2:1670+167*3,0] - np.average(trajectory[1670-167*2:1670+167*3,0])
    #z_r = trajectory[1670-167*2:1670+167*3,2] - np.average(trajectory[1670-167*2:1670+167*3,2])
    z_h = trajectory[1670+167*5:1670+167*11,0] - np.average(trajectory[1670+167*5:1670+167*11,0])
    z_r = trajectory[1670+167*5:1670+167*11,2] - np.average(trajectory[1670+167*5:1670+167*11,2])
    #print("ave",np.average(trajectory[167*4:,0]),np.average(trajectory[167*4:,2]))
    #v_h = trajectory[167*24:,1]
    #v_r = trajectory[167*24:,3]
    #ips_h = (z_h - 1.24)/1.24
    #ips_r = (z_r - z_h -0.6)/0.6
    #eta_h = 0.5 + 0.5 * np.tanh(- np.power(10,4)) * ips_h
    #eta_r = 0.5 + 0.5 * np.tanh(- np.power(10,4)) * ips_r
    #F_h = -eta_h * c_h * v_r - eta_r * c_r * (v_r - v_h) - eta_h * k_h * ips_h + eta_r * k_r * ips_r - m_h * g + eta_h * ff_h(F_h,omega_h,t)
    #F_r = -eta_r * c_r * (v_r - v_h) - eta_r * k_r * ips_r - m_r * g + eta_r * ff_r(F_r,omega_r,gamma_r,t)
    #P_h = F_h*v_h
    #P_r = F_r*v_r
    #print("P_h",np.sum(P_r[0:168]))
    #print("v",v_h)
    plt.plot(t,z_h,label = "horse",color="r")
    plt.plot(t,z_r,label = "rider",color = "b")
    #plt.plot(t,P_h,label = "horse",color="r")
    #plt.plot(t,P_r,label = "rider",color = "b")
    plt.xlabel("t")
    plt.ylabel("z")
    plt.title("z_h & z_r")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()