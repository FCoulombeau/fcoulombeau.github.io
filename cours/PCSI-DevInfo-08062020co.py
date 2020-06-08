# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:59:23 2017

@author: FC
"""

# Questions 6/7
import random as rd
def init(n):
    M=[]
    for i in range(n):
        L=[0 for k in range(n)]
        M.append(L)
    i,j=rd.randrange(n),rd.randrange(n)
    M[i][j]=1
    return M

# Question 8
def compte(G):
    n0,n1,n2,n3=0,0,0,0
    n=len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j]==0:
                n0+=1
            elif G[i][j]==1:
                n1+=1
            elif G[i][j]==2:
                n2+=1
            else:
                n3+=1
    return [n0,n1,n2,n3]

# Question 10
def est_exposee(G,i,j):
    voisins=[[k,l] for l in range(-1,2) for k in range(-1,2) if j!=0 or k!=0]
    n=len(G)
    b=False
    for c in voisins:
        if 0<=i+c[0]<n and 0<=j+c[1]<n:
            b=b or G[i+c[0]][j+c[1]]==1
    return b

# Question 12
def bernoulli(p):
    x=rd.random()
    if x<=p:
        return 1
    return 0
    
def suivant(G,p1,p2):
    n=len(G)
    H=[[0 for k in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]==0:
                if est_exposee(G,i,j):
                    H[i][j]=bernoulli(p2)
            elif G[i][j]==1:
                H[i][j]=2+bernoulli(p1)
            elif G[i][j]==2:
                H[i][j]=2
            else:
                H[i][j]=3
    return H

# Question 13
def simulation(n,p1,p2):
    G=init(n)
    n1=1
    pas=0
    while n1>0:
        G=suivant(G,p1,p2)
        n0,n1,n2,n3=compte(G)
        pas+=1
    return n0/n**2,0,n2/n**2,n3/n**2,pas
    
# Bonus : simulation video
import moviepy.editor as mpy
import matplotlib.pyplot as plt
import numpy as np

def simulvideo(n,p1,p2,p3,filename):
    G=init_vac(n,p3)
    pas=0
    ima=np.array(G,dtype=np.uint8)
    plt.imsave('./temp/image'+format(pas,'04d')+'.jpg',ima)
    ims=['./temp/image'+format(pas,'04d')+'.jpg']
    n1=1
    while n1>0:
        G=suivant(G,p1,p2)
        n0,n1,n2,n3=compte(G)
        pas+=1
        ima=np.array(G,dtype=np.uint8)
        plt.imsave('./temp/image'+format(pas,'04d')+'.jpg',ima)
        ims.append('./temp/image'+format(pas,'04d')+'.jpg')
    vid=mpy.ImageSequenceClip(ims,fps=20)
    vid.write_videofile(filename,fps=20,codec='mpeg4')
    return n0/n**2,0,n2/n**2,n3/n**2,pas

def init_vac(n,q):
	G = init(n)
	nvac = int(q*n**2)
	k = 0
	while k < nvac:
		i = rd.randrange(n)
		j = rd.randrange(n)
		if G[i][j] == 0:
			G[i][j] = 2
			k += 1
	return G

print(simulvideo(500,0.5,0.36,0.147,'contagionVac.mp4'))