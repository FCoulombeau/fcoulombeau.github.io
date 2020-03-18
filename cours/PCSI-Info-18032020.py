# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:03:40 2020

@author: François Coulombeau
"""
# Q1
def estPremier(n):
    """Renvoie True si n est premier, False sinon."""
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False
# Q2    
def listePremiers(a,b):
    """Renvoie tous les nombres premiers entre a et b-1 (inclus)"""
    res = []
    for i in range(a,b):
        if not estPremier(i):
            continue
        res.append(i)
    return res
# Q3
# a)
def facteursPremiers(n):
    """Renvoie la liste des (p,a) tels que n est le produit des p**a
    où p sont les facteurs premiers de n
    L'idée : 
    on pose p=2
    1.Tant qu'on peut diviser n par p, on le fait et on incrémente de 1 la valeur
    de l'exposant
    2.Quand on ne peut plus, on augmente p de 1, et on réinitialise l'exposant à 0
    3.On recommence l'étape 1 jusqu'à ce que n==1 (quand n ==1, on a trouvé tous
    les facteurs premiers)
    Evidemment, il faut stocker les résultats intermédiaires ;-)
    """
    L=[]
    p=1
    a=0
    for i in range (n):
        a=0
        p=p+1
        while n%p==0:
           a=a+1
           n=n//p
        if a>0:
            L.append([p,a])
    return L

def decomp(n):
    res = []
    l=[];expo=[];a=1
    for p in range(2,n+1):
        i=0
        while estPremier(p) and n%(p**i)==0:
            i+=1
        if estPremier(p) and i-1:    
            l.append(p);expo.append(i-1)
            res.append((p,i-1))
            a=a*p**(i-1)
        if a==n:
            break
    return res
# b)
def f(n):
    """On décompose n comme produit de facteurs premiers :
        n = p1**a1*p2**a2*...*pk**ak
    On renvoie f(n)= a1**p1*a2**p2*...*ak**pk"""
    p=1;a=decomp(n)
    for i in range(len(a)):
        p=p*(a[i][1])**(a[i][0])
    return p

# Q4
def demandeEntiers():
    """Demande à l'utilisateur de rentrer deux entiers
    le premier >=2
    le deuxième positif
    Recommence tant que ce n'est pas le cas."""
    i=0;k=-1
    while i<2 or (not isinstance(i,int)):
        try:
            i=int(input("Nombre >= à 2 svp: "))
        except Exception:
            print("Erreur : un entier !")
    while k<0 or (not isinstance(k,int)):
        try:
            k=int(input("Nombre >=0 svp: "))
        except Exception:
            print("Erreur : un entier !")
    return i,k
    
def SuiteU():
    """Demande 2 entiers (n,i) où n>=2, i>=0
    et calcule la valeur de u_i où u est définie par
    u_0 = n
    u_(k+1) = f(u_k)  <<< c'est pas un mauvais jeu de mots ;-)"""
    n,i=demandeEntiers()
    u0=n
    for k in range(i):
        u0=f(u0)
        print(u0)
    return u0


# Remarque :
# a = input('Question à poser')
# effectue les choses suivantes :
# 1. Affiche le message (ici 'Question à poser') donné en paramètre
# 2. Attend que l'utilisateur écrive la réponse et appuie sur Entrée
# 3. affecte la chaîne de caractères tapée par l'utilisateur à la
#    variable a

L1 = []
L2 = []
for i in range(50):
    L1.append(1)
    L2 = L2+[1]
print(L1,L2)

# time est un module qui permet de gérer le temps en Python
import time as t

L1 = []
T=t.process_time()
for i in range(100000):
    L1.append(1)
print(t.process_time()-T)

# Prend beaucoup plus de temps !
# Décommenter pour tester
# L1 = []
# T=t.process_time()
# for i in range(100000):
#     L1 = L1+[1]
# print(t.process_time()-T)

A = [1,2,3,4]
B = A
C = A[:]
A[0] = 5
print(A,B,C)

A = [1,2,3,4]
import numpy as np

A = np.array(A)
B = A
C = A[:]
D = np.copy(A)
A[0] = 5
print(A,B,C,D)
