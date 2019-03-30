---
layout: page
title: Origine et raison d'être de ce site
subtitle: Repli stratégique après la fermeture de Google+...
date: 2018-06-26T11:19:07+02:00
authors: ["FCoulombeau"]
---

Ce site est né de la fermeture de Google+. Il a essentiellement trois vocations :

- présenter les divers projets que je mets à disposition sur GitHub. Cette présentation se trouve [ici](/git/);
- centraliser les divers liens et documents utiles pour mes élèves, en informatique ou en mathématiques : voir [là](/enseignement/).
- puisque le site offre cette possibilité, blogger de temps à autres. Une liste des derniers posts est présente en bas de cette page, et le menu **Thèmes** permet une recherche thématique dans l'ensemble des posts du blog.

# À propos des commentaires

Certaines pages sont fermées aux commentaires, d'autres au contraire peuvent accueillir des commentaires - qui sont alors les bienvenus !

Avant de commenter, vous pouvez consulter [cette page](/commentpolicy/) pour la mise en forme des commentaires, l'introduction de formules de maths, les smileys, etc...

# Liste des posts

{% for post in site.posts %} - [{{post.title}}]({{ site.baseurl }}{{ post.url }})
{% endfor %}