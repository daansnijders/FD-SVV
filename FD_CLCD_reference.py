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
            
W0 = (9165.+4050)*0.45359237+695.               #kg
S = 30.0                                        #m^2
c = 2.0569                                      #m
b = 15.911                                      #m
    
Cd0 = 0.04                                      #-
e = 0.8                                         #-

# Flight Test Measurements Data
hp = [5010,5020,5020,5030,5020,5110]            #ft
hp = np.array(hp)*0.3048                        #m
TAT = [12.5,10.5,8.8,7.2,6.,5.2]                #deg
TAT = np.array(TAT)+T0                          #K
IAS = [249.,221.,192.,163.,130.,118.]            #kts
IAS = np.array(IAS)*0.514444444                 #m/s
alpha = [1.7,2.4,3.6,5.4,8.7,10.6]         #deg
FFl = [798,673,561,463,443,474]            #lbs/hr
FFl = np.array(FFl)*0.45359237                  #kg/hr
FFr = [813,682,579,484,467,499]            #lbs/hr
FFr = np.array(FFr)*0.45359237                  #kg/hr
F_used = [360,412,447,478,532,570]         #lbs
F_used = np.array(F_used)*0.45359237            #kg


# List of Parameters From Flight Test
W_data = []
M = []
T = []
a = []
V_tas = []
CL = []
rho = []
dT = []
p = []
# Calculated Parameters From Flight Test
for i in range(len(F_used)):
    p.append(p0*(1+(Lambda*hp[i]/T0))**(-g0/(Lambda*R)))
    W_data.append((W0-F_used[i])*9.81)          #NEWTON!
    M.append(sqrt(((2/(gamma-1))*(((1 + (p0/p[i])*((1 + (gamma-1)/(2*gamma)*((rho0*IAS[i]**2)/p0))**(gamma/(gamma-1)) - 1) )**((gamma-1)/gamma)) - 1))))  
    T.append(TAT[i]/(1+((gamma-1)/2)*M[i]**2))
    a.append(sqrt(gamma*R*T[i]))
    V_tas.append(M[i]*a[i])
    rho.append(p[i]/(R*T[i]))
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

z = np.polyfit(alpha, CL, 1)
p = np.poly1d(z)
plt.plot(alpha,p(alpha),"r--")
plt.plot(alpha, CL, 'b^')
plt.xlabel('alpha [deg]')
plt.ylabel('CL [-]') #CL-alpha for reference data with polynominal in red given by z=z[0]*x+z[1]
#z[0]*180/pi #deg per radian
#----------------------------------------------------------------------------------------------------

