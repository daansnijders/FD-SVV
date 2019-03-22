from math import * 
import matplotlib.pyplot as plt


time_d1 = []
V_tas_d1 = []
V_cas_d1 = []
roll_angle_d1 = []
pitch_angle_d1 = []
body_roll_rate_d1 = []
body_pitch_rate_d1 = []
body_yaw_rate_d1 = []
fuel_right_d1 = []
fuel_left_d1 = []
delta_a_d1 = []
delta_e_d1 = []
delta_r_d1 = []
hp_d1 = []
m_d1 = []
T_ISA_d1 = []
rho_d1 = []
p_d1 = []
AoA_d1 = []

lst_element = [27380, 28010, 28510, 30540, 31140, 32710]

g0 = 9.80665    
S = 30.0   
m0 = 13803.1*0.45359237
R = 287.
p0 = 101325.
T0 = 288.15
Lambda = -0.0065  

"*** Time ***"
filename = 'time.dat' 
time_data = open(filename,'r')
lines = time_data.readlines()

for line in lines:
    line1 = line.strip('   ').split('   ')
    for i in range(len(line1)):
        time_d1.append(float(line1[i]))

"*** True Airspeed ***"
filename = 'V_tas.dat' 
V_tas_data = open(filename,'r')
lines = V_tas_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    V_tas_d1.append(float(line1[0]))

"*** Calibrated Airspeed ***"
filename = 'V_cas.dat' 
V_cas_data = open(filename,'r')
lines = V_cas_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    V_cas_d1.append(float(line1[0]))

"*** Roll Angle ***"
filename = 'roll_angle.dat' 
roll_angle_data = open(filename,'r')
lines = roll_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    roll_angle_d1.append(float(line1[0]))

"*** Pitch Angle ***"
filename = 'pitch_angle.dat' 
pitch_angle_data = open(filename,'r')
lines = pitch_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    pitch_angle_d1.append(float(line1[0]))

"*** Body Roll Rate ***"
filename = 'body_roll_rate.dat' 
body_roll_rate_data = open(filename,'r')
lines = body_roll_rate_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    body_roll_rate_d1.append(float(line1[0]))

"*** Body Pitch Rate ***"
filename = 'body_pitch_rate.dat' 
body_pitch_rate_data = open(filename,'r')
lines = body_pitch_rate_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    body_pitch_rate_d1.append(float(line1[0]))
    
"*** Body Yaw Rate ***"
filename = 'body_yaw_rate.dat' 
body_yaw_rate_data = open(filename,'r')
lines = body_yaw_rate_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    body_yaw_rate_d1.append(float(line1[0]))

"*** Fuel Right Engine ***"
filename = 'fuel_right.dat' 
fuel_right_data = open(filename,'r')
lines = fuel_right_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    fuel_right_d1.append(float(line1[0]))
    
"*** Fuel Left Engine ***"
filename = 'fuel_left.dat' 
fuel_left_data = open(filename,'r')
lines = fuel_left_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    fuel_left_d1.append(float(line1[0]))

"*** deflection aileron (right wing?) ***"
filename = 'delta_a.dat' 
delta_a_data = open(filename,'r')
lines = delta_a_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_a_d1.append(float(line1[0]))

"*** deflection elevator ***"
filename = 'delta_e.dat' 
delta_e_data = open(filename,'r')
lines = delta_e_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_e_d1.append(float(line1[0]))

"*** deflection rudder ***"
filename = 'delta_r.dat' 
delta_r_data = open(filename,'r')
lines = delta_r_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_r_d1.append(float(line1[0]))
    

"*** altitude ***"
filename = 'altitude.dat' 
altitude_data = open(filename,'r')
lines = altitude_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    hp_d1.append(float(line1[0]))

"*** Angle of Attack ***"
filename = 'AoA.dat' 
AoA_data = open(filename,'r')
lines = AoA_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    AoA_d1.append(float(line1[0]))


#---------------------------------------------------------------------------------------------------



for i in range(len(fuel_left_d1)):
    total_mass = (fuel_left_d1[i] + fuel_right_d1[i] )*0.45359237
    T_ISA_d1.append(T0 + Lambda*hp_d1[i]*0.3048) 
    p_d1.append(p0*(1+(Lambda*hp_d1[i]*0.3048/T0))**(-g0/(Lambda*R)))
    rho_d1.append(p_d1[i]/(R*T_ISA_d1[i]))
    m_d1.append(m0 - total_mass)
    
thrust_d = [0, 3677.93, 3731.13, 3652.73, 3701.04, 3734.19, 3093.23]
time_d = [0]
V_tas_d = [0]
V_cas_d = [0]
roll_angle_d = [0]
pitch_angle_d = [0]
body_roll_rate_d = [0]
body_pitch_rate_d = [0]
body_yaw_rate_d = [0]
fuel_right_d = [0]
fuel_left_d = [0]
delta_a_d = [0]
delta_e_d = [0]
delta_r_d = [0]
hp_d = [0]
m_d = [0]
rho_d = [0]
CL_d = [0]
CD_d = [0]

for i in lst_element:
    time_d.append(time_d1[i])                                   #s
    V_tas_d.append(V_tas_d1[i]*0.514444444)                     #m/s
    V_cas_d.append(V_cas_d1[i]*0.514444444)                     #m/s
    roll_angle_d.append(roll_angle_d1[i]*(pi/180))              #rad
    pitch_angle_d.append(pitch_angle_d1[i]*(pi/180))            #rad
    body_roll_rate_d.append(body_roll_rate_d1[i]*(pi/180))      #rad/s
    body_pitch_rate_d.append(body_pitch_rate_d1[i]*(pi/180))    #rad/s
    body_yaw_rate_d.append(body_yaw_rate_d1[i]*(pi/180))        #rad/s
    fuel_right_d.append(fuel_right_d1[i]*0.45359237)            #kg
    fuel_left_d.append(fuel_left_d1[i]*0.45359237)              #kg
    delta_a_d.append(delta_a_d1[i]*(pi/180))                    #rad
    delta_e_d.append(delta_e_d1[i]*(pi/180))                    #rad
    delta_r_d.append(delta_r_d1[i]*(pi/180))                    #rad
    hp_d.append(hp_d1[i]*0.3048)                                #m
    m_d.append(m_d1[i])                                         #kg
    rho_d.append(rho_d1[i])                                     #kg/m^3

for i in range(1, len(thrust_d), 1):
    CL_d.append((m_d[i]*g0)/(0.5*rho_d[i]*(V_tas_d[i]**2)*S))
    CD_d.append((thrust_d[i])/(0.5*rho_d[i]*V_tas_d[i]**2*S))
