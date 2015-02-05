#/usr/bin/pyython

import os
import sys
import numpy as np
from scipy.constants import codata

def main():
    E_g = 2.0 #Fermi energy in eV
    k = float(codata.value('Boltzmann constant in eV/K'))
    T = float(sys.argv[1])

    output = open('PE_' + str(int(T)),'w')

    eV_i = 1.5
    eV_f = 2.5
 
    E = eV_i

    while E <= eV_f:
        P = 1/(np.exp((E - E_g)/(k*T)) + 1)
        output.write(str(E) + ' ' + str(P) + '\n')
        E += 0.05

    output.close()
main()
