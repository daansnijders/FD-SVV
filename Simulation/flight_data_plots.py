from math import *
import numpy as np
import matplotlib.pyplot
from flight_data import *
from Cit_par_updated import i

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

delta_e_input_phugoid =  (delta_e_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10])


if i == 3:   
    plt.subplot(221)
    plt.plot(np.arange(0,time_phugoid+x_change1,0.1), V_tas_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('V [m/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(222)
    plt.plot(np.arange(0,time_phugoid+x_change1,0.1), pitch_angle_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\Theta$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_phugoid+x_change1,0.1), AoA_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\alpha$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_phugoid+x_change1, 0.1), body_pitch_rate_d1[lst_element[2]+x_f1*10:lst_element[2]+time_phugoid*10+x_b1*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('q [rad/s]')
    plt.grid()
    plt.legend()



"*** Short Period Motion ***"
time_short = 15
x_f2 = 0
x_b2 = 0  
x_change2 = (-x_f2 + x_b2)

delta_e_input_short = (delta_e_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10])

if i == 2:
    plt.subplot(221)
    plt.plot(np.arange(0,time_short+x_change2,0.1), V_tas_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('V [m/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(222)
    plt.plot(np.arange(0,time_short+x_change2,0.1), pitch_angle_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10],label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\Theta$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_short+x_change2,0.1), AoA_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\alpha$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_short+x_change2,0.1), body_pitch_rate_d1[lst_element[1]+x_f2*10:lst_element[1]+time_short*10+x_b2*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('q [rad/s]')
    plt.grid()
    plt.legend()



"*** Dutch Roll ***" 
time_dutch = 12
x_f3 = 0
x_b3 = 0
x_change3 = (-x_f3 + x_b3)

delta_a_input_dutch = (delta_a_d1[lst_element[3]+x_f3*10:lst_element[3]+time_dutch*10+x_b3*10])
delta_r_input_dutch = (delta_r_d1[lst_element[3]+x_f3*10:lst_element[3]+time_dutch*10+x_b3*10])

if i == 4:
    plt.subplot(222)
    plt.plot(np.arange(0,time_dutch+x_change3,0.1), roll_angle_d1[lst_element[3]+x_f3*10:lst_element[3]+time_dutch*10+x_b3*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\phi$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_dutch+x_change3,0.1), body_roll_rate_d1[lst_element[3]+x_f3*10:lst_element[3]+time_dutch*10+x_b3*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('p [rad/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_dutch+x_change3,0.1), body_yaw_rate_d1[lst_element[3]+x_f3*10:lst_element[3]+time_dutch*10+x_b3*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('r [rad/s]')
    plt.grid()
    plt.legend()


"*** Dutch Roll Yaw Motion ***"
time_dutch_yaw = 12
x_f4 = 0
x_b4 = 0
x_change4 = (-x_f4 + x_b4)

delta_a_input_dutch_yaw = (delta_a_d1[lst_element[4]+x_f4*10:lst_element[4]+time_dutch_yaw*10+x_b4*10])
delta_r_input_dutch_yaw = (delta_r_d1[lst_element[4]+x_f4*10:lst_element[4]+time_dutch_yaw*10+x_b4*10])

if i == 5:
    plt.subplot(222)
    plt.plot(np.arange(0,time_dutch_yaw+x_change4,0.1), roll_angle_d1[lst_element[4]+x_f4*10:lst_element[4]+time_dutch_yaw*10+x_b4*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\phi$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_dutch_yaw+x_change4,0.1), body_roll_rate_d1[lst_element[4]+x_f4*10:lst_element[4]+time_dutch_yaw*10+x_b4*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('p [rad/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_dutch_yaw+x_change4,0.1), body_yaw_rate_d1[lst_element[4]+x_f4*10:lst_element[4]+time_dutch_yaw*10+x_b4*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('r [rad/s]')
    plt.grid()
    plt.legend()

"*** A-Periodic Roll Motion ***"
time_aperiodic = 7
x_f5 = 0
x_b5 = 0
x_change5 = (-x_f5 + x_b5)

delta_a_input_aperiodic = (delta_a_d1[lst_element[0]+x_f5*10:lst_element[0]+time_aperiodic*10+x_b5*10])
delta_r_input_aperiodic = (delta_r_d1[lst_element[0]+x_f5*10:lst_element[0]+time_aperiodic*10+x_b5*10])

if i == 1:
    plt.subplot(222)
    plt.plot(np.arange(0,time_aperiodic+x_change5,0.1), roll_angle_d1[lst_element[0]+x_f5*10:lst_element[0]+time_aperiodic*10+x_b5*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\phi$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_aperiodic+x_change5,0.1), body_roll_rate_d1[lst_element[0]+x_f5*10:lst_element[0]+time_aperiodic*10+x_b5*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('p [rad/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_aperiodic+x_change5,0.1), body_yaw_rate_d1[lst_element[0]+x_f5*10:lst_element[0]+time_aperiodic*10+x_b5*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('r [rad/s]')
    plt.grid()
    plt.legend()

"*** Spiral Motion ***"
time_spiral = 100
x_f6 = 0
x_b6 = 0 
x_change6 = (-x_f6 + x_b6)

delta_a_input_spiral = (delta_a_d1[lst_element[5]+x_f6*10:lst_element[5]+time_spiral*10+x_b6*10])
delta_r_input_spiral = (delta_r_d1[lst_element[5]+x_f6*10:lst_element[5]+time_spiral*10+x_b6*10])

if i == 6:
    plt.subplot(222)
    plt.plot(np.arange(0,time_spiral+x_change6,0.1), roll_angle_d1[lst_element[5]+x_f6*10:lst_element[5]+time_spiral*10+x_b6*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel(r'$\phi$ [rad]')
    plt.grid()
    plt.legend()
    
    plt.subplot(223)
    plt.plot(np.arange(0,time_spiral+x_change6,0.1), body_roll_rate_d1[lst_element[5]+x_f6*10:lst_element[5]+time_spiral*10+x_b6*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('p [rad/s]')
    plt.grid()
    plt.legend()
    
    plt.subplot(224)
    plt.plot(np.arange(0,time_spiral+x_change6,0.1), body_yaw_rate_d1[lst_element[5]+x_f6*10:lst_element[5]+time_spiral*10+x_b6*10], label='Validation Data')
    plt.xlabel('Time [s]')
    plt.ylabel('r [rad/s]')
    plt.grid()
    plt.legend()






