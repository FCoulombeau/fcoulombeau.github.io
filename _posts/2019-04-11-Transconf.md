---
layout: post

gh-repo: FCoulombeau/confmap
gh-badge: [star, fork, follow]

title: "La fonction $\exp$"
subtitle: "Un exemple de transformation conforme"
date: 2019-04-22T11:03:00+02:00
mathjax: true
authors: ["FCoulombeau"]
comments: true
slug: foncexp
tags: ["Maths", "Info", "Transformations conformes", "ConfMap"]
categories: ["Git"]
niveau : Introduction à ConfMap
image: /img/Pluie.jpg
bigimg: /img/bandeau.jpg
---

Cet article a pour but de détailler, en se concentrant sur l'exemple de la fonction **_exponentielle_** complexe, les propriétés des **_transformations conformes_**.

# Un peu de vocabulaire

Le terme de **_transformation_** est un synonyme, en mathématiques, du terme bijection : il s'agit d'une fonction entre deux ensembles telle que tout élément du second ensemble possède un, et un seul, antécédent dans le premier ensemble. Une des dénominations anglaises pour cette notion est **one-to-one-mapping** qui est probablement plus parlante.  
Par ailleurs, le terme de **_transformation_** s'utilise pour les fonctions entre ensembles géométriques.

On dit d'une transformation qu'elle est **_conforme_** si elle préserve, localement, les angles.

Parmi les transformations conformes, il y a donc les **_isométries_** qui préservent non seulement les angles, mais aussi les longueurs. Ou plus généralement les **_similitudes_** qui multiplient toutes les longueurs par un réel donné, appelé rapport de similitude.

Enfin, on dit d'une similitude qu'elle est **_directe_** si elle préserve les **_angles orientés_**.

Pour en savoir plus sur les similitudes, notamment pour comprendre que l'on peut facilement les classifier, on pourra se rapporter à l'[article de Wikipedia](https://fr.wikipedia.org/wiki/Similitude_(g%C3%A9om%C3%A9trie)) sur le sujet.

# Similitudes directes du plan complexe

Intéressons plus précisément aux similitudes directes de $\mathds{C}$, c'est-à-dire aux fonctions du plan complexe dans lui-même multipliant les longueurs par un réel strictement positif et préservant les angles orientés. Par théorème de classification, on peut affirmer que

- du point de vue géométrique, ce sont _exactement_ les **translations**, les **rotations** ou les composées d'une rotation et d'un homothétie de même centre;
- du point de vue numérique, ce sont _exactement_ les fonctions du type $f:z\mapsto az+b$ où $a\neq0$ et $b$ sont deux nombres complexes.