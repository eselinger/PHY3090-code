#/usr/bin/python

import sys
import numpy as np

def main():
    bl = sys.argv[1]
    numcells = int(sys.argv[2])

    lattice = []
    a = 1

    if bl=='sc':
        basis = np.array([0,0,0])
        a1 = np.array([a,0,0])
        a2 = np.array([0,a,0])
        a3 = np.array([0,0,a])

    lattice0 = []

#going to do for loops in each direction using basis atoms
    for z in range(numcells): #place atoms in z
        for i in range(len(basis)):
            atom = basis[i] + a3*z
            lattice0.append(atom)
            lattice.append(atom)
    print lattice0

    lattice1 = []

    for y in range(numcells):
        for j in range(len(lattice0)):
            atom = lattice0[j] + a2*y
            lattice1.append(atom)
            lattice.append(atom)
    print lattice1

    for x in range(numcells): #repeat all atoms in x
        for k in range(len(lattice0) + len(lattice1)):
            atom = lattice[k] + a1*x
            lattice.append(atom)

    output = open('bravais_lattice.xyz', 'w')
    output.write(str(len(lattice)) + '\n \n')
   
    for a in range(len(lattice)):
        for element in lattice[a]: output.write(X + '     ' + str(element) + '     ')
        output.write('\n')

    output.close()

main()
