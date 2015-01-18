#/usr/bin/python

import sys
import numpy as np

def main():
    bl = sys.argv[1]
    n1 = int(sys.argv[2])+1
    n2 = int(sys.argv[3])+1
    n3 = int(sys.argv[4])+1

    a = 1.
    b = 2.
    c = 3.

    A = np.deg2rad(90) #alpha
    B = np.deg2rad(80) #beta
    Y = np.deg2rad(90) #gamma

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

    if bl=='st':
#        if c==a: print "ERROR: Result is a simple cubic. Must specify c for a simple tetragonal."
        basis = np.array([[0., 0., 0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., c])

    if bl=='bct':
#        if c==a: print "ERROR: Result is a body-centered cubic. Must specificy c for body-centered tetragonal."
        basis = np.array([[0., 0., 0.],[a*0.5, a*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., a, 0.])
        a3 = np.array([0., 0., c])

    if bl=='so':
        basis = np.array([[0.,0.,0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='bco':
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='eco':
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, 0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='fco':
        basis = np.array([[0., 0., 0.],[a*0.5, b*0.5, 0.],[a*0.5, 0., c*0.5],[0., b*0.5, c*0.5]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., 0., c])

    if bl=='sm':
        basis = np.array([[0.,0.,0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        if B > np.pi:
            a3 = np.array([0., -np.absolute(np.tan((np.pi/2)-B)), c])

    if bl=='ecm':
        basis = np.array([[0.,0.,0.],[a*0.5, b*0.5, 0.]])
        a1 = np.array([a, 0., 0.])
        a2 = np.array([0., b, 0.])
        a3 = np.array([0., -np.absolute(np.tan((np.pi/2)-B)), c])


    lattice = []

    for i in range(len(basis)):
        for z in range(n3):
            for y in range(n2):
                for x in range(n1):
                    R = x*a1 + y*a2 + z*a3 + basis[i]

                    if R[0] <= (n1-1.)*a:
                        if R[1] <= (n2-1.)*b:
                            if R[2] <= (n3-1.)*c:
                                lattice.append(R)

    output = open(str(sys.argv[1]) + '.xyz', 'w')
    output.write(str(int(len(lattice))) + '\n \n')

    for j in range(len(lattice)):
        a = lattice[j]
        output.write('X ' + ' ' + str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + '\n')

    output.close()

main()
