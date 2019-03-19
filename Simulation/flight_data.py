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
lst_element = [27380, 28010, 28510, 30540, 31140, 32710]

"*** Time ***"
filename = 'time.dat' 
time_data = open(filename,'r')
lines = time_data.readlines()

for line in lines:
    line1 = line.strip('   ').split('   ')
    time_d = line1

"*** True Airspeed ***"
filename = 'V_tas.dat' 
V_tas_data = open(filename,'r')
lines = V_tas_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    V_tas_d1.append(line1[0])

"*** Calibrated Airspeed ***"
filename = 'V_cas.dat' 
V_cas_data = open(filename,'r')
lines = V_cas_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    V_cas_d1.append(line1[0])

"*** Roll Angle ***"
filename = 'roll_angle.dat' 
roll_angle_data = open(filename,'r')
lines = roll_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    roll_angle_d1.append(line1[0])

"*** Pitch Angle ***"
filename = 'pitch_angle.dat' 
pitch_angle_data = open(filename,'r')
lines = pitch_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    pitch_angle_d1.append(line1[0])

"*** Body Roll Rate ***"
filename = 'body_roll_rate.dat' 
body_roll_rate_data = open(filename,'r')
lines = body_roll_rate_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    body_roll_rate_d1.append(line1[0])

"*** Body Pitch Rate ***"
filename = 'body_pitch_rate.dat' 
body_pitch_rate_data = open(filename,'r')
lines = body_pitch_rate_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    body_pitch_rate_d1.append(line1[0])

"*** Fuel Right Engine ***"
filename = 'fuel_right.dat' 
fuel_right_data = open(filename,'r')
lines = fuel_right_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    fuel_right_d1.append(line1[0])
    
"*** Fuel Left Engine ***"
filename = 'fuel_left.dat' 
fuel_left_data = open(filename,'r')
lines = fuel_left_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    fuel_left_d1.append(line1[0])

"*** deflection aileron (right wing?) ***"
filename = 'delta_a.dat' 
delta_a_data = open(filename,'r')
lines = delta_a_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_a_d1.append(line1[0])

"*** deflection elevator ***"
filename = 'delta_e.dat' 
delta_e_data = open(filename,'r')
lines = delta_e_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_e_d1.append(line1[0])

"*** deflection rudder ***"
filename = 'delta_r.dat' 
delta_r_data = open(filename,'r')
lines = delta_r_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    delta_r_d1.append(line1[0])
    

"*** altitude ***"
filename = 'altitude.dat' 
altitude_data = open(filename,'r')
lines = altitude_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    hp_d1.append(line1[0])

time_d = []
for i in lst_element:
    time_d.append(time_d1[i])

 


