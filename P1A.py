import numpy as np
def ode1(u, x):
    u1,u2 = u
    du =  [u2,u2+2*u1+np.cos(x)]
    return du

# parameters
a = 0
b = np.pi/2
ya = -0.3
yb = -0.1
yexact = lambda x: -(np.sin(x)+3*np.cos(x))/10
a1 = -1
a2 = 0

# linear shoot method
x = np.linspace(a,b, 20)
from scipy.integrate import odeint
s1 = odeint(ode1, [ya,a1], x)
s2 = odeint(ode1, [ya,a2], x)
yb1 = s1[-1,0]
yb2 = s2[-1,0]
lbd = (yb-yb2)/(yb1-yb2)
a = a1*lbd+a2*(1-lbd)
s = s1*lbd+s2*(1-lbd)

# compute error
yshoot = s[:,0]
yexact = yexact(x)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
plt.plot(x, yshoot, 'b', label='shoot')
plt.plot(x, yexact, 'og', label='exact')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(loc='best')
ax2 = plt.twinx()
plt.plot(x,yshoot-yexact,'--ro',label='error')
plt.legend(loc='best')
plt.ylabel('error')
plt.grid()
plt.savefig('p1a.png')
plt.show()
