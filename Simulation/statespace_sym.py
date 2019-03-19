# -*- coding: utf-8 -*-
import numpy as np
from Cit_par_appC import *
import control
import control.matlab as ml
import matplotlib.pyplot as plt
#from FD_CLCD import *
from scipy import signal

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



C1_sym = np.array([[-2*muc*c/V/V, 0, 0, 0], 
                   [0, (CZadot-2*muc)*c/V, 0, 0], 
                   [0, 0, -c/V, 0], 
                   [0, Cmadot*c/V, 0, -2*muc*KY2*c*c/V/V]])
C2_sym = np.array([[CXu/V, CXa, CZ0, (c/V)*CXq], [CZu/V, CZa, -CX0, c/V*(CZq+2*muc)], [0, 0, 0, c/V], [Cmu/V, Cma, 0, Cmq*c/V]])
C3_sym = np.array([[CXde], [CZde], [0], [Cmde]])


A_sym = -np.dot(np.linalg.inv(C1_sym), C2_sym)
B_sym = -np.dot(np.linalg.inv(C1_sym), C3_sym)
C_sym = np.array([[1.,0.,0.,0.], [0.,1.,0.,0.], [0.,0.,1.,0.], [0.,0.,0.,1.]])
D_sym = np.array([[0.],[0.],[0.],[0.]])

#sys_sym = signal.StateSpace(A_sym, B_sym, C_sym, D_sym)
sys_sym2 = ml.ss(A_sym, B_sym, C_sym, D_sym)
eig = np.linalg.eig(A_sym)
#print (sys_sym)


t = np.linspace(0., 150, 150)
u = np.zeros(len(t))
for i in range (20):
    u[i] = -0.006
z,x,c = ml.lsim(sys_sym2, u, t)

#yout, T = ml.impulse(sys_sym2)

plt.subplot(2, 2, 1)
plt.plot(t, (z[:,0] + V))
plt.xlabel('Time [sec]')
plt.ylabel('Velocity')

plt.subplot(2, 2, 2)
plt.plot(t, (z[:,1]))
plt.xlabel('Time [sec]')
plt.ylabel('Angle of Attack [rad]')

plt.subplot(2, 2, 3)
plt.plot(t, (z[:,2]))
plt.xlabel('Time [sec]')
plt.ylabel('Theta [rad]')

plt.subplot(2, 2, 4)
plt.plot(t, (z[:,3]))
plt.xlabel('Time [sec]')
plt.ylabel('q [rad/sec]')



plt.show()
plt.savefig('foo.png')

