# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:07:31 2020

@author: François Coulombeau
"""

def essai():
    """Fonction bidon
    Essentiellement, ne fait rien"""
    return

def recherche(liste, valeur):
    """Renvoie l'indice de la première occurence
    de *valeur* dans *liste* (si elle existe)
    
    ou renvoie la longueur de *liste* sinon."""
    for i in range(len(liste)):
        if liste[i]==valeur:
            return i
    return len(liste)

def maximum(liste):
    if liste==[]:
        return None,None
    a=liste[0]
    for i in range(len(liste)):
        if liste[i]>a:
            a=liste[i]
    return (a,recherche(liste,a))

def cherche(chaine,mot):
    for i in range (len(chaine)-len(mot)+1):
        if chaine[i:i+len(mot)]==mot:
            return i
    return len(chaine)


carre = lambda x:x**2
cube = lambda x:x**3
racine = lambda x:x**0.5

def approxDerivee(f,dx):
    fp = lambda x :(f(x + dx)-f(x))/dx
    return fp
approxDerivee2=lambda f,dx:(lambda x:(f(x+dx)-f(x))/dx)


import numpy as np
import matplotlib.pyplot as plt
Dexp = approxDerivee(np.exp,1e-7)
X = np.linspace(-2,2)
Y = []
for x in X:
    Y.append(Dexp(x))
plt.plot(X,Y)
plt.plot(X,np.exp(X))

def exemple():
    x=2
    n=-1
    return (x,n)

x = 3
print(x,exemple())


def initialisation():
    global x,n
    x=1.
    n=0
initialisation()

def XProf(n):
    for i in range(n):
        print(i*' '+'*'+(2*n-1-2*i)*' '+'*')
    print(n*' '+'*')
    for i in range(n-1,-1,-1):
        print(i*' '+'*'+(2*n-1-2*i)*' '+'*')
    
def X(n):
    """Solution de M.Tournaire"""
    for i in range (0,2*n+1):
        for j in range (0,2*n+1):
            if i==j or j==2*n-i:
                print("*",end='')
            else:
                print(" ",end='')
        print()

def A(n):
    """Solution de M.Lasserre"""
    print((2*n)*' '+'*')
    for i in range(1,2*n+1):
        if n==i:
            print(n*' '+(2*n+1)*'*')
        else:
            print((2*n-i)*' '+'*'+(2*i-1)*' '+'*')



