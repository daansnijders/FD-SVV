from math import *
import numpy as np
import matplotlib.pyplot as plt
from FD_CLCD import thrust

# Initialize Parameters
rho0 = 1.225                                                #kg/m^3
p0 = 101325                                                 #Pa
T0 = 288.15                                                 #K
gamma = 1.4                                                 #-
g0 = 9.80665                                                #m/s^2
Lambda = -0.0065                                            #K/m
R = 287.                                                    #JK^-1kg^-1
Mu = 1.81*10**-5
Cm_tc = -0.0064



W0 = ((9165+2750)*0.45359237+856.5)*g0                      #N
Ws = 60500                                                  #N
S = 30.0                                                    #m^2
c = 2.0569                                                  #m
b = 15.911                                                  #m
A = b**2/S

# List of Parameters
ET = [1996, 2072, 2150, 2222, 2358, 2430, 2516]             #s
hp = [7970, 8120, 8350, 8550, 7800, 7320, 6850, 7100, 7090] #ft
hp = np.array(hp)*0.3048                                    #m
IAS = [161, 150, 140, 131, 170, 181, 188, 158, 159]         #kts
IAS = np.array(IAS)*0.514444444                             #m/s
alpha = [5, 5.9, 6.8, 7.9, 4.2, 3.6, 3.3, 5.1, 5.1]         #deg
de = [-0.4, -0.9, -1.4, -2.0, -0.1, 0.2, 0.5, -0.5, -1.1]   #deg
de = np.array(de)*(pi/180.)                                 #rad
detr = [2, 2, 2, 2, 2, 2, 1.8, 1.8]                         #deg
detr = np.array(detr)*(pi/180.)                             #rad
Fe = [0, -16, -29, -41, -19, 40, 51, 0, -25]                #N
FFl = [412, 409, 406, 402, 416, 424, 433, 422, 422]         #lbs/hr
FFl = np.array(FFl)*0.45359237                              #kg/hr
FFr = [446, 443, 440, 433, 452, 460, 468, 458, 458]         #lbs/hr
FFr = np.array(FFr)*0.45359237                              #kg/hr
F_used = [620, 642, 658, 675, 708, 726, 740, 767, 788]      #lbs
F_used = np.array(F_used)*0.45359237                        #kg
TAT = [-4.5, -4.9, -5.9, -6.5, -3.5, -2, -0.2, -2.8, -2.8]  #deg   
TAT = np.array(TAT)+273.15                                  #K

# C.G Shift Parameters
delta_de = 0.6*(pi/180.)                                    #rad
delta_cg = 0.0718                                           #m


# List Generated
W_data = []
p = []
M = []
T_ISA = []
T = []
a = []
V_tas = []
rho = []
Re = []
Ve = []
Ve_r = []
dT = []
thrust = []
thrust_standard =[]
T_c = []
T_cs = []
delta_e_eq = []
Fe_r = []

for i in range(len(hp)):
    W_data.append(W0-(F_used[i]*g0))
    p.append(p0*(1+(Lambda*hp[i]/T0))**(-g0/(Lambda*R)))
    M.append(sqrt(((2/(gamma-1))*(((1 + (p0/p[i])*((1 + (gamma-1)/(2*gamma)*((rho0*IAS[i]**2)/p0))**(gamma/(gamma-1)) - 1) )**((gamma-1)/gamma)) - 1))))  
    T_ISA.append(T0 + (Lambda*hp[i]))
    T.append(TAT[i]/(1+((gamma-1)/2)*M[i]**2))
    a.append(sqrt(gamma*R*T_ISA[i]))
    V_tas.append(M[i]*a[i])
    rho.append(p[i]/(R*T_ISA[i]))
    Re.append((rho[i]*V_tas[i]*c)/Mu)
    Ve.append(V_tas[i]*sqrt((rho[i]/rho0)))
    Fe_r.append(Fe[i]*(Ws/W_data[i]))
    Ve_r.append(Ve[i]*sqrt(Ws/W_data[i]))
    
    dT.append(T[i]-T_ISA[i])
    
CN = ((W_data[7]/(0.5*rho0*Ve_r[7]**2*S)) + (W_data[i]/(0.5*rho0*Ve_r[i]**2*S)))/2
Cm_d = -1./(delta_de)*CN*(delta_cg/c)

with open("matlabV1.dat", "w") as output:
    for j in range(7):
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

filename = 'thrust_trim.dat' 
thrust_data = open(filename,'r')
lines = thrust_data.readlines()

for line in lines:
    line1 = (line.strip('\n').split('\t'))
    thrust.append(float(line1[0])+float(line1[1]))
    
filename1 = 'thrust_trim_standard.dat' 
thrust_data1 = open(filename1,'r')
lines1 = thrust_data1.readlines()

for line in lines1:
    line1 = (line.strip('\n').split('\t'))
    thrust_standard.append(float(line1[0])+float(line1[1]))

for i in range(len(thrust)):
    T_c.append(thrust[i]/(0.5*rho[i]*V_tas[i]**2*S))
    T_cs.append(thrust_standard[i]/(0.5*rho[i]*V_tas[i]**2*S))

for i in range(len(T_c)):
    delta_e_eq.append(de[i] - (1/Cm_d) * Cm_tc*(T_cs[i]-T_c[i]))
    


'*** Elevator Trim Curve Plot ***'
z_function = np.polyfit(sorted(Ve_r[:7]), sorted(delta_e_eq), 1)
function = np.poly1d(z_function)

#plt.plot(sorted(Ve_r[:7]), function(sorted(Ve_r[:7])), label='M = [0.23 - 0.32], Re = [8200000 - 12100000]')
#plt.plot(sorted(Ve_r[:7]), sorted(delta_e_eq),'x')
#plt.legend()
#plt.title('Clean cruise (flaps up, gear up)')
#plt.gca().invert_yaxis()
#plt.grid()
#plt.xlabel('Ve [m/s]')
#plt.ylabel('de [rad]')

'*** Elevator vs AoA ***'
z_function1 = np.polyfit(alpha[:7], delta_e_eq[:7], 1)
function1 = np.poly1d(z_function1)

#plt.plot(alpha[:7], function1(alpha[:7]), label='M = [0.23 - 0.32], Re = [8200000 - 12100000]')
#plt.plot(alpha[:7], delta_e_eq[:7], 'x')
#plt.legend()
#plt.title('Clean cruise (flaps up, gear up)')
#plt.grid()
#plt.xlabel('AoA [deg]')
#plt.ylabel('de [rad]')



Cm_a = (function1[1]*-Cm_d)


'*** Elevator Force Curve Plot ***'
z_function2 = np.polyfit(sorted(Ve_r[:7]), sorted(Fe_r[:7]), 2)
function2 = np.poly1d(z_function2)

#plt.plot(sorted(Ve_r[:7]), function2(sorted(Ve_r[:7])), label='M = [0.23 - 0.32], Re = [8200000 - 12100000]')
#plt.plot(Ve_r[:7], Fe_r[:7],'x')
#plt.legend()
#plt.title('Clean cruise (flaps up, gear up)')
#plt.gca().invert_yaxis()
#plt.grid()
#plt.xlabel('Ve [m/s]')
#plt.ylabel('Fe [N]')

'*** Output Cm_a and Cm_d *** '
print (Cm_a), print (Cm_d)
