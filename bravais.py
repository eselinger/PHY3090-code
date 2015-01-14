#/usr/bin/python

import sys
import numpy as np

def main():
    bl = sys.argv[1]
    numcells = int(sys.argv[2])

    lattice = []
    a = 1

    if bl=='sc':
        numat = numcells* #give total number of atoms from type of BL and # unit cells
        basis = np.array([0,0,0])
        a1 = [a,0,0]
        a2 = [0,a,0]
        a3 = [0,0,a]

        lattice.append(basis)

#oing to do for loops in each direction using basis atoms
    for i in range(numcells): #place atoms in z
        atom = basis + a3
        basis = np.array(atom)
        lattice.append(atom)

    for j in range(numcells):

                #repeat all atoms in y direction
    for k in range(numcells): #repeat all atoms in x

        lattice.append(atom)

    output = open('bravais_lattice.xyz', 'w')
    output.write(str(numat) + '\n \n')
