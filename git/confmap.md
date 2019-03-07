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
bigimg: /img/bandeau.png
---

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