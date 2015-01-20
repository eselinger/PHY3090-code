#/usr/bin/pyython

import os
import sys
import numpy as np
from  scipy.spatial.distance import cdist

def main():
    bl = sys.argv[1]

    for i in range(1,100):
        n1 = i+1
        n2 = n1
        n3 = n1

        a = 2.

        if bl=='sc':
            basis = np.array([[0.,0.,0.]])
            a1 = np.array([a, 0., 0.])
            a2 = np.array([0., a, 0.])
            a3 = np.array([0., 0., a])

        if bl=='bcc':
            basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, a*0.5]])
            a1 = np.array([a, 0., 0.])
            a2 = np.array([0., a, 0.])
            a3 = np.array([0., 0., a])

        if bl=='fcc':
            basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, 0.],[a*0.5, 0., a*0.5],[0., a*0.5, a*0.5]])
            a1 = np.array([a, 0., 0.])
            a2 = np.array([0., a, 0.])
            a3 = np.array([0., 0., a])     


        lattice = []

        for j in range(len(basis)):
            for z in range(n3):
                for y in range(n2):
                    for x in range(n1):
                        R = x*a1 + y*a2 + z*a3 + basis[j]

                        if R[0] <= (n1-1.)*a:
                            if R[1] <= (n2-1.)*a:
                                if R[2] <= (n3-1.)*a:
                                    lattice.append(R)

        numat = len(lattice)

        r_m=2.
        eps=10.
        ETOT = 0.

        for k in range(numat):
            r = cdist(lattice,np.array([lattice[k]])).flatten()
            r = r[np.nonzero(r)]
            V = eps*((r_m/r)**12 - (2.*(r_m/r)**6))
            ETOT += np.sum(V)
        
        E = ETOT/(numat*2.)
        print E, numat

main()
