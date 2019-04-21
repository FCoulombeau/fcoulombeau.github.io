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

# Posts publiés

{% for post in {{site.categories["Enseignement"] | reverse}} %} - {% if post.niveau != "" %}{{post.niveau}} : {% endif %}[{{post.title}}]({{ site.baseurl }}{{ post.url }})
{% endfor %}