from math import * 
import matplotlib.pyplot as plt


time_d = [0]
V_tas_d = [0]
V_cas_d = [0]
roll_angle_d = [0]
pitch_angle_d = [0]
body_roll_rate_d = [0]
body_pitch_rate_d = [0]
body_yaw_rate_d = [0]

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
    V_tas_d.append(line1[0])

"*** Calibrated Airspeed ***"
filename = 'V_cas.dat' 
V_cas_data = open(filename,'r')
lines = V_cas_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    V_cas_d.append(line1[0])

"*** Roll Angle ***"
filename = 'roll_angle.dat' 
roll_angle_data = open(filename,'r')
lines = roll_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    roll_angle_d.append(line1[0])

"*** Pitch Angle ***"
filename = 'pitch_angle.dat' 
pitch_angle_data = open(filename,'r')
lines = pitch_angle_data.readlines()

for line in lines:
    line1 = line.strip('  ').split('  ')
    pitch_angle_d.append(line1[0])


        

