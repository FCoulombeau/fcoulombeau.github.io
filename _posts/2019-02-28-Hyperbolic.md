---
layout: post

gh-repo: FCoulombeau/confmap
gh-badge: [star, fork, follow]

title: "Pavages hyperboliques"
subtitle: "Introduction à ConfMap"
date: 2019-02-28T10:52:00+02:00
mathjax: true
authors: ["FCoulombeau"]
comments: true
slug: hyperb
tags: ["Maths", "Info", "Pavages hyperboliques", "ConfMap"]
categories: ["Git"]
niveau : Introduction à ConfMap
image: /img/Reflets-1.jpg
bigimg: /img/bandeau.jpg
---
L'article sur les [transformations conformes](/2019-28-02-Confmap/) explique comment utiliser le module [confmap](https://github.com/FCoulombeau/confmap) pour faire des transformations conformes.

Je présente ici comment l'utiliser pour obtenir des pavages du plan hyperbolique.

# Utilisation et syntaxe

Je complèterai éventuellement plus tard cette section. Pour l'heure, voici un exemple minimal vous permettant d'obtenir les deux images ci-dessus :

1. Installer le module, par exemple à l'aide de `pip install confmap`.
2. Créer un fichier Python dans le même répertoire que l'image (`monimage.jpg` par exemple) que vous souhaitez utiliser.
3. Créer un pavage hyperbolique  - ici par un hexagone régulier, avec 4 hexagones autour de chaque sommet, ce qui est possible en géométrie hyperbolique ! -:

```python
import confmap as cm

im = cm.HyperbolicTiling('monimage.jpg',0,'',600,600)

im.transform(sommets=(6,4),nbit=20,backcolor=[255,255,255])
```
Ou un pavage un peu plus compliqué :
 
```python
import confmap as cm
import numpy as np

im = cm.HyperbolicTiling('monimage.jpg',1,'',600,600)

im.transform(sommets=(np.inf,6,4,6),nbit=20,
             backcolor=[255,255,255])
```

Ce qui donne les images suivantes :

![Reflets 1](/img/Reflets-1.jpg)

![Reflets 2](/img/Reflets-0.jpg)