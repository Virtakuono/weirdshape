#!/usr/bin/python

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


centerPoints = []

for c1 in (-1,1):
    centerPoints.append(np.array([c1,0,0]))
    centerPoints.append(np.array([0,c1,0]))
    centerPoints.append(np.array([0,0,c1]))

cCoef = (2*np.sqrt(3)-2)/(np.sqrt(3)+1)
edges = []

rm1 = np.array([[0,1,0],[0,0,1],[1,0,0]])
rm2 = np.dot(rm1,rm1)

for ii in range(len(centerPoints)):
    cp = centerPoints[ii]
    v1 = cCoef*np.dot(rm1,cp)
    v2 = cCoef*np.dot(rm2,cp)
    for jj in range(12):
        p1 = cp+np.sin(((2*np.pi*jj)/12))*v1+np.cos(((2*np.pi*jj)/12))*v2
        p2 = cp+np.sin(((2*np.pi*(jj+1))/12))*v1+np.cos(((2*np.pi*(jj+1))/12))*v2
        edges.append((np.zeros(3),p1))
        edges.append((p1,2*cp))
        edges.append((p1,p2))

for c1 in (-1,1):
    for c2 in (-1,1):
        for c3 in (-1,1):
            centerPoints.append((1.0/np.sqrt(3))*np.array([c1,c2,c3]))
            cp = centerPoints[-1]
            v1 = np.array([-0.5*c1,-0.5*c2,c3])/np.sqrt(1.5)*cCoef
            v2 = np.cross(cp,v1)
            for jj in range(12):
                p1 = cp+np.sin(((2*np.pi*(0.5+jj))/12))*v1+np.cos(((2*np.pi*(jj+0.5))/12))*v2
                p2 = cp+np.sin(((2*np.pi*(jj+1.5))/12))*v1+np.cos(((2*np.pi*(jj+1.5))/12))*v2
                edges.append((np.zeros(3),p1))
                edges.append((p1,p2))
                edges.append((p1,2*cp))

fig = plt.figure()
ax = fig.gca(projection='3d')
lines = ['#x1\ty1\tz1\tx2\ty2\tz2\n']
for edge in edges:
    ax.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],[edge[0][2],edge[1][2]],'b-')
    lines.append('%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\n'%(edge[0][0],edge[0][1],edge[0][2],edge[1][0],edge[1][1],edge[1][2]))

f = open('weirdshape.txt','w')
f.writelines(lines)
f.close()

plt.title('George\'s weird construction')

plt.show()
