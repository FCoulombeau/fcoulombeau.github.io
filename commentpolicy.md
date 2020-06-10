---
date: 2019-02-28T11:18:24+02:00
authors: [ "FCoulombeau" ]
title: "Commentaires"
comments: true
layout: page
mathjax: true
subtitle: "De l'usage de Markdown, de Latex et des smileys dans les commentaires"
slug: cp
---

Tous les commentaires sont les bienvenus... ou presque ! Seront automatiquement effacés :

- tous les commentaires agressifs, discourtois, hargneux, etc...
- tous les commentaires hors-sujet ou autres messages publicitaires, spam, etc...
- les trolls :laughing:

Le Markdown peut-être utilisé pour la mise en forme du texte dans les commentaires - ainsi que sur beaucoup de sites Web contemporains. [Prenez 5 minutes pour apprendre le Markdown](http://markdowntutorial.com/) (tutoriel en anglais) ou consultez ce [post](/2019-03-08-markdown/) avec les principales syntaxes expliquées.

Des smileys sont aussi disponibles. L'ensemble des smileys supportés se trouve [là](https://www.webpagefx.com/tools/emoji-cheat-sheet/). On peut aussi (avec certains navigateurs) les obtenir avec un simple clic droit. Parmi les plus courants :

-  :smiley: -> Taper `:`smiley`:`
-  :laughing: -> Taper `:`laughing`:`
-  :wink: -> Taper `:`wink`:`
-  :worried: -> Taper `:`worried`:`
-  :grin: -> Taper `:`grin`:`
-  :sweat_smile: -> Taper `:`sweat_smile`:`
-  :angry: -> Taper `:`angry`:`

Des formules mathématiques, utilisant le langage Latex, peuvent enfin être insérées dans les commentaires. Soit en entourant les formules de `$` - formules en-ligne -, soit en les entourant de `$$` - formules centrées. Par exemple :

- $\int_a^bf(t)dt$ s'écrit `$\int_a^bf(t)dt$`
- $\displaystyle\sum_{i=1}^ni=\dfrac{n(n+1)}{2}$ s'écrit `$\displaystyle\sum_{i=1}^ni=\dfrac{n(n+1)}{2}$`  
Remarque : le `\displaystyle` n'est pas absolument nécessaire, mais c'est tellement plus beau avec :yum:
- etc...

Juste pour cette page, et pour que les novices puissent s'exercer... les commentaires hors-sujet sont autorisés !

Derniers commentaires :
        {% assign comments = site.data.comments | sort %}
        {% for comment in comments %}
        {% assign coms = comment[1] | sort %}
        {% for com in coms %}
          {% assign email = com[1].email %}
          {% assign name = com[1].name %}
          {% assign url = com[1].url %}
          {% assign date = com[1].date %}
          {% assign message = com[1].message limit:30%}
          <br/>- Publié le {{ date }} par {{ name }} : <a href="https://fcoulombeau.github.io/{{ comment[0] }}/#comment{{ forloop.index }}">{{ comment[0] }}</a>
        {% endfor %}
        {% endfor %}