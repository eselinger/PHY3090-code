#/usr/bin/python

import numpy as np
from scipy import integrate
from scipy import constants as con


Td = 300.
Te = 288.
N = 2.

f = lambda x: ((x**4)*np.exp(x))/(np.exp(x) - 1.)**2

for T in range(500):
    T = T+1
    y = Td/T
    z = Te/T
    x = integrate.quad(f,0,y)
    x = float(x[0])

    C_D = 9.*N*con.k*(y**3)*x
    C_E = 3*N*con.k*(z**2)*(np.exp(z)/((np.exp(z) - 1)**2))
    print T,C_D,C_E
