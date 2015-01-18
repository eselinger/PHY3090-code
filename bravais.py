#/usr/bin/python

import sys
import numpy as np

def main():
    bl = sys.argv[1]
    n1 = int(sys.argv[2])+1
    n2 = int(sys.argv[3])+1
    n3 = int(sys.argv[4])+1

    a = 1.

    if bl=='sc':
        b = a
        c = a
        basis = np.array([[0.,0.,0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., a])

    if bl=='bcc':
        b = a
        c = a
        basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, a*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., a])

    if bl=='fcc':
        b = a
        c = a
        basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, 0.],[a*0.5, 0., a*0.5],[0., a*0.5, a*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., a])     

    if bl=='st':
        b = a
        c = 2*a
        basis = np.array([[0., 0., 0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., c])

    if bl=='bct':
        b = a
        c = 3*a
        basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., c])

    if bl=='so':
        b = 2*a
        c = 3*a
        basis = np.array([[0.,0.,0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='bco':
        b = 2*a
        c = 3*a
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='eco':
        b = 2*a
        c = 3*a
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, 0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='fco':
        b = 2*a
        c = 3*a
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, 0.],[a*0.5, 0., c*0.5],[0., b*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])


    lattice = []

    for i in range(len(basis)):
        for z in range(n3):
            for y in range(n2):
                for x in range(n1):
                    R = x*a1 + y*a2 + z*a3 + basis[i]

                    if R[0] <= (n1-1)*a:
                        if R[1] <= (n2-1)*b:
                            if R[2] <= (n3-1)*c:
                                lattice.append(R)

    output = open(str(sys.argv[1]) + '.xyz', 'w')
    output.write(str(int(len(lattice))) + '\n \n')

    for j in range(len(lattice)):
        a = lattice[j]
        output.write('X ' + ' ' + str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + '\n')

    output.close()

main()
