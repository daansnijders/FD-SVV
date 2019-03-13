from math import * 
import numpy as np
import matplotlib.pyplot as plt

# Initialize Parameters
rho0 = 1.225                                    #kg/m^3
p0 = 101325                                     #Pa
T0 = 273.15                                     #K
gamma = 1.4                                     #-
g0 = 9.80665                                    #m/s^2
Lambda = -0.0065                                #K/m
R = 287.                                        #JK^-1kg^-1
            
W0 = 60250.                                     #kg
S = 30.0                                        #m^2
c = 2.0569                                      #m
b = 15.911                                      #m
    
Cd0 = 0.04                                      #-
e = 0.8                                         #-

# Flight Test Measurements Data
hp = [8000,8000,8000,8000,8000,8000]            #ft
hp = np.array(hp)*0.3048                        #m
TAT = [2.0, -0.5, -2.8, -4.2, -5.5, -6.0]       #deg
TAT = np.array(TAT)+T0                          #K
IAS = [250, 219, 190, 160, 132, 114]            #kts
IAS = np.array(IAS)*0.514444444                 #m/s
alpha = [1.4, 2.1, 3.3, 5.2, 7.7, 11.1]         #deg
alpha_rad = np.array(alpha) * (math.pi/180.)    #rad
FFl = [732, 605, 506, 421, 410, 397]            #lbs/hr
FFl = np.array(FFl)*0.45359237                  #kg/hr
FFr = [777, 650, 546, 473, 444, 430]            #lbs/hr
FFr = np.array(FFr)*0.45359237                  #kg/hr
F_used = [405, 440, 469, 500, 530, 555]         #lbs
F_used = np.array(F_used)*0.45359237            #kg
p = p0*(1+(Lambda*hp[0]/T0))**(-g0/(Lambda*R))
pitch = [0.95, 1.7, 2.7, 4.7, 6.8, 10.2]          #deg
pitch_rad = np.array(pitch) * (math.pi/180.)    #rad

# List of Parameters From Flight Test
W_data = []
M = []
T = []
a = []
V_tas = []
CL = []
rho = []
dT = []

# Calculated Parameters From Flight Test
for i in range(len(F_used)):
    W_data.append(W0-F_used[i])
    M.append(sqrt(((2/(gamma-1))*(((1 + (p0/p)*((1 + (gamma-1)/(2*gamma)*((rho0*IAS[i]**2)/p0))**(gamma/(gamma-1)) - 1) )**((gamma-1)/gamma)) - 1))))  
    T.append(TAT[i]/(1+((gamma-1)/2)*M[i]**2))
    a.append(sqrt(gamma*R*T[i]))
    V_tas.append(M[i]*a[i])
    rho.append(p/(R*T[i]))
    CL.append(W_data[i]/(0.5*rho[i]*V_tas[i]**2*S))
    T_ISA = T0 + (Lambda*hp[i])
    dT.append(T[i]-T_ISA)

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

plt.plot(alpha, CL, 'b^')
plt.xlabel('alpha [deg]')
plt.ylabel('CL [-]')

#----------------------------------------------------------------------------------------------------

