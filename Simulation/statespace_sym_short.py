# -*- coding: utf-8 -*-
import numpy as np
from Cit_par_updated import *
import control
import control.matlab as ml
import matplotlib.pyplot as plt
#from FD_CLCD import *
from scipy import signal
from flight_data_plots import *

"""Symmetric equations of motion to state space form"""

#delta_e = 1.
#
#u = 1.
#alpha = 1.
#theta = 2. 
#q = 3.
#
#u_dot = 1.
#alpha_dot = 1.
#theta_dot = 1.
#q_dot = 1.
#
#
#u_bar_sym = np.array([delta_e])
#x_bar_sym = np.array([[u], [alpha], [theta], [q]])
#x_bardot_sym = np.array([[u_dot], [alpha_dot], [theta_dot], [q_dot]])



C1_sym = np.array([[-2*muc*c/V0/V0, 0, 0, 0], 
                   [0, (CZadot-2*muc)*c/V0, 0, 0], 
                   [0, 0, -c/V0, 0], 
                   [0, Cmadot*c/V0, 0, -2*muc*KY2*c*c/V0/V0]])
C2_sym = np.array([[CXu/V0, CXa, CZ0, (c/V0)*CXq], [CZu/V0, CZa, -CX0, c/V0*(CZq+2*muc)], [0, 0, 0, c/V0], [Cmu/V0, Cma, 0, Cmq*c/V0]])
C3_sym = np.array([[CXde], [CZde], [0], [Cmde]])


A_sym = -np.dot(np.linalg.inv(C1_sym), C2_sym)
B_sym = -np.dot(np.linalg.inv(C1_sym), C3_sym)
C_sym = np.array([[1.,0.,0.,0.], [0.,1.,0.,0.], [0.,0.,1.,0.], [0.,0.,0.,1.]])
D_sym = np.array([[0.],[0.],[0.],[0.]])

#sys_sym = signal.StateSpace(A_sym, B_sym, C_sym, D_sym)
sys_sym2 = ml.ss(A_sym, B_sym, C_sym, D_sym)
eig = np.linalg.eig(A_sym)
#print (sys_sym)

t = np.linspace(0., 15, 150)
u = np.zeros(len(t))
for i in range (20):
    u[i] = -0.006

"""Initial conditions"""
X0_short = np.array([[V_tas_d1[lst_element[1]]],[AoA_d1[lst_element[1]]],[pitch_angle_d1[lst_element[1]]],[body_pitch_rate_d1[lst_element[1]]]])
z,x,c = ml.lsim(sys_sym2, delta_e_input_short, t)


#yout, T = ml.impulse(sys_sym2)

plt.subplot(2, 2, 1)
plt.plot(t, (z[:,0] + V0), label='Numerical model')
plt.xlabel('Time [s]')
plt.ylabel('V [m/s]')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(t, (z[:,1]+ X0_short[1]), label='Numerical model')
plt.xlabel('Time [s]')
plt.ylabel(r'$\alpha$ [rad]')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t, (z[:,2]+ X0_short[2]), label='Numerical model')
plt.xlabel('Time [s]')
plt.ylabel(r'$\theta$ [rad]')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(t, (z[:,3]), label='Numerical model')
plt.xlabel('Time [s]')
plt.ylabel('q [rad/sec]')
plt.legend()


plt.show()
plt.savefig('sym-short.png')
