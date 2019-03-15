# -*- coding: utf-8 -*-
import numpy as np
from Cit_par_appC import *
import control
import control.matlab as ml
import matplotlib.pyplot as plt
#from FD_CLCD import *
from scipy import signal

"""Symmetric equations of motion to state space form"""

V = 59.9

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



t = np.linspace(0., 150, 150)
u = np.zeros(len(t))
u[:] = -0.005
z,x,c = ml.lsim(sys_sym2, u, t)

#yout, T = ml.impulse(sys_sym2)

plt.plot(t, (z[:,3]))
plt.show()

#print (sys_sym)

"""#Asymmetric equations of motion in state space form"""

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




