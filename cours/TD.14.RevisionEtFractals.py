# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:45:39 2020

@author: François Coulombeau
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Suites récurrentes
# Q1
def A(n):
    res = 2
    i = 0
    while i<n:
        res = 1-np.exp(res)
        i += 1
    return res

# Q2
def lstA(n):
    res = [2]
    i = 0
    while i<n:
        res.append(1-np.exp(res[-1]))
        i += 1
    return res

# Q3
N = 100
lst = lstA(N)
plt.plot(range(N+1),lst,'+')

# Q4
def BC(n):
    B = 0
    C = 1
    i = 0
    while i<n:
        D = -B + C/2
        C = B - C
        B = D
        i += 1
    return (B,C)

# Q5
def lstBC(n):
    res = [(0,1)]
    B = 0
    C = 1
    i = 0
    while i<n:
        D = -B + C/2
        C = B - C
        B = D
        res.append((B,C))
        i += 1
    return res

# Q6
plt.figure()
N = 10
lst = lstBC(N)
plt.plot(range(N+1),[k[0] for k in lst],'+')
plt.plot(range(N+1),[k[1] for k in lst],'o')

# Q7
def lstBC(n):
    res = [(0,1)]
    B = 0
    C = 1
    i = 0
    while i<n:
        B = -B + C/2
        C = B - C
        res.append((B,C))
        i += 1
    return res

plt.figure()
N = 1000
lst = lstBC(N)
plt.plot(range(N+1),[k[0] for k in lst],'+')
plt.plot(range(N+1),[k[1] for k in lst],'o')

# 2. Equations différentielles
# Q1
def euler(y0,T,dt=1e-2):
    y = y0
    t = 0
    res = [y0]
    while t<T:
        y = y + dt*(y**2+y-np.cos(y))
        res.append(y)
        t += dt
    return res

# Q2
plt.figure()
Y = euler(0.55000934993,10,dt=1e-3)
T = np.linspace(0,10,len(Y))
plt.plot(T,Y)

# Q3
def eulerXYZ(V0,T,dt=1e-2):
    x,y,z = V0
    t = 0
    res = [V0]
    while t<T:
        xx = x + dt*(-y-z)
        yy = y + dt*(x+0.2*y)
        z  = z + dt*(0.1+z*(x-5.7))
        x = xx
        y = yy
        res.append((x,y,z))
        t += dt
    return res

# Q4
plt.figure()
Sol = eulerXYZ((-10,0,0),100,dt=1e-2)
X = [k[0] for k in Sol]
Y = [k[1] for k in Sol]
plt.plot(X,Y)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [k[0] for k in Sol]
Y = [k[1] for k in Sol]
Z = [k[2] for k in Sol]
plt.plot(X,Y,Z)

# 3. Méthode de Newton et fractals
# Methode de Newton appliquee a la fonction
# z->z**3-1
def suite(u,prec = 1e-3):
    n=0
    v=10
    g = lambda z:2*z**3+1
    h = lambda z:3*z**2
    # pour la deuxième question, décommenter les 2 lignes suivantes
    # g = lambda z:3*z**3+z**2+z+1
    # h = lambda z:4*z**2+z+1
    while n<=40 and h(u)!=0 and abs(v-u)>prec:
        v=u
        u = g(u)/h(u)
        n+=1
    return u,n

# On trace une image dont la couleur des points
# indique la racine cubique de l'unite vers laquelle
# a converge la suite, lorsqu'elle converge.
# Si elle ne converge pas, on trace le point en noir.
# Si elle converge vers 1, on trace le point en rouge.
# Si elle converge vers exp(2iPi/3), on trace le point en bleu.
# Si elle converge vers exp(-2iPi/3), on trace le point en vert.
# Lorsqu'elle converge, le point sera d'autant plus lumineux que
# la suite a converge rapidement.

# Taille de l'image
# Pour Taille=1000, l'image met environ une minute
# a etre calculee sur mon ordinateur.
Taille=1000
# Creation de l'image sous forme d'un tableau de pixels
image=np.ndarray((Taille,Taille,3),np.uint8)
# On parcourt les lignes (i) et les colonnes (j)
for i in range(Taille):
    for j in range(Taille):
        # On calcule abscisse et ordonnee
        x=-1+2*j/(Taille-1)
        y=1-2*i/(Taille-1)
        # On calcule l'affixe
        z=x+y*1.j
        # On initialise le point en noir
        image[i,j]=[0,0,0]
        # On calcule la valeur de suite(z) et
        # on compare aux racines cubiques de
        # l'unite
        u,n=suite(z)
        if np.abs(u-1)<=0.01:
            image[i,j,0]=255-3*n
        if np.abs(u-(-0.5+0.8660254037844387j))<=0.01:
            image[i,j,1]=255-3*n
        if np.abs(u-(-0.5-0.8660254037844387j))<=0.01:
            image[i,j,2]=255-3*n

# L'image est calculee : on l'affiche
plt.figure()
plt.imshow(image)
