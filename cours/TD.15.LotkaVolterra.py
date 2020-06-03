# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:51:34 2020

@author: François Coulombeau
"""

import numpy as np
import matplotlib.pyplot as plt

def suivant(x,y,dt,a,b,c,d):
    derx = x*(a-b*y)
    dery = y*(c*x-d)
    nx = x+derx*dt
    ny = y+dery*dt
    return (nx,ny)

def simulation(x,y,dt,a,b,c,d,N):
    Lx = [x]
    Ly = [y]
    for k in range(N):
        x,y = suivant(x,y,dt,a,b,c,d)
        Lx.append(x)
        Ly.append(y)
    return Lx,Ly

a=1
b=0.045
d=1
c=0.045

y = 22
x = 22

dt=1/3650
N = 100*3650

Lx,Ly = simulation(x,y,dt,a,b,c,d,N)

T = np.linspace(0,N*dt,N+1)

plt.plot(T,Lx)
plt.plot(T,Ly)
plt.figure()
plt.plot(Lx,Ly)

def suivant2(x1,x2,y1,y2,dt,a,b,c,d):
    derx1 = x1*(a-b*y1)
    dery1 = y1*(b*x1-c)-d*y1+d*y2
    derx2 = x2*(a-b*y2)
    dery2 = y2*(b*x2-c)-d*y2+d*y1
    nx1 = x1+derx1*dt
    ny1 = y1+dery1*dt
    nx2 = x2+derx2*dt
    ny2 = y2+dery2*dt
    return (nx1,nx2,ny1,ny2)

def simulation2(x1,x2,y1,y2,dt,a,b,c,d,N):
    Lx = [x1+x2]
    Ly = [y1+y2]
    for k in range(N):
        x1,x2,y1,y2 = suivant2(x1,x2,y1,y2,dt,a,b,c,d)
        Lx.append(x1+x2)
        Ly.append(y1+y2)
    return Lx,Ly

a=1.1
b=0.05
c=1.1
d=0.012
plt.figure()
# Deux graphiques dans une même fenêtre
# 121 : 1 ligne de graphiques, 2 colonnes, 1er graphique
plt.subplot('121')
y1 = 24
y2 = 20
x1 = 20
x2 = 24
dt = 1/100
N = 60*100

Lx,Ly = simulation2(x1,x2,y1,y2,dt,a,b,c,d,N)

T = np.linspace(0,N*dt,N+1)

plt.plot(T,Lx)
plt.plot(T,Ly)
# 121 : 1 ligne de graphiques, 2 colonnes, 2ème graphique
plt.subplot('122')
plt.plot(Lx,Ly)