# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:18:33 2020

@author: François Coulombeau
"""

import time as t

# Exo 1
def exo1(a,n):
    r=a
    for k in range(a-1):
        r=r*a
        r=r%10**n
    return r

T0 = t.process_time()
exo1(1234567,2)
print(t.process_time()-T0)

T0 = t.process_time()
exo1(12345678,2)
print(t.process_time()-T0)

def exo1(a,n):
    r = 1
    p = a
    md = 10**n
    while a>0:
        if a%2 == 1 :
            r = (r*p)% md
        a = a//2
        p = (p*p) % md
    return r


T0 = t.process_time()
exo1(1234567,2)
print(t.process_time()-T0)

T0 = t.process_time()
exo1(123456789,2)
print(t.process_time()-T0)





# Exo 2
def somme1(T):
    n = T.shape[0]
    S = 0
    for i in range(n):
        for j in range(n):
            S += T[i,j]
    return S

def somme2(L):
    n = len(L)
    S = 0
    for i in range(n):
        S += L[i][2]
    return S