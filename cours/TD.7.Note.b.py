# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:12:25 2021

@author: François Coulombeau
"""

# Q1
carres = [k**2 for k in range(30)]

# Q2
def som(n):
    s = 0
    for k in str(abs(n)):
        k = int(k)
        s = s + k
    return s

# Q3
def myst(n):
    res = str(som(n))
    while len(res)>1:
        res = str(som(int(res)))
    return int(res)

# Q4
print([myst(k) for k in carres ])

# Q5
def suite(n):
    u = 1
    for i in range(n):
        u = (u-2/u)/2
    return u

# Q6
print([suite(k) for k in range(20)])
# La suite ne semble pas converger.

# Q7
def moyenne(n):
    i=0
    s=0
    while i<n:
        s = s+suite(i)
        i += 1
    return s/n

# Q8
print(moyenne(400))
print(moyenne(500))
print(moyenne(600))
# La moyenne des termes de la suite ne semble pas non plus converger.

# Q9
def sapin(n):
    print(n*' '+'*')
    for k in range(1,n):
        print((n-k)*' '+(2*k+1)*'*')
        print((n-k)*' '+(2*k+1)*'*')
    print((2*n+1)*'*')
    print(n*' '+'*')
    
# Q10
sapin(3)
sapin(8)