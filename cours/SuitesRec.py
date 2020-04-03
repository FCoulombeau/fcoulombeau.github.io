# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:40:35 2020

@author: François Coulombeau
"""

import numpy as np
import matplotlib.pyplot as plt


# Modéfier les lignes suivantes 
xmin = -2
xmax = 3
f=lambda x:x**2/4+1
x0 = -1/2
nbtermes = 7

# La suite est automatique
X=np.linspace(xmin,xmax,500)
Y=f(X)
ymin = min(Y)
ymax = max(Y)
plt.plot(X,Y,'k')
X=np.linspace(max(xmin,ymin),min(xmax,ymax),500)
plt.plot(X,X,':k')
plt.axis('scaled')
X=[x0]
Y=[0]
for i in range(nbtermes):
    X.append(X[-1])
    Y.append(f(X[-1]))
    X.append(Y[-1])
    Y.append(Y[-1])
plt.plot(X,Y)
plt.title('Si $x_0='+str(x0)+'$')