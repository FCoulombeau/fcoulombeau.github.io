---
layout: page

gh-repo: FCoulombeau/confmap
gh-badge: [star, fork, follow]

title: "Transformations conformes"
subtitle: "Introduction à ConfMap"
date: 2019-02-28T10:52:00+02:00
mathjax: true
authors: ["FCoulombeau"]
slug: transconf
comments: true
tags: ["Maths", "Info", "Complexes", "Transformations"]
categories: ["ConfMap", "Git"]
---
La page du projet : [https://framagit.org/FCoulombeau/confmap](https://framagit.org/FCoulombeau/confmap)

ou sur GitHub     : [https://github.com/FCoulombeau/confmap](https://github.com/FCoulombeau/confmap)

Pour installer le module :

- **à la main** depuis l'une des deux pages ci-dessus :  
`(bash) python setup.py install`
- **avec pip** s'il est installé sur votre machine :  
`(bash) pip install confmap`

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

<p align="center"><img src=/images/oim-1.png style="vertical-align:middle"> $\overset{\exp}{\longrightarrow}$ <img src=/images/oim-2.png style="vertical-align:middle"></p>

# Utilisation et syntaxe

Je complèterai éventuellement plus tard cette section. Pour l'heure, voici un exemple minimal vous permettant d'obtenir les deux images ci-dessus :

1. Installer le module, par exemple à l'aide de `pip install confmap`.
2. Créer un fichier Python dans le même répertoire que l'image (`monimage.jpg` par exemple) que vous souhaitez utiliser.
3. Pour la première image, taper le code suivant :

```python
import confmap as cm
im0 = cm.ImageTransform('monimage.jpg',1,
                r=1.*(1.+0.j),c=0.5*(1.+0.j),
                d=0.-0.5j,output_width=300,
                output_height=200,blur=False)
im0.transform()
```
Pour la seconde image, taper le code suivant :

```python
import trans as conf
im0=conf.ImageTransform('monimage.jpg',1,
                r=1.*(1.+0.j),c=0.5*(1.+0.j),
                d=0.-0.5j,output_width=300,
                output_height=200,blur=False)
im0.exp(N=4,P=2)
im0.transform()
```