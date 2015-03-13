#/usr/bin/python

import sys
import numpy as np

def main():
    a = 1.

    basis = np.array([[0.,0.]])
    a1 = np.array([a, 0.])
    a2 = np.array([0., a])

    lattice = []

    for i in range(len(basis)):
        for y in range(10):
            for x in range(10):
                R = x*a1 + y*a2 + basis[i]

                if R[0] <= (10-1.):
                    if R[1] <= (10-1.):
                        lattice.append(R)

    output = open('2dlatt.xyz', 'w')
    output.write(str(int(len(lattice))) + '\n \n')

    for j in range(len(lattice)):
        a = lattice[j]
        output.write('X ' + ' ' + str(a[0]) + ' ' + str(a[1]) + ' ' + '0.000' + '\n')

    output.close()

if __name__ == '__main__':
    main()
