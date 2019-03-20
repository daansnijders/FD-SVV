from math import *
import numpy as np
import matplotlib.pyplot
from flight_data import *

time_d1 = time_d1
V_tas_d1 = np.array(V_tas_d1)*0.514444444
V_cas_d1 = np.array(V_cas_d1)*0.514444444
roll_angle_d1 = np.array(roll_angle_d1)*(pi/180)
pitch_angle_d1 = np.array(pitch_angle_d1)*(pi/180)
body_roll_rate_d1 = np.array(body_roll_rate_d1)*(pi/180)
body_pitch_rate_d1 = np.array(body_pitch_rate_d1)*(pi/180)
body_yaw_rate_d1 = np.array(body_yaw_rate_d1)*(pi/180)
fuel_right_d1 = np.array(fuel_right_d1)*0.45359237
fuel_left_d1 = np.array(fuel_left_d1)*0.45359237
delta_a_d1 = np.array(delta_a_d1)*(pi/180)
delta_e_d1 = np.array(delta_e_d1)*(pi/180)
delta_r_d1 = np.array(delta_r_d1)*(pi/180)
hp_d1 = np.array(hp_d1)*0.3048
m_d1 = m_d1
T_ISA_d1 = T_ISA_d1
rho_d1 = rho_d1
p_d1 = p_d1
AoA_d1 = np.array(AoA_d1)*(pi/180)

print (lst_element)

"*** Phugoid Motion ***"
time_phugoid = 170
x_f1 = 0
x_b1 = 0
x_change1 = (-x_f1 + x_b1)

#plt.subplot(221)
#plt.plot(np.arange(0,time_phugoid+x_change1,0.1), V_tas_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])
#plt.xlabel('Time [s]')
#plt.ylabel('V [m/s]')
#plt.grid()
#
#plt.subplot(222)
#plt.plot(np.arange(0,time_phugoid+x_change1,0.1), pitch_angle_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])
#plt.xlabel('Time [s]')
#plt.ylabel(r'$\Theta$ [rad]')
#plt.grid()
#
#plt.subplot(223)
#plt.plot(np.arange(0,time_phugoid+x_change1,0.1), AoA_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])
#plt.xlabel('Time [s]')
#plt.ylabel(r'$\alpha$ [rad]')
#plt.grid()
#
#plt.subplot(224)
#plt.plot(np.arange(0,time_phugoid+x_change1, 0.1), body_pitch_rate_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])
#plt.xlabel('Time [s]')
#plt.ylabel('q [rad/s]')
#plt.grid()

#delta_e_input_phugoid =  (delta_e_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])

"*** Short Period ***"
time_short = 15
x_f2 = 0
x_b2 = 0  
x_change2 = (-x_f2 + x_b2)

#plt.subplot(221)
#plt.plot(np.arange(0,time_short+x_change2,0.1), V_tas_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])
#plt.xlabel('Time [s]')
#plt.ylabel('V [m/s]')
#plt.grid()
#
#plt.subplot(222)
#plt.plot(np.arange(0,time_short+x_change2,0.1), pitch_angle_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])
#plt.xlabel('Time [s]')
#plt.ylabel(r'$\Theta$ [rad]')
#plt.grid()
#
#plt.subplot(223)
#plt.plot(np.arange(0,time_short+x_change2,0.1), AoA_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])
#plt.xlabel('Time [s]')
#plt.ylabel(r'$\alpha$ [rad]')
#plt.grid()
#
#plt.subplot(224)
#plt.plot(np.arange(0,time_short+x_change2,0.1), body_pitch_rate_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])
#plt.xlabel('Time [s]')
#plt.ylabel('q [rad/s]')
#plt.grid()

#delta_e_input_short = (delta_e_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])

"*** Dutch Roll ***" 
time_dutch = 15
x_f3 = 0
x_b3 = 0
x_change3 = (-x_f3 + x_b3)

#plt.subplot(221)
#plt.plot(np.arange(0,time_short+x_change3,0.1), roll_angle_d1[lst_element[4]+x_f3*10:lst_element[4]+time_short*10+x_b3*10])
#plt.xlabel('Time [s]')
#plt.ylabel(r'$\phi$ [rad]')
#plt.grid()
#
#plt.subplot(222)
#plt.plot(np.arange(0,time_short+x_change3,0.1), body_roll_rate_d1[lst_element[4]+x_f3*10:lst_element[4]+time_short*10+x_b3*10])
#plt.xlabel('Time [s]')
#plt.ylabel('p [rad/s]')
#plt.grid()
#
#plt.subplot(223)
#plt.plot(np.arange(0,time_short+x_change3,0.1), body_yaw_rate_d1[lst_element[4]+x_f3*10:lst_element[4]+time_short*10+x_b3*10])
#plt.xlabel('Time [s]')
#plt.ylabel('r [rad/s]')
#plt.grid()

#delta_a_input_dutch = (delta_a_d1[lst_element[4]+x_f3*10:lst_element[4]+time_dutch*10+x_b3*10])
#delta_r_input_dutch = (delta_r_d1[lst_element[4]+x_f3*10:lst_element[4]+time_dutch*10+x_b3*10])

"*** 