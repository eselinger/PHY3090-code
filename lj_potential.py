#/usr/bin/python

import sys
import numpy as np

def main():
    r_m=2
    eps=10

    V = eps*((r_m/r)**12 - 2*(r_m/r)**6)
    ETOT = np.sum(V)
    E = ETOT/#of of atoms

main()
