# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:47:52 2020

@author: François Coulombeau
"""

import random as r

def creerTableau(p):
    return [0]*p

def affiche(*a,**b):
    print(*a,**b)
    
def entierAleatoire(k):
    return r.randrange(1,k+1)

def creerListeVide(n):
    a = creerTableau(n+1)
    a[0] = 0
    return a

def estDansListe(liste, x):
    n = liste[0]
    for i in range(n):
        if x == liste[i+1]:
            return True
    return False

def ajouteDansListe(liste, x):
    n = liste[0]
    if not estDansListe(liste,x):
        liste[0] = n+1
        liste[n+1] = x

plan1 = [[5,7],
         [2,2,3,0,0],
         [3,1,3,5,0],
         [4,1,2,4,5],
         [2,3,5,0,0],
         [3,2,3,4,0]]

plan2 = [[5,4],
         [1,2,0,0,0],
         [3,1,4,3,0],
         [1,2,0,0,0],
         [2,2,5,0,0],
         [1,4,0,0,0]]

def creerPlanSansRoute(n):
    res = creerTableau(n+1)
    el = creerTableau(2)
    el[0] = n
    el[1] = 0
    res[0] = el
    for i in range(n):
        el = creerListeVide(n)
        res[i+1] = el
    return res

def estVoisine(plan, x, y):
    return estDansListe(plan[x],y)

def ajouteRoute(plan, x, y):
    m = plan[0][1]
    if not estVoisine(plan,x,y):
        plan[0][1]=m+1
        ajouteDansListe(plan[x],y)
        ajouteDansListe(plan[y],x)


def afficheToutesLesRoutes(plan):
    m = plan[0][1]
    nbaffichees = 0
    aAfficher = 'Ce plan contient '+str(m)+' routes : '
    ville = 1
    while nbaffichees<m:
        for i in range(0,plan[ville][0]):
            j = plan[ville][i+1]
            if j>ville:
                aAfficher += '('+str(ville)+'-'+str(j)+') '
                nbaffichees += 1
        ville += 1
    affiche(aAfficher)
  
afficheToutesLesRoutes(plan1)

def coloriageAleatoire(plan, couleur, k, s, t):
    n = plan[0][0]
    couleur[s] = 0
    couleur[t] = k+1
    for i in range(n):
        if i+1!=s and i+1!=t:
            couleur[i+1] = entierAleatoire(k)

def voisinesDeCouleur(plan, couleur, i, c):
    n = plan[i][0]
    L = creerListeVide(n)
    for k in plan[i][1:n+1]:
        if couleur[k]==c:
            ajouteDansListe(L,k)
    return L

def voisinesDeLaListeDeCouleur(plan, couleur, liste, c):
    nb = liste[0]
    n= plan[0][0]
    L = creerListeVide(n)
    for i in liste[1:nb+1]:
        p = plan[i][0]
        for k in plan[i][1:p+1]:
            if couleur[k]==c:
                ajouteDansListe(L,k)
    return L

def existeCheminArcEnCiel(plan, couleur, k, s, t):
    L = voisinesDeCouleur(plan,couleur,s,1)
    i=2
    while L[0]>0 and i<=k:
        L = voisinesDeLaListeDeCouleur(plan, couleur, L, i)
        i=i+1
    L = voisinesDeLaListeDeCouleur(plan, couleur, L, k+1)
    return L[0]>0

def existeCheminSimple(plan, k, s, t):
    n = plan[0][0]
    couleur = creerTableau(n+1)
    for i in range(k**k):
        coloriageAleatoire(plan, couleur, k, s, t)
        if existeCheminArcEnCiel(plan,couleur,k,s,t):
            return True
    return False

print(existeCheminSimple(plan1, 2, 1, 5))