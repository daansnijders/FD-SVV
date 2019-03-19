# -*- coding: utf-8 -*-
"""#Asymmetric equations of motion in state space form"""
import numpy as np
from Cit_par_appC import *
import control
import control.matlab as ml
import matplotlib.pyplot as plt
#from FD_CLCD import *
from scipy import signal

V = 82.

#delta_a = 1.
#delta_r = 1.
#
#beta = 1.
#phi = 2. 
#p = 3.
#r = 4.
#
#beta_dot = 1.
#phi_dot = 1.
#p_dot = 1.
#r_dot = 1.
#
#
#u_bar_sym = np.array([[delta_a], [delta_r]])
#x_bar_sym = np.array([[beta], [phi], [p], [r]])
#x_bardot_sym = np.array([[beta_dot], [phi_dot], [p_dot], [r_dot]])

C1_asym = np.array([[(CYbdot-2*mub)*b/V, 0, 0, 0],[0, -1/2*b/V, 0, 0],[0, 0, -4*mub*KX2*b/V*b/2/V, 4*mub*KXZ*b/V*b/2/V],[Cnbdot*b/V, 0, 4*mub*KXZ*b/V*b/2/V, -4*mub*KZ2*b/V*b/2/V]])
C2_asym = np.array([[CYb, CL, CYp*b/2/V, (CYr-4*mub)*b/2/V],[0,0,1*b/2/V,0],[Clb, 0, Clp*b/2/V, Clr*b/2/V],[Cnb, 0, Cnp*b/2/V, Cnr*b/2/V]])
C3_asym = np.array([[CYda, CYdr], [0,0], [Clda, Cldr], [Cnda, Cndr]])


A_asym = -np.matmul(np.linalg.inv(C1_asym), C2_asym)
B_asym = -np.matmul(np.linalg.inv(C1_asym), C3_asym)
C_asym = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
D_asym = np.array([[0,0],[0,0],[0,0],[0,0]])

sys_asym = signal.StateSpace(A_asym, B_asym, C_asym, D_asym)

sys_asym2 = ml.ss(A_asym, B_asym, C_asym, D_asym)
#print (sys_asym)

t = np.linspace(0., 150, 150)
u = np.zeros((len(t),2))
for i in range (20):
    u[i,0] = -0.006
z,x,c = ml.lsim(sys_asym2, u, t)

#yout, T = ml.impulse(sys_sym2)

plt.subplot(2, 2, 1)
plt.plot(t, (z[:,0] + V))
plt.xlabel('Time [s]')
plt.ylabel('Velocity')

plt.subplot(2, 2, 2)
plt.plot(t, (z[:,1]))
plt.xlabel('Time [s]')
plt.ylabel('Angle of Attack [rad]')

plt.subplot(2, 2, 3)
plt.plot(t, (z[:,2]))
plt.xlabel('Time [s]')
plt.ylabel('Theta [rad]')

plt.subplot(2, 2, 4)
plt.plot(t, (z[:,3]))
plt.xlabel('Time [s]')
plt.ylabel('q')



plt.show()
plt.savefig('foo.png')