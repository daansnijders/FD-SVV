# -*- coding: utf-8 -*-
import numpy as np
from Cit_par.py import *
from FD_CLCD.py import *

"""Symmetric equations of motion to state space form"""

delta_e = 0.
u = 0.
alpha = 1.
theta = 2. 
q = 3.
V_test = 1.

Dc = c / V_test 

u_bar_sym = np.array([delta_e])
x_bar_sym = np.array([[u], [alpha], [theta], [q]])
x_bardot_sym = np.array([[u_dot], [alpha_dot], [theta_dot], [q_dot]])

C1_sym = np.array([[-2*muc*c/V_test, 0, 0, 0], [0, (CZadot-2*muc)*c/V_test, 0, 0], [0, 0, -c/V_test, 0], [0, Cmadot*c/V_test, 0, -2*muc*KY2*c**2/(V_test**2)]])
C2_sym = np.array([[CXu, CXa, CZ0, c/V_test*CXq], [CZu, CZa, -CX0, c/V_test(CZq+2*muc)], [0, 0, 0, c/V_test], [Cmu, Cma, 0, Cmq*c/V_test]])
C3_sym = np.array([[CXde], [CZde], [0], [Cmde]])


A = -C1_sym**-1*C2_sym
B = -C1_sym**-1*C3_sym
C = np.identity(4)
D = np.zeros((4,1))

"""#Asymmetric equations of motion in state space form"""






