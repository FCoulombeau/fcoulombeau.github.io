# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:12:25 2021

@author: François Coulombeau
"""

# Q1
cubes = [k**3 for k in range(30)]

# Q2
def div11(n):
    s = 0
    i = 1
    for k in str(abs(n))[-1::-1]:
        k = int(k)
        s = s+ i*k
        i = -i
    return s

# Q3
def myst(n):
    res = str(div11(n))
    while len(res)>1:
        res = str(div11(int(res)))
    return int(res)

# Q4
print([myst(k) for k in cubes])

# Q5
def her(n):
    u = 1
    for i in range(n):
        u = (u+3/u)/2
    return u

# Q6
print(her(10),3**0.5)

# Q7
import numpy as np

# Q8
def somme(n):
    u=0
    i=0
    s=0
    while i<n:
        s = s+(-1)**i*u
        i += 1
        u = np.exp(-u)/i
    return s

# Q9
print(somme(50))
print(somme(100))
# La somme semble converger.

# Q10
def diamond(n):
    print(n*' '+'*')
    for k in range(1,n+1):
        print((n-k)*' '+'*'+(2*k-1)*' '+'*')
    for k in range(n-1,0,-1):
        print((n-k)*' '+'*'+(2*k-1)*' '+'*')
    print(n*' '+'*')

# Q11
diamond(3)
diamond(4)