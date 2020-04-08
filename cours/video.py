# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:47:28 2020

@author: François Coulombeau
"""

import moviepy.editor as mpe
import numpy as np


im =[]
for l in range(500):
    X = np.fromfunction(lambda i,j,k:(k==0)*(i+l)+(k==1)*(j-l)+(k==2)*(i+j)//2//(l+1),(255,255,3),dtype=np.uint8)
    im.append(X)
vid = mpe.ImageSequenceClip(im,fps=25)
vid.write_videofile('essai.mp4',audio=False,codec='libx264',fps=25)