#/usr/bin/python

import os, sys
import numpy as np

#system parameters
k = 1.
m = 1.
r0 = 2.
steps = 10000
dt = 0.001

#initial conditions
#

def lattice(n): #n number of columns/rows
    basis = np.array([[0.,0.]])
    a1 = np.array([1, 0.])
    a2 = np.array([0., 1])

    lattice = []

    for i in range(len(basis)):
        for y in range(n):
            for x in range(n):
                R = x*a1 + y*a2 + basis[i]

                if R[0] <= (10-1.):
                    if R[1] <= (10-1.):
                        lattice.append(R)

    return lattice

def dist(a,b):
    """
    Returns the distance between two vectors, a and b
    """
    dist = 0.
    for i in range(len(a)):
        dist += (b[i]-a[i])**2.

    dist = dist**.5
    return dist

def F(a,b):

    r = dist(a,b)

    f = -k*(r - r0)
    return f

def move_f(atoms):

    forces = np.zeros((len(atoms),3),dtype=float) # empty forces list
    natoms = len(atoms)

    # Use neighbours on either side to set force. Ends will be wrong (see fix below)
    # note that this assumes the spring is the x direction. No projections are being done!

    for i in range(natoms):
        forces[i][0]  = -F(atoms[i],  atoms[(i+1)%natoms])   # atom to the right
        forces[i][0] += +F(atoms[i-1],atoms[i])              # atom to the left
        forces[i][1] = -F(atoms[i], atoms[(i+n)%natoms])     # atom down
        forces[i][1] += +F(atomes[i-n],atoms[i])            # atom up

    # Deal with the special case of the atoms at either end of the chain
    for i in range(n):
        forces[-n-1] = atoms[-n-1]

    return forces

def move_a(atom_a, atom_f, m):

    natoms = len(atom_a)
    for i in range(natoms):
        atom_a[i] = atom_f[i]/m
    return atom_a


def move_v(atom_v, atom_a, dt):

    natoms = len(atom_v)
    for i in range(natoms):
        atom_v[i] += atom_a[i]*dt
    return atom_v

def move_x(atom_x, atom_v, dt):

    natoms = len(atom_x)
    for i in range(natoms):
        atom_x[i] += atom_v[i]*dt
    return atom_x

def create_arrays(natoms):

    atom_x = np.zeros((natoms,3), dtype=float) # empty list of atoms
    atom_v = np.zeros((natoms,3), dtype=float)
    atom_a = np.zeros((natoms,3), dtype=float)
 
    return atom_x, atom_v, atom_a
 

def main():
    natoms = 10
    atom_x, atom_v, atom_a = create_arrays(natoms)
  
    atom_x = lattice(10.)

    # dynamics
    print '# Note, forces are only updated in x right now'

    for i in range(steps):

        atom_f = move_f(atom_x)  
        atom_a = move_a(atom_a, atom_f, m)
        atom_v = move_v(atom_v, atom_a, dt)
        atom_x = move_x(atom_x, atom_v, dt)

        outstr = ' '
        for i in range(natoms):
            outstr += str(atom_x[i][0]) + ' '
   
        print outstr  


# This executes main() only if executed from shell
if __name__ == '__main__':
    main()

