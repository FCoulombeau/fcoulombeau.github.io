# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:05:11 2020

@author: François Coulombeau
"""

import time as t

depart = partiel = t.time()
i=0
print('0:00',sep='',end='')
NbMinutes = 2

while t.time()-depart<=2*60:
    if t.time()-partiel>1:
        partiel = t.time()
        i= i+1
        secondes = i%60
        minutes = i//60
        chiffreUniteSecondes = (secondes%10)
        chiffreDizaineSecondes = (secondes//10)
        print('\b\b\b\b',
              minutes,
              ":",
              chiffreDizaineSecondes,
              chiffreUniteSecondes,
              sep='',end='')
        