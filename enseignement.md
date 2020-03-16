---
layout: page
title: "Enseignement"
subtitle: "Cours, Notebook, tuto..."
mathjax: true
date: 2019-03-07T21:21:07+02:00
authors: ["FCoulombeau"]
comments: true
slug: teaching
---

Je regroupe ici mes documents de cours, tutoriels, Jupyter notebooks et autres.

---

# PCSI

- [Cours, exercices et TD de maths de l'année scolaire 2018/2019](https://fcoulombeau.github.io/PCSI-2018.pdf)
- [Cours du 16 mars 2020 à distance](https://fcoulombeau.github.io/PCSI-Cours-16032020.pdf)

# MP

- [X 2015 PSI-PT](https://fcoulombeau.github.io/X2015-PT-PSI.pdf)

---

# Posts publiés

{% for post in {{site.categories["Enseignement"] | reverse}} %} - {% if post.niveau != "" %}{{post.niveau}} : {% endif %}[{{post.title}}]({{ site.baseurl }}{{ post.url }})
{% endfor %}