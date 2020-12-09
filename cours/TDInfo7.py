# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:01:49 2020

@author: François Coulombeau
"""

# 1.
def decimal(L):
    L2 = [L[-k-1]*2**k for k in range(len(L))]
    return sum(L2)

# 2.
print(decimal([1,0,0,1,1]))
print(decimal([1,0,1,0,0]))

# 3.
# 107 = 2*53+1
#     = 2*(2*26+1) +1
#     = 2*(2*2*13+1) +1
#     = 2*(2*2*(2*6+1) +1) +1
#     = 2*(2*2*(2*2*(2+1) +1) +1) +1
# Donc 107 = 1101011
print(decimal([1,1,0,1,0,1,1]))

# 4.
def binaire(n):
    if n<0:
        return
    L=[n%2]
    n=n//2
    while n>0:
        L.append(n%2)
        n=n//2
    return L
print(binaire(107))

# 5.
# a)
def dicho(f,a,b,epsilon):
    assert f(a)*f(b)<=0 and epsilon>0
    c=(b-a)/2
    while abs(c)>epsilon:
        if f(a+c)*f(a)>0:
            a=a+c
            c=c/2
        else:
            b=a+c
            c=c/2
    if abs(f(a))<abs(f(b)):
        return a
    else:
        return b

# b)
r2=dicho(lambda x:x**2-2,1,2,1e-7)

# c)
print(r2,abs(r2-2**0.5))

# d)
r2=dicho(lambda x:x**2-2,1,2,1e-16)
print(r2,abs(r2-2**0.5))
r3=dicho(lambda x:x**2-3,1,2,1e-15)
print(r3,abs(r3-3**0.5))
r5=dicho(lambda x:x**2-5,2,3,1e-15)
print(r5,abs(r5-5**0.5))
r1000=dicho(lambda x:x**2-1000,30,40,1e-15)
print(r1000,abs(r1000-1000**0.5))
r10001=dicho(lambda x:x**2-10001,100,101,1e-15)
print(r10001,abs(r10001-10001**0.5))