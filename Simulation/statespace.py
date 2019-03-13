# -*- coding: utf-8 -*-
import numpy as np
from Cit_par_daan import *
#from FD_CLCD import *
from scipy import signal

"""Symmetric equations of motion to state space form"""

delta_e = 1.
u = 1.
alpha = 1.
theta = 2. 
q = 3.
V_test = 1.
u_dot = 1.
alpha_dot = 1.
theta_dot = 1.
q_dot = 1.

Dc = c / V_test 

u_bar_sym = np.array([delta_e])
x_bar_sym = np.array([[u], [alpha], [theta], [q]])
x_bardot_sym = np.array([[u_dot], [alpha_dot], [theta_dot], [q_dot]])

C1_sym = np.array([[-2*muc*c/V_test, 0, 0, 0], [0, (CZadot-2*muc)*c/V_test, 0, 0], [0, 0, -c/V_test, 0], [0, Cmadot*c/V_test, 0, -2*muc*KY2*c**2/(V_test**2)]])
C2_sym = np.array([[CXu, CXa, CZ0, c/V_test*CXq], [CZu, CZa, -CX0, c/V_test*(CZq+2*muc)], [0, 0, 0, c/V_test], [Cmu, Cma, 0, Cmq*c/V_test]])
C3_sym = np.array([[CXde], [CZde], [0], [Cmde]])


A = -np.matmul(np.linalg.inv(C1_sym), C2_sym)
B = -np.matmul(np.linalg.inv(C1_sym), C3_sym)
C = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
D = np.array([[0],[0],[0],[0]])

sys_sym = signal.StateSpace(A, B, C, D)

print (sys_sym)

"""#Asymmetric equations of motion in state space form"""

delta_e = 1.
u = 1.
alpha = 1.
theta = 2. 
q = 3.
V_test = 1.
u_dot = 1.
alpha_dot = 1.
theta_dot = 1.
q_dot = 1.

Dc = c / V_test 

u_bar_sym = np.array([[delta_a], [delta_r]])
x_bar_sym = np.array([[beta], [phi], [p], [r]])
x_bardot_sym = np.array([[beta_dot], [phi_dot], [p_dot], [r_dot]])

C1_asym = np.array([[(CYbdot-2*mub)*b/V_test, 0, 0, 0],[0, -1/2*b/V_test, 0, 0],[0, 0, -4*mub*KX2*b/V_test, 4*mub*KXZ*b/V_test],[Cnbdot*b/V_test, 0, 4*mub*KXZ*b/V_test, -4*mub*KZ2*b/V_test]])
C2_asym = np.array([[CXu, CXa, CZ0, c/V_test*CXq], [CZu, CZa, -CX0, c/V_test*(CZq+2*muc)], [0, 0, 0, c/V_test], [Cmu, Cma, 0, Cmq*c/V_test]])
C3_asym = np.array([[CXde], [CZde], [0], [Cmde]])


A = -np.matmul(np.linalg.inv(C1_asym), C2_asym)
B = -np.matmul(np.linalg.inv(C1_asym), C3_asym)
C = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
D = np.array([[0],[0],[0],[0]])

sys_sym = signal.StateSpace(A, B, C, D)

print (sys_sym)





