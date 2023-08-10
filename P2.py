import numpy as np
def ode1(u, x):
    u1,u2 = u
    du =  [u2,-u2**2-u1+np.log(x)]
    return du

# parameters
a = 1
b = 2
ya = 0
yb = np.log(2)
yexact = lambda x: np.log(x)
a1 = 1.2
a2 = 0.7

err = 1
tol = 1e-10

# shoot method
n = 1
x = np.linspace(a,b, 50)
from scipy.integrate import odeint
while err>tol and n<=10:
    n = n+1
    s1 = odeint(ode1, [ya,a1], x)
    s2 = odeint(ode1, [ya,a2], x)
    yb1 = s1[-1,0]
    yb2 = s2[-1,0]
    # updata
    a3 = a2+(yb-yb2)*(a2-a1)/(yb2-yb1)
    s3 = odeint(ode1, [ya,a3], x)
    # error
    yb0 = s3[-1,0]
    err = np.abs(yb0-yb)
    # updata
    a1,a2 = a2,a3
    
# compute error
yshoot = s3[:,0]
yex = yexact(x)

import matplotlib.pyplot as plt
plt.figure(1,figsize=(10,4))
plt.plot(x, yshoot, 'b', label='shoot')
plt.plot(x, yex, 'og', label='exact')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(loc='best')
ax2 = plt.twinx()
plt.plot(x,yshoot-yex,'--ro',label='error')
plt.legend(loc='best')
plt.ylabel('error')
plt.grid()
plt.savefig('p2.png')
plt.show()