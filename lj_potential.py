#/usr/bin/pyython

import sys
import numpy as np
import cdist from  scipy.spatial.distance

def main():
    infile = sys.argv[1]
    readin = open(infile, 'r')

    numat = int(readin.readline())
    readin.readline()

    lattice = np.array([readin.readlines()])    

    r_m=2
    eps=10

    for i in range(numat):
        r = cdist(R,np.array(lattice[i])).flatten()
        r = r[np.nonzero(r)]
        V = eps*((r_m/r)**12 - 2*(r_m/r)**6)
        ETOT += np.sum(V)
    E = ETOT/(numat)
    print E

main()
