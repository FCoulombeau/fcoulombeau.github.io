# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:31:19 2020

@author: François Coulombeau
"""

import datetime as date
import numpy as np
import matplotlib.pyplot as plt

G = 6.6743e-11

SolM = 1.9891e30
Solv = np.array([-8.75538795, -3.79305189])
Sol = np.array([0,0])

Mev = np.array([51715.567061538,-8735.47167717])
Me = np.array([9.981599394e8,-5.2636564547e10])
Mea = 1.8313878634560854
MeM = 3.3011e23
MeE = 0.20564
MeRev = 87.95565

Vv = np.array([4112.709706081,34731.918])
V = np.array([1.07698363527e11,-1.2034680765e10])
Va = 1.3195756496516213
VM = 4.8685e24
VE = 0.00678
VRev = 224.667

Tv = np.array([324.60689824877045,29434.108808025805])
T = np.array([151360430047.16098,0])
Ta = 0.726895356622999
TM = 5.9736e24
TE = 0.01671022
TRev = 365.256

Mav = np.array([-20724.10667360203,15511.883350108248])
Ma = np.array([137312706733.34933,161495528534.79022])
Maa = -2.306017444888871
MaM = 6.4185e23
MaE = 0.09339
MaRev = 686.885

Jv = np.array([-9987.275166209147,8510.286997552814])
J = np.array([529989881128.5033,565439713216.703])
Ja = -1.6299106107596426
JM = 1.8986e27
JE = 0.04839
JRev = 4332.01

Sv = np.array([-7594.88390455696,5165.561309258631])
S = np.array([868976801781.4513,1218549311665.1877])
Sa = -0.4041376801660269
SM = 4.6846e26
SE = 0.0539
SRev = 10754

Uv = np.array([-2695.052700740164,-6004.362895244607])
U = np.array([-2661672665454.1055,1305509063809.2822])
Ua = -0.772163876023619
UM = 8.681e25
UE = 0.04726
URev = 30698

Nv = np.array([-5230.3848056687975,-1559.5581345922094])
N = np.array([-1248416467144.5132,4299828498072.9155])
Na = -2.306017444888871
NM = 1.0243e26
NE = 0.00859
NRev = 60216.8

planetes = ["Soleil", "Mercure", "Vénus", "Terre", "Mars", "Jupiter",
            "Saturne", "Uranus", "Neptune"]

excentricites = [MeE,VE,TE,MaE,JE,SE,UE,NE]
periodes = [MeRev, VRev, TRev, MaRev, JRev, SRev, URev, NRev]

def norm(u):
    return (u[0]**2+u[1]**2)**0.5

objets = [Sol,Me,V,T,Ma,J,S,U,N]
vitesses = [Solv,Mev,Vv,Tv,Mav,Jv,Sv,Uv,Nv]
masses = [SolM,MeM,VM,TM,MaM,JM,SM,UM,NM]

# Calcul des extrencités et des périodes de révolution pour chaque planète
# indépendamment de l'attraction exercée par les autres
dt = 3600
today = date.datetime(2020,5,23).toordinal()
trajectoires = [([],[]) for k in range(len(objets))]
for k in range(1,len(objets)):
    T = today
    pos = np.copy(objets[k])
    vit = np.copy(vitesses[k])
    perihelie = np.copy(objets[k])
    b = True
    print()
    print(planetes[k])
    if np.dot(pos,vit)<0:
        b = False
        while norm(pos)<=norm(perihelie):
            perihelie = np.copy(pos)
            vit = vit-dt*masses[0]*G/norm(pos)**3*pos
            pos = pos+dt*vit
            T = T+dt/3600/24
        print("Prochain périhélie simulé:",date.datetime(2020,5,23).fromordinal(int(T)),norm(pos))
    aphelie = np.copy(objets[0])
    while norm(pos)>norm(aphelie):
        aphelie = np.copy(pos)
        vit = vit-dt*masses[0]*G/norm(pos)**3*pos
        pos = pos+dt*vit
        T = T+dt/3600/24
    Taph = T
    print("Prochain aphélie simulé:",date.datetime(2020,5,23).fromordinal(int(T)),norm(pos))
    perihelie = np.copy(aphelie)
    trajectoires[k][0].append(pos[0])
    trajectoires[k][1].append(pos[1])
    while norm(pos)<norm(perihelie):
        perihelie = np.copy(pos)
        vit = vit-dt*masses[0]*G/norm(pos)**3*pos
        pos = pos+dt*vit
        trajectoires[k][0].append(pos[0])
        trajectoires[k][1].append(pos[1])
        T = T+dt/3600/24
    if b:
        print("Prochain périhélie simulé:",date.datetime(2020,5,23).fromordinal(int(T)),norm(pos))
    print("Excentricité simulée :",
          (1-norm(perihelie)/norm(aphelie))/(1+norm(perihelie)/norm(aphelie)))
    print("Excentricité observée",excentricites[k-1])
    print("Période simulée :")
    print((T-Taph)*2,'jours c\'est-à-dire')
    print(2*(T-Taph)/365.25,'années')
    print("Période observée :", periodes[k-1],"jours.")

for Posx,Posy in trajectoires[1:]:
    plt.plot(Posx,Posy)
plt.legend(planetes[1:])
plt.axis('scaled')
plt.title('Demi-trajectoires d\'aphélie à périhélie (+)')
plt.plot(0,0,',k')

for Posx,Posy in trajectoires[1:]:
    plt.plot(Posx[-1],Posy[-1],'+k')
    
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
dt = 3600
today = date.datetime(2020,5,23)
debut = today.toordinal()
fin = date.datetime(2020,9,11).toordinal()
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
        Posx.append(P[0])
        Posy.append(P[1])
    pos = np.copy(obj2)
    vit = np.copy(vit2)
    
debuP = 0
finP = 1
plt.figure()
for (Posx,Posy) in trajectoires[debuP:finP]:
    plt.plot(Posx,Posy)
plt.legend(planetes[debuP:finP])
for (Posx,Posy) in trajectoires[debuP:finP]:
    plt.plot(Posx[-1],Posy[-1],'+k')
plt.axis('scaled')