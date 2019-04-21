---
layout: page
title: "ConfMap"
subtitle: "Transformations conformes (Conformal mappings)"
date: 2018-06-26T11:19:07+02:00
mathjax: true
authors: ["FCoulombeau"]
comments: true
slug: git
bigimg: /img/bandeau.jpg
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

---

# Posts publiés

{% for post in {{site.categories["Git"] | reverse}} %} - {% if post.niveau != "" %}{{post.niveau}} : {% endif %}[{{post.title}}]({{ site.baseurl }}{{ post.url }})
{% endfor %}
