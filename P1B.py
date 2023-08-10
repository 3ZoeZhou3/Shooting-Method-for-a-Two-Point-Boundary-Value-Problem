import numpy as np
def ode1(u, x):
    u1,u2 = u
    du =  [u2,3*u1-x*(1-x)]
    return du

# parameters
a = 0
b = 1
ya = 0
yb = 1
yexact = lambda x: -x**2/3+x/3-2/9 +(2*(-7+(np.sqrt(3)+1)*np.exp(np.sqrt(3)))*np.exp(np.sqrt(3)*(1-x))+2*(-1+np.sqrt(3)+7*np.exp(np.sqrt(3)))*np.exp(np.sqrt(3)*x))/(9*(-1+np.sqrt(3)+np.exp(2*np.sqrt(3))+np.sqrt(3)*np.exp(2*np.sqrt(3))))
a1 = 0
a2 = 1

# linear shoot method
x = np.linspace(a,b, 20)
from scipy.integrate import odeint
s1 = odeint(ode1, [ya,a1], x)
s2 = odeint(ode1, [ya,a2], x)
yb1 = s1[-1,0]+s1[-1,1]
yb2 = s2[-1,0]+s2[-1,1]
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
plt.savefig('p1b.png')
plt.show()
