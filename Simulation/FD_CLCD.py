from math import * 
import numpy as np
import matplotlib.pyplot as plt

# Initialize Parameters
rho0 = 1.225                                    #kg/m^3
p0 = 101325                                     #Pa
T0 = 288.15                                     #K
gamma = 1.4                                     #-
g0 = 9.80665                                    #m/s^2
Lambda = -0.0065                                #K/m
R = 287.                                        #JK^-1kg^-1
            
W0 = 15053*0.45359237*g0                        #N
S = 30.0                                        #m^2
c = 2.0569                                      #m
b = 15.911                                      #m
A = b**2/S
    
Cd0 = 0.04                                      #-
e = 0.8                                         #-

# Flight Test Measurements Data
hp = [8000,8000,8000,8000,8010,8000]            #ft
hp = np.array(hp)*0.3048                        #m
TAT = [2.0, -0.5, -2.8, -4.2, -5.5, -6.0]       #deg
TAT = np.array(TAT)+273.15                      #K
IAS = [250, 219, 190, 160, 132, 114]            #kts
IAS = np.array(IAS)*0.514444444                 #m/s
alpha = [1.4, 2.1, 3.3, 5.2, 7.7, 11.1]         #deg
alpha_rad = np.array(alpha) * (pi/180.)    #rad
FFl = [732, 605, 506, 421, 410, 397]            #lbs/hr
FFl = np.array(FFl)*0.45359237                  #kg/hr
FFr = [777, 650, 546, 473, 444, 430]            #lbs/hr
FFr = np.array(FFr)*0.45359237                  #kg/hr
F_used = [405, 440, 469, 500, 530, 555]         #lbs
F_used = np.array(F_used)*0.45359237*g0         #N
pitch = [0.95, 1.7, 2.7, 4.7, 6.8, 10.2]        #deg
pitch_rad = np.array(pitch) * (pi/180.)    #rad

# List of Parameters From Flight Test
W_data = []
M = []
T = []
T_ISA = []
a = []
p = []
V_tas = []
CL = []
CL_2 = []
CD = []
rho = []
dT = []
thrust = []

# Calculated Parameters From Flight Test
for i in range(len(F_used)):
    W_data.append(W0-F_used[i])
    p.append(p0*(1+(Lambda*hp[i]/T0))**(-g0/(Lambda*R)))
    M.append(sqrt(((2/(gamma-1))*(((1 + (p0/p[i])*((1 + (gamma-1)/(2*gamma)*((rho0*IAS[i]**2)/p0))**(gamma/(gamma-1)) - 1) )**((gamma-1)/gamma)) - 1))))  
    T_ISA.append(T0 + (Lambda*hp[i]))
    T.append(TAT[i]/(1+((gamma-1)/2)*M[i]**2))
    a.append(sqrt(gamma*R*T_ISA[i]))
    V_tas.append(M[i]*a[i])
    rho.append(p[i]/(R*T_ISA[i]))
    CL.append(W_data[i]/(0.5*rho[i]*V_tas[i]**2*S))
    dT.append(T[i]-T_ISA[i])

CL_2 = np.array(CL)**2
            
with open("matlab.dat", "w") as output:
    for j in range(len(hp)):
        output.write(str(hp[j]))
        output.write(' ')
        output.write(str(M[j]))
        output.write(' ')
        output.write(str(dT[j]))
        output.write(' ')
        output.write(str(FFl[j]/3600))
        output.write(' ')
        output.write(str(FFr[j]/3600))
        output.write('\n')
            
filename = 'thrust.dat' 
thrust_data = open(filename,'r')
lines = thrust_data.readlines()

for line in lines:
    line1 = (line.strip('\n').split('\t'))
    thrust.append(float(line1[0])+float(line1[1]))
    
# CD Calculations
for k in range(len(thrust)):
    CD.append(thrust[k]/(0.5*rho[k]*V_tas[k]**2*S))

#----------------------------------------------------------------------------------------------------

