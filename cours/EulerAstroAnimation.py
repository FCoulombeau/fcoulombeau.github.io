# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:14:22 2020

@author: François Coulombeau
"""

import datetime as date
import numpy as np
import matplotlib.pyplot as plt

G = 6.6743e-11

NbJoursTrace = 5
NbJoursSimul = 500
DeltaTParFrame = 1
# DeltaTParFrame = 1/24 
# 1 image = 1h
# 1s d'animation = 1 jour astronomique
# DeltaTParFrame = 1
# 1 image = 1 jour
# 1s d'animation ~ 1 mois astronomique

SolM = 1.9891e30
Solv = np.array([11.69559797,   -9.17424867])
Sol = np.array([0,0])

Mev = np.array([51715.567061538,-8735.47167717])
Me = np.array([9.981599394e8,-5.2636564547e10])
Mea = 1.8313878634560854
MeM = 3.3011e23
MeE = 0.20564

Vv = np.array([4112.709706081,34731.918])
V = np.array([1.07698363527e11,-1.2034680765e10])
Va = 1.3195756496516213
VM = 4.8685e24
VE = 0.00678

Tv = np.array([324.60689824877045,29434.108808025805])
T = np.array([151360430047.16098,0])
Ta = 0.726895356622999
TM = 5.9736e24
TE = 0.01671022

Mav = np.array([-20724.10667360203,15511.883350108248])
Ma = np.array([137312706733.34933,161495528534.79022])
Maa = -2.306017444888871
MaM = 6.4185e23
MaE = 0.09339

Jv = np.array([-9987.275166209147,8510.286997552814])
J = np.array([529989881128.5033,565439713216.703])
Ja = -1.6299106107596426
JM = 1.8986e27
JE = 0.04839

Sv = np.array([-7594.88390455696,5165.561309258631])
S = np.array([868976801781.4513,1218549311665.1877])
Sa = -0.4041376801660269
SM = 4.6846e26
SE = 0.0539

Uv = np.array([-2695.052700740164,-6004.362895244607])
U = np.array([-2661672665454.1055,1305509063809.2822])
Ua = -0.772163876023619
UM = 8.681e25
UE = 0.04726

Nv = np.array([-5230.3848056687975,-1559.5581345922094])
N = np.array([-1248416467144.5132,4299828498072.9155])
Na = -2.306017444888871
NM = 1.0243e26
NE = 0.00859

planetes = ["Soleil", "Mercure", "Vénus", "Terre", "Mars", "Jupiter",
            "Saturne", "Uranus", "Neptune"]
excentricites = [MeE,VE,TE,MaE,JE,SE,UE,NE]

def norm(u):
    return (u[0]**2+u[1]**2)**0.5

objets = [Sol,Me,V,T,Ma,J,S,U,N]
vitesses = [Solv,Mev,Vv,Tv,Mav,Jv,Sv,Uv,Nv]
masses = [SolM,MeM,VM,TM,MaM,JM,SM,UM,NM]

# Tracé des trajectoires des planetes de debut jusqu'à fin
# Périgée de Mercure : 29 juin
# Périgée de Vénus : 3 juin
# Périgée de Mars : 6 octobre
# Périgée de Jupiter : 15 juillet
# Périgée de Saturne : 21 juillet
# Périgée d'Uranus : 31 octobre
# Périgée de Neptune : 11 septembre
obj2 = np.copy(objets)
vit2 = np.copy(vitesses)
pos = np.copy(objets)
vit = np.copy(vitesses)

trajectoires = [([],[]) for j in range(len(objets))]
dt = 3600*24*DeltaTParFrame
today = date.datetime(2020,5,23)
debut = today.toordinal()
fin = debut + NbJoursTrace
T = debut

while T<fin:
    T = T+dt/3600/24
    for k in range(len(objets)):
        P = pos[k]
        Pv = vit[k]
        Posx = trajectoires[k][0]
        Posy = trajectoires[k][1]
        # Pv = Pv-dt*G*SunM/norm(P)**3*P
        for i in range(len(objets)):
            if i!=k:
                Pv = Pv-dt*G*masses[i]/norm(P-pos[i])**3*(P-pos[i])
        P = P+dt*Pv
        obj2[k] = P
        vit2[k] = Pv
        Posx.append(P[0]-obj2[0][0])
        Posy.append(P[1]-obj2[0][1])
    pos = np.copy(obj2)
    vit = np.copy(vit2)
    
debuP = 1
finP = 5
plt.figure()
anim = []
for (Posx,Posy) in trajectoires[debuP:finP]:
    anim.append(plt.plot(Posx,Posy)[0])
plt.legend(planetes[debuP:finP])
anim.append(plt.plot(0,0,'ok')[0])
for (Posx,Posy) in trajectoires[debuP:finP]:
    anim.append(plt.plot(Posx[-1],Posy[-1],'+k')[0])

plt.axis('scaled')
plt.axis([-norm(objets[finP-1]),norm(objets[finP-1]),-norm(objets[finP-1]),norm(objets[finP-1])])

for fin in np.linspace(fin+NbJoursTrace,fin+NbJoursSimul,int((NbJoursSimul-NbJoursTrace)/DeltaTParFrame+1)):
    plt.pause(1/25)
    while T<fin:
        T = T+dt/3600/24
        for k in range(len(objets)):
            P = pos[k]
            Pv = vit[k]
            Posx = trajectoires[k][0]
            Posy = trajectoires[k][1]
            # Pv = Pv-dt*G*SunM/norm(P)**3*P
            for i in range(len(objets)):
                if i!=k:
                    Pv = Pv-dt*G*masses[i]/norm(P-objets[i])**3*(P-objets[i])
            P = P+dt*Pv
            obj2[k] = P
            vit2[k] = Pv
            Posx.append(P[0]-obj2[0][0])
            Posy.append(P[1]-obj2[0][1])
        pos = np.copy(obj2)
        vit = np.copy(vit2)
        k=0
        for (Posx,Posy) in trajectoires[debuP:finP]:
            anim[k].set_data(Posx[-int(NbJoursTrace/DeltaTParFrame):],
                             Posy[-int(NbJoursTrace/DeltaTParFrame):])
            k +=1
        k+=1
        for (Posx,Posy) in trajectoires[debuP:finP]:
            anim[k].set_data(Posx[-1],Posy[-1])
            k+=1