from FD_CLCD import *

'*** CL-Alpha Plot ***'
#z = np.polyfit(alpha, CL, 1)
#p1 = np.poly1d(z)
#plt.plot(alpha, p1(alpha),"b--")
#plt.plot(alpha, CL, 'x')
#plt.xlabel('alpha [deg]')
#plt.ylabel('CL [-]')

'*** CD-Alpha Plot ***'
#z = np.polyfit(alpha, CD, 2)
#p1 = np.poly1d(z)
#plt.plot(alpha, p1(alpha),"b--") 
#plt.plot(alpha, CD, 'x')
#plt.xlabel('alpha [deg]')
#plt.ylabel('CD [-]')
#plt.show()

'*** CL-CD Plot [from data points] ***'
#z = np.polyfit(CD, CL, 2)
#p1 = np.poly1d(z)
#plt.plot(CD, p1(CD),"b--")  
#plt.plot(CD, CL, 'x')
#plt.xlabel('CD [-]')
#plt.ylabel('CL [-]')

'*** CD-CL^2 Plot ***'
#z = np.polyfit(CL_2, CD, 1)
#p1 = np.poly1d(z)
#plt.plot(CL_2, p1(CL_2))
#plt.plot(CL_2, CD, 'x')

'*** CL-CD plot [from equation] ***'
CL_new = np.arange(-0.3, 1.4, 0.02)
CD_new = []

for c in range(len((CL_new))):
    CD_new.append(CD0 + (CL_new[c]**2)/(pi*A*e))
    
plt.plot(CD_new, CL_new, '^', markersize=2.0)
plt.xlabel('CD [-]')
plt.ylabel('CL [-]')


