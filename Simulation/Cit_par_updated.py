# Citation 550 - Linear simulation
from math import *
# xcg = 0.25 * c
from FD_CLCD import e, CD0, CLa, CL, CD #For Stationary Part
from flight_data import time_d, V_tas_d, V_cas_d, roll_angle_d, pitch_angle_d, body_roll_rate_d, body_pitch_rate_d, body_yaw_rate_d, hp_d, m_d, CL_d, CD_d #For stationary meas during dynamic part

motion_names = ["Zeros as input", "Aperiodic Roll", "Short Period", "Phugoid", "Dutch Roll", "Dutch Roll with Yaw Damper", "Spiral"]

print()
print("What motion are you working on?")
print("0) Results in errors")
print("1) Aperiodic Roll")
print("2) Short Period")
print("3) Phugoid (Long Period)")
print("4) Dutch Roll")
print("5) Dutch Roll With Yaw Damper")
print("6) Spiral")
print()

i = int(input("i =  "))
print("Chosen: ", motion_names[i])

# ==========================CHOOSE WHICH MOTION===================================================
# i = 0 #Check code, result is zer
# i = 1 #Aperiodic Roll
# i = 2 #Short Period 
# i = 3 #Phugoid 
# i = 4 #Dutch Roll 
# i = 5 #Dutch Roll with Yaw Damper 
# i = 6 #Spiral 
# =============================================================================


"""ÏNPUTS FROM THE FLIGHT DATA:"""

# Stationary flight condition JUST before Manouevre

hp0    =  hp_d[i]    	         # pressure altitude in the stationary flight condition [m]
V0     =  V_tas_d[i]            # true airspeed in the stationary flight condition [m/sec]
#alpha0 =  9999999999.           # angle of attack in the stationary flight condition [rad]
th0    =   pitch_angle_d[i]     # math.pitch angle in the stationary flight condition [rad]

# Aircraft mass
m      =   m_d[i]          # mass [kg]

# aerodynamic properties
e      =     e        # Oswald factor [ ]
CD0    =     CD0      # Zero lift drag coefficient [ ]
CLa    =     CLa       # Slope of CL-alpha curve [ RAD ! ]

# Longitudinal stability
Cma    =     -0.796        # longitudinal stabilty [as found by Stationary Measurements ]
Cmde   =     -1.521      # elevator effectiveness [as found by stationary Measurments ]


""""CALCULATE THE OTHER PARAMETERS FROM THESE INPUTS:"""

# Aircraft geometry
S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 0.71 * 5.968    # tail length [m]
c      = 2.0569	          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * pi / 180   # stabiliser angle of incidence [rad]

# Constant values concerning atmosphere and gravity02.

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lambdas = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

# air density [kg/m^3]  
rho    = rho0 * ((1+(lambdas * hp0 / Temp0)))**(-((g / (lambdas*R)) + 1))
W      = m * g            # [N]       (aircraft weight)

# Constant values concerning aircraft inertia

muc    = m / (rho * S * c)
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114

# Aerodynamic constants

Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL =  CL_d[i]       # Lift coefficient [ ]
CD =  CD_d[i]       # Drag coefficient [ ]

#--------------------------------------------------------

# Stabiblity derivatives

CX0    = W * sin(th0) / (0.5 * rho * V0 ** 2 * S)
CXu    = -0.02792
CXa    = -0.47966
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -W * cos(th0) / (0.5 * rho * V0 ** 2 * S)
CZu    = -0.37616
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939
