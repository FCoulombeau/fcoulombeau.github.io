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

- [Cours, exercices et TD de maths de l'année scolaire 2018/2019](https://fcoulombeau.github.io/cours/PCSI-2018.pdf)
- [Cours du 16 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-Cours-16032020.pdf)
- [Correction des exercices du cours du 16 mars 2020](https://fcoulombeau.github.io/cours/PCSI-Cor-16032020.pdf)
- [Cours du 17 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-Cours-17032020.pdf)
- [TD du 17 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-TD-17032020.pdf)
- [Cours de maths du 18 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-CoursCor-18032020.pdf)
- [Cours d'info du 18 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-Info-18032020.pdf)
- [TD d'info du 20 mars 2020 à distance](https://fcoulombeau.github.io/cours/PCSI-Info-20032020.pdf)
- [Correction de quelques exos de maths (20 mars)](https://fcoulombeau.github.io/cours/PCSI-CoursCor-20032020.pdf)
- [Résumé de ce qui a été fait en TD](https://nbviewer.jupyter.org/urls/fcoulombeau.github.io/cours/Cours-Maths-20032020.ipynb)
- [Correction du TD d'info du 20 mars 2020](https://fcoulombeau.github.io/cours/PCSI-InfoCor-20032020.pdf)

# MP

- [X 2015 PSI-PT](https://fcoulombeau.github.io/cours/X2015-PT-PSI.pdf)
- [Colle de maths MP du 18 mars 2020 à distance](https://fcoulombeau.github.io/cours/MP-Colle-18032020.pdf)

---

# Posts publiés

{% for post in {{site.categories["Enseignement"] | reverse}} %} - {% if post.niveau != "" %}{{post.niveau}} : {% endif %}[{{post.title}}]({{ site.baseurl }}{{ post.url }})
{% endfor %}