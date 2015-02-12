#/usr/bin/python

#system parameters
k = 20.0
m = 3.0
x0 = 4.
dt = 0.001

#initial conditions
x = 2.
v = 0.
a = 0.
t = 0.

for i in range(10000):
    f = -k*(x - x0)
    a = f/m
    v = v + a*dt
    x = x + v*dt
    t = i*dt
    
    KE = 0.5*m*v**2
    PE = 0.5*k*(x - x0)**2
    TE = KE + PE

    print t, x #specify parameter you are interested in vs. time 
