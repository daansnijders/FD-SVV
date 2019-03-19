# -*- coding: utf-8 -*-
"""#Asymmetric equations of motion in state space form"""
import numpy as np
from Cit_par_appC import *
import control
import control.matlab as ml
import matplotlib.pyplot as plt
#from FD_CLCD import *
from scipy import signal

V = 59.9

# Citation 550 - Linear simulation
from math import *
c      = 2.0569
xcg = 0.30 * c

# Stationary flight condition

hp0    =    1.      # pressure altitude in the stationary flight condition [m]
V0     =     1.    # true airspeed in the stationary flight condition [m/sec]
alpha0 =      1.     # angle of attack in the stationary flight condition [rad]
th0    =       1.      # pitch angle in the stationary flight condition [rad]

# Aircraft mass
m      =    4547.8       # mass [kg]

# aerodynamic properties
e      =    0.8     # Oswald factor [ ]
CD0    =     0.04      # Zero lift drag coefficient [ ]
CLa    =       5.084      # Slope of CL-alpha curve [ ]

# Longitudinal stability
Cma    =    -0.5626      # longitudinal stabilty [ ]
Cmde   =     -1.1642       # elevator effectiveness [ ]

# Aircraft geometry

S      = 24.2	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 5.5    # tail length [m]
          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 13.36         # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * pi / 180   # stabiliser angle of incidence [rad]

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lambdas = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

# air density [kg/m^3]  
rho    = rho0 * ( ((1+(lambdas * hp0 / Temp0)))**(-((g / (lambdas*R)) + 1)))   
W      = m * g            # [N]       (aircraft weight)

# Constant values concerning aircraft inertia

muc    = 102.7
mub    = 15.5
KX2    = 0.012
KZ2    = 0.037
KXZ    = 0.002
KY2    = 1.3925

# Aerodynamic constants

Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL = 1.1360            # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (pi * A * e) # Drag coefficient [ ]

# Stabiblity derivatives

CX0    = 0
CXu    = -0.0279
CXa    = -0.4797
CXadot = 0.0833
CXq    = -0.2817
CXde   = -0.0373

CZ0    = -1.1360
CZu    = -0.3762
CZa    = -5.7434
CZadot = -0.0035
CZq    = -5.6629
CZde   = -0.6961

Cmu    = 0.0699
Cmadot = 0.1780
Cmq    = -8.7941

CYb    = -0.9896
CYbdot =  0     
CYp    = -0.087
CYr    = 0.43
CYda   = 0
CYdr   = 0.3037

Clb    = -0.0772
Clp    = -0.3444
Clr    = 0.2800
Clda   = -0.2349
Cldr   = 0.0286

Cnb    =  0.1638
Cnbdot =   0
Cnp    =  -0.0108
Cnr    =  -0.1930
Cnda   =  0.0286
Cndr   =  -0.1261


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

t = np.linspace(0., 15, 150)
u = np.zeros((len(t),2))
for i in range (10):
    u[i,1] = 0.025
z,x,c = ml.lsim(sys_asym2, u, t)

#yout, T = ml.impulse(sys_sym2)

plt.subplot(2, 2, 1)
plt.plot(t, (z[:,0]))
plt.xlabel('Time [sec]')
plt.ylabel(r'$\beta$ [rad]')

plt.subplot(2, 2, 2)
plt.plot(t, (z[:,1]))
plt.xlabel('Time [sec]')
plt.ylabel(r'$\varphi$ [rad]')

plt.subplot(2, 2, 3)
plt.plot(t, (z[:,2]))
plt.xlabel('Time [s]')
plt.ylabel('p [rad/sec]')

plt.subplot(2, 2, 4)
plt.plot(t, (z[:,3]))
plt.xlabel('Time [s]')
plt.ylabel('r [rad/sec]')



plt.show()
plt.savefig('foo.png')