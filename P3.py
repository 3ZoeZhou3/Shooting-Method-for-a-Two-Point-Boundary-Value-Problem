import numpy as np
def ode1(u, x):
    u1,u2 = u
    du =  [u2,u2+2*u1+np.cos(x)]
    return du

# parameters
x0 = 0
xn = np.pi/2
ya = -0.3
yb = -0.1
yexact = lambda x: -(np.sin(x)+3*np.cos(x))/10

Nvec = [10,20]

for N in Nvec:
    
    h = (xn-x0)/N
    x = np.linspace(x0,xn,N+1)
    
    # comoute the matrix a,b,c,d
    a = np.zeros(N-1)
    b = np.zeros(N-1)
    c = np.zeros(N-1) 
    d = np.zeros(N-1) 
    for i in range(N-1):
        a[i] = -(1+h/2)
        b[i] = -h**2*np.cos(x[i+1])
        c[i] = -(1-h/2)
        d[i] = 2+2*h**2       
        
    # comute A,b   
    A = np.zeros((N-1,N-1))
    for i in range(N-1):
        if i<N-2:
            A[i,i+1]=c[i]
        if i>0:
            A[i,i-1]=a[i]
        A[i,i] = d[i]
    for i in range(N-1):
        if i == 0:
            b[i] = b[i]-a[i]*ya
        if i==N-2:
            b[i] = b[i]-c[i]*yb
    
    # solve 
    y = np.linalg.solve(A,b)
    yfdm = np.concatenate(([ya,],y,[yb,]),axis= 0)
    yex = yexact(x)
    err = yex-yfdm
    
    # plt
    import matplotlib.pyplot as plt
    plt.figure(1,figsize=(10,7))
    plt.subplot(2,1,1)
    plt.plot(x, yfdm, '--',lw=2, label='y for N'+str(N))
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend(loc='best')
    plt.subplot(2,1,2)
    plt.plot(x, err, '--',lw=2, label='error for N'+str(N))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.legend(loc='best')
plt.subplot(2,1,1)
plt.grid()
plt.subplot(2,1,2)
plt.grid()
plt.savefig('p3.png')
plt.show()
