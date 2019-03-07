---
layout: page

gh-repo: FCoulombeau/confmap
gh-badge: [star, fork, follow]

title: "ConfMap"
subtitle: "Transformations conformes du plan complexe (Conformal mappings)"
mathjax: true
date: 2018-06-26T11:19:07+02:00
authors: ["FCoulombeau"]
tags: [ Maths ,  Info ,  Complexes ,  Transformations ]
categories: [ ConfMap ,  Git ]
bigimg: /img/bandeau.png
comments: true
slug:git
---

Cette page regroupe une présentation des diverses pages, posts et documents détaillant le fonctionnement du module Python [ConfMap](https://pypi.org/project/confmap/).

La page du projet : [https://github.com/FCoulombeau/confmap](https://github.com/FCoulombeau/confmap)

ou sur FramaGit     : [https://framagit.org/FCoulombeau/confmap](https://framagit.org/FCoulombeau/confmap)

Pour installer le module :

- **à la main** depuis l'une des deux pages ci-dessus :  
`(bash) python setup.py install`
- **avec pip** s'il est installé sur votre machine :  
`(bash) pip install confmap`

Ce module a pour but de définir des objets, fonctions et méthodes utiles pour effectuer des transformations conformes du plan complexe et des pavages du plan hyperbolique.

# Qu'est-ce qu'une transformation conforme ?

C'est une transformation géométrique qui préserve les angles. On pourra se reporter à [cet article de Wikipedia](https://fr.wikipedia.org/wiki/Transformation_conforme) pour plus d'explications sur les transformations conformes en général.

Ce qui nous intéresse ici, c'est plus particulièrement les **transformations conformes du plan complexe** qui regroupent, grosso modo, toutes les transformations du type $z\mapsto f(z)$ auxquelles on pourrait penser où la conjugaison et le module sont interdits.

Par exemple, $\exp$ peut être vue comme une transformation conforme du plan complexe, ou encore n'importe quel polynôme de la variable $z$.

# Le projet

Ce projet est né d'une difficile journée d'enseignant de mathématiques, où il m'est venu l'idée étrange de tenter de montrer à mes élèves l'effet de la fonction $\exp$ sur le plan complexe. Après quelques vagues dessins au tableau et beaucoup de gesticulations, il m'a fallu admettre que c'était un échec cuisant : non seulement les élèves n'avaient rien compris à ce que j'avais dit, mais encore ils paraissaient être complètement perdus par mes explications.

J'ai donc décidé d'écrire un code Python permettant de visualiser les transformations conformes du plan complexe. L'idée est simple :

- on part d'une image dont on recouvre le plan;
- on applique au plan ainsi recouvert une transformation conforme;
- on regarde le résultat en créant une nouvelle image à partir d'une zone rectangulaire du plan transformé.

![avant](/img/oim-1.png) ---> ![après](/img/oim-2.png)

# Les pages explicatives

- Introduction : [Utilisation de ConfMap pour les transformations conformes](/git/confmap/)
- Introduction : [Utilisation de ConfMap pour les pavages hyperboliques](/git/hyperbolic/)