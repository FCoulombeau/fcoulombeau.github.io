# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 05:56:49 2020

@author: François Coulombeau
"""

import numpy as np
import matplotlib.pyplot as plt

A = 1954
B = 600
C = 1790
D = 560
E = 1400
F = 1960
G = 112

def f(theta_m,theta_v):
    return A+B*np.cos(theta_v)+C*np.sin(theta_v)-D*np.cos(theta_m)-E*np.sin(theta_m)\
           -F*np.cos(theta_v-theta_m)-G*np.sin(theta_v-theta_m)

def df(theta_m,theta_v):
    return -B*np.sin(theta_v)+C*np.cos(theta_v)+F*np.sin(theta_v-theta_m)\
           -G*np.cos(theta_v-theta_m)


def newton(theta_m,epsilon=1e-5):
    x=0
    xm=2*epsilon
    while abs(xm-x)>epsilon:
        xm=x
        x = x-f(theta_m,x)/df(theta_m,x)
    return x

ThM = np.linspace(-2.4,0.2,500)
ThV = [newton(k) for k in ThM]
plt.plot(ThM,ThV)


# 1 radian par seconde à raison de 25 images par seconde
dth = 1/25
nbim = int(np.pi/2/dth)
ThM = np.linspace(-np.pi/2,0,nbim)[::-1]
ThV = [newton(k) for k in ThM]

plt.figure()
plt.axis('scaled')
plt.axis([min(0,np.min(np.cos(ThV))),max(0,np.max(np.cos(ThV))),
          min(0,np.min(np.sin(ThV))),max(0,np.max(np.sin(ThV)))])

vantail ,= plt.plot([0,np.cos(ThV[0])],[0,np.sin(ThV[0])])

for k in ThV[1:]:
    plt.pause(1/25)
    vantail.set_data([0,np.cos(k)],[0,np.sin(k)])

for j in range(25):
    plt.pause(1/25)

for k in ThV[-1::-1]:
    plt.pause(1/25)
    vantail.set_data([0,np.cos(k)],[0,np.sin(k)])