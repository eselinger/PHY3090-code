#/usr/bin/python

#system parameters
k = 20.
m = 3.
r0 = 2.
dt = 0.001

#initial conditions
x1 = 2.
x2 = 6.
v1 = 0.
v2 = 0.
a1 = 0.
a2 = 0.
t = 0.

for i in range(10000):
    x02 = x1 + 2
    f = -k*(
    f2 = -k2*((x2 - x02))

    a1 = f1/m1
    a2 = f2/m2
    
    v1 = v1 + a1*dt
    v2 = v2 + a2*dt
    
    x1 = x1 + v1*dt
    x2 = x2 + v2*dt
 
    t = i*dt
    
    KE = 0.5*(m1*v1**2 + m2*v2**2)
    PE = 0.5*(k1*(x1 - x01)**2 + k2*(x2 - x1 - x02)**2)
    TE = KE + PE

    print t, x1, x2 #specify parameter you are interested in vs. time 
