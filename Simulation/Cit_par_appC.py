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

S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 5.5    # tail length [m]
          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
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
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.3925

# Aerodynamic constants

Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
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
N=0