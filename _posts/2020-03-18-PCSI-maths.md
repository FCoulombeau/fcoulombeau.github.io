---
layout: post
title: Cours de maths du 18-3-2020
subtitle: Dénombrement : introduction, opérations sur les ensembles
mathjax: true
comments: true
date: 2020-03-18T04:22:51+02:00
authors: ["FCoulombeau"]
tags: [ Maths, Cours, Algèbre linéaire ]
categories: [ Enseignement ]
slug: pcsi-m3
niveau: PCSI
---

# Travail à effectuer

- Télécharger la [partie du cours de maths prévue pour aujourd'hui](https://fcoulombeau.github.io/cours/PCSI-Cours-18032020.pdf).  
  Nous la traiterons ensemble de 8h à 10h sur le serveur Discord.  
  Je mettrai à jour cette page avec les démonstrations du cours et la correction des exercices du cours une fois que nous l'aurons vu ensemble.
- Pour vendredi prochain, préparer autant d'exercices que possible de la feuille d'exercices sur les espaces vectoriels que je vous ai déjà distribuée.  
  Voici aussi la [feuille d'exercices sur le dénombrement](https://fcoulombeau.github.io/cours/PCSI-Exo-18032020.pdf), à télécharger. Vous pouvez commencer à préparer quelques exercices de cette feuille pour vendredi aussi.
- Télécharger la [partie du cours d'informatique prévue pour aujourd'hui](https://fcoulombeau.github.io/cours/PCSI-Info-18032020.pdf).  
  Nous la traiterons ensemble de 10h à 12h sur le serveur Discord.
- Voici ce que je considèrerai comme fait aujourd'hui : [Cahier de texte du 18 mars](https://fcoulombeau.github.io/cours/CT-18032020.pdf).

# Quelques explications et rappels

- Vous pouvez à tout moment de la journée, de 8h à 19h, me joindre par mail, par téléphone ou en postant un commentaire ci-dessous.  
  **_ATTENTION_** : concernant les commentaires, ils sont **modérés**, c'est-à-dire que votre commentaire n'apparaîtra pas immédiatement lorsque vous l'aurez posté. Il faut attendre que j'accepte le commentaire comme valide pour qu'il soit publié. J'ai pris cette précaution pour éviter les nombreux spams qui sont publiés sans cela (probablement automatiquement par des robots).
- N'hésitez pas à demander de l'aide ! Notamment, un petit SMS et je vous rejoins sur le serveur Discord.\\
Une autre possibilité sur le serveur Discord est d'écrire un message commençant par `@François Coulombeau` : une notification me sera envoyée sur mon téléphone et je vous rejoindrai.
- Les notions et résultats importants du cours d'aujourd'hui sont les suivants :
   - Définition de l'**_ensemble des parties_** d'un ensemble.
   - Définition de l'**_image directe_** d'une partie de $E$ par une application $f\in\mathcal{F}(E,F)$.  
     Nous avions déjà croisé cette notion à plusieurs reprises (image d'un sous-espace vectoriel par une application linéaire, ou encore dans le premier chapitre de l'année, définition 1.25 et exercice suivant).
   - Définition de l'**_image réciproque_** d'une partie de $F$ par une application $f\in\mathcal{F}(E,F)$.  
     C'est une notion nouvelle qui peut prêter à confusion : **_attention_**, l'image réciproque d'une partie $A$ de $F$ par $f\in\mathcal{F}(E,F)$, notée $f^{-1}(A)$ est **_toujours définie_**, mais $f^{-1}$ - bijection réciproque de $f$ - n'est définie **_que lorsque $f$ est bijective_**.
   - Définition d'une **_partition_** d'un ensemble, que nous retrouverons plus tard dans l'année sous un autre nom.
   - Les différentes propositions du paragraphe concernant les opérations sur les cardinaux.