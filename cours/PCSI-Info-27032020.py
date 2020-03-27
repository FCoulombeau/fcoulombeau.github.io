# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:31:35 2016

@author: FC
"""

import numpy as np
import matplotlib.pyplot as plt

# TD n°1

def fraction_continue(x,n=5):
    """Renvoie une fraction proche de x.
    x doit etre de type float, la valeur de retour est un couple d'int.
    n est un parametre optionnel de type int
    permettant d'ameliorer la precision de l'approximation rationnelle.
    """
    i=0
    l=[]
    while i<n:
        l=[int(np.floor(x))]+l
        if abs(x-l[0])<1e-7:
            break
        x=1/(x-l[0])
        i+=1
    p,q=l[0],1
    for i in range(len(l)-1):
        p,q=p*l[i+1]+q,p
    return (p,q)
def frac_pi(alpha):
    """Renvoie une chaine de caractères correspondant à la représentation de
    alpha comme fraction de Pi"""
    p,q=fraction_continue(alpha/np.pi)
    if abs(p)==1:
        if p>0:
            s="Pi"
        else:
            s="-Pi"
        if q==1:
            return s
        else:
            return s+"/"+str(q)
    else:
        if q==1:
            return str(p)+"*Pi"
        else:
            return str(p)+"*Pi/"+str(q)
            

def FrotLin(a,v0,alpha,dt=0.001):
    X=[0]
    Y=[0]
    t=0
    g=10
    while Y[-1]>=0:
        t=t+dt
        X.append(v0*np.cos(a)/alpha*(1-np.exp(-alpha*t)))
        Y.append((v0*np.sin(a)*alpha+g)/alpha**2*(1-np.exp(-alpha*t))-g*t/alpha)
    return X,Y

v0=30
alpha=0.1
plt.plot(*FrotLin(np.pi/4,v0,alpha))
plt.plot(*FrotLin(np.pi/3,v0,alpha))
plt.plot(*FrotLin(np.pi/6,v0,alpha))

def AngleOptimal(v0,alpha,da=np.pi/180):
    maxdist=0
    aopt=0
    a=da
    while a<np.pi/2:
        X,Y=FrotLin(a,v0,alpha)
        if X[-1]>maxdist:
            aopt=a
            maxdist=X[-1]
        a+=da
    return aopt,maxdist
a,d=AngleOptimal(v0,alpha)
print(frac_pi(a),d)
plt.plot(*FrotLin(a,v0,alpha))
plt.axis('scaled')
plt.title('Trajectoires théoriques\nFrottements linéaires\nAngles : 30°, 45°, 60° et optimal')
plt.legend(['45°','60°','30°','Distance max'])
plt.figure()

# TD n°2

def FrotLin2(a,v0,alpha,dt=0.001):
    X=[0]
    Y=[0]
    vx=[v0*np.cos(a)]
    vy=[v0*np.sin(a)]
    g=10
    while Y[-1]>=0:
        X.append(X[-1]+vx[-1]*dt)
        Y.append(Y[-1]+vy[-1]*dt)
        vx.append(vx[-1]-alpha*vx[-1]*dt)
        vy.append(vy[-1]-alpha*vy[-1]*dt-g*dt)
    return X,Y

v0=30
alpha=0.1
plt.plot(*FrotLin(np.pi/4,v0,alpha))
plt.plot(*FrotLin2(np.pi/4,v0,alpha,dt=0.001))
plt.title('Trajectoires théoriques et numériques\nFrottements linéaires')
plt.legend(['Théorique','Méthode d\'Euler'])
plt.axis('scaled')

def AngleOptimal2(v0,alpha,da=np.pi/180,dt=0.001):
    maxdist=0
    aopt=0
    a=da
    while a<np.pi/2:
        X,Y=FrotLin2(a,v0,alpha,dt=dt)
        if X[-1]>maxdist:
            aopt=a
            maxdist=X[-1]
        a+=da
    return aopt,maxdist
a,d=AngleOptimal(v0,alpha)
print("Avec la primitivation théorique :",frac_pi(a),d)
a,d=AngleOptimal2(v0,alpha)
print("Avec la méthode d'Euler :",frac_pi(a),d)

def FrotNonLin(a,v0,alpha,beta,dt=0.001):
    X=[0]
    Y=[0]
    vx=[v0*np.cos(a)]
    vy=[v0*np.sin(a)]
    g=10
    while Y[-1]>=0:
        X.append(X[-1]+vx[-1]*dt)
        Y.append(Y[-1]+vy[-1]*dt)
        v=(vx[-1]**2+vy[-1]**2)**0.5
        vx.append(vx[-1]-alpha*vx[-1]*dt-beta*vx[-1]*v*dt)
        vy.append(vy[-1]-alpha*vy[-1]*dt-beta*vy[-1]*v*dt-g*dt)
    return X,Y

plt.figure()
v0=60
alpha=0.1
beta=0.0015
plt.plot(*FrotLin2(np.pi/4,v0,alpha,dt=0.001))
plt.plot(*FrotNonLin(np.pi/4,v0,alpha,beta,dt=0.001))

def AngleOptimal3(v0,alpha,beta,da=np.pi/180,dt=0.001):
    maxdist=0
    aopt=0
    a=da
    while a<np.pi/2:
        X,Y=FrotNonLin(a,v0,alpha,beta,dt=dt)
        if X[-1]>maxdist:
            aopt=a
            maxdist=X[-1]
        a+=da
    return aopt,maxdist

a,d=AngleOptimal3(v0,alpha,beta)
plt.plot(*FrotNonLin(a,v0,alpha,beta,dt=0.001))
plt.axis('scaled')
plt.title('Trajectoire numérique\nFrottements non linéaires et linéaires\nAngles : 45° et optimal')
plt.legend(['Frottements linéaires','Frottements non linéaires 45°','Non linéaires, distance max'])