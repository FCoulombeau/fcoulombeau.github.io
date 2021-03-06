---
layout: post
title: Semaine du 7 avril
subtitle: Programme
mathjax: true
comments: true
date: 2020-04-03T07:05:51+02:00
authors: ["FCoulombeau"]
tags: [ Maths, Cours, Info ]
categories: [ Enseignement ]
slug: pcsi-m10
niveau: PCSI
---

Sur le principe, on continue comme la semaine dernière. Pour préparer la semaine, voici le travail à effectuer :
- **_Pour le mardi 8 avril_** : Faire un maximum d'exercices à l'avance en vous répartissant, si possible, les exercices préparés.
- **_Pour le mercredi 9 avril_** : en vue du TD d'informatique, il faut effectuer la préparation suivante (sous Windows - pour les utilisateurs Mac, se référer à [cette page Web](https://zulko.github.io/moviepy/install.html))
   1. Télécharger l'archive [PodRace.zip](/cours/PodRace.zip) et la décompresser dans votre dossier de travail.
   2. Aller dans le dossier d'installation de Python, puis dans le sous-dossier `Scripts`.
   3. Ouvrir une fenêtre `PowerShell` (Maj-Ctrl puis clique droit dans le dossier `Scripts` et *Ouvrir la fenêtre PowerShell ici*).
   4. Il faut être connecté à internet pour effectuer cette étape : cela va télécharger `moviepy` et tous les modules nécessaires puis les installer. Fermer aussi Spyder s'il est ouvert.    
      Taper les lignes suivantes :  
      ```
cmd.exe "/K" .\activate.bat ..\
.\conda.exe update imageio
.\pip.exe install moviepy
      ```  
      Pour tester si l'installation s'est bien passée, télécharger et exécuter ce [fichier Python](https://fcoulombeau.github.io/cours/video.py). Il devrait créer une vidéo dans le dossier où il est enregistré. Si ce n'est pas le cas : (la première ligne est inutile si vous n'avez pas fermé la fenêtre PowerShell)  
      ```
cmd.exe "/K" .\activate.bat ..\
.\pip.exe uninstall moviepy
conda install -c conda-forge moviepy
      ```  
- **_Pour le jeudi 10 et le vendredi 11 avril_** : réviser tous les chapitres sur les espaces vectoriels, lire, comprendre et apprendre le nouveau chapitre.

---

# Mardi 7 avril 10h-12h :
### Exercices
- Préparer la feuille d'exercices sur la [dérivabilité](https://fcoulombeau.github.io/cours/PCSI-Exo-24032020.pdf).  
  **_Faire un maximum d'exercices à l'avance en vous répartissant, si possible, les exercices préparés._**  
  [Corrigé de l'exercice 17.11 et de quelques autres](https://fcoulombeau.github.io/cours/PCSI-ExoCor-07042020.pdf).

---

# Mercredi 8 avril 10h-12h : 
### TD d'info
- [TD d'info : Projet Podrace](https://fcoulombeau.github.io/cours/PCSI-Info-08042020.pdf).  
  Le but de ce TD est de programmer des algorithmes de pilotage automatique de Pods s'affrontant dans une course style **_Star Wars Episode 1_**.  
  Je vous fournis un [programme](/cours/PodRace.zip) qui gère toute la partie ludique et graphique. Il n'y a plus qu'à programmer les algorithmes de pilotage.  
  [Correction du TD](https://fcoulombeau.github.io/img/PodRace.zip).  
  Voici un [exemple de course](/img/wawa2-wawa.webm).  
  Et voici ce que vous [devez vous imaginer :-)](https://www.youtube.com/watch?v=Dqus0aXiAVE).  
  Enfin, ce TD sera la base du prochain devoir à la maison d'informatique.

---

# Jeudi 9 avril 10h-12h : 
### Cours

- Matrices : [début du chapitre sur les matrices](https://fcoulombeau.github.io/cours/PCSI-Cours-09042020.pdf).

---

# Vendredi 10 avril 10h-12h : 
### Cours

- Matrices : [fin du chapitre sur les matrices](https://fcoulombeau.github.io/cours/PCSI-Cours-10042020.pdf).  
  Feuille d'[exercices sur les matrices](https://fcoulombeau.github.io/cours/PCSI-Exo-09042020.pdf) **_à préparer pour le mardi 14 avril et le jeudi 16 avril_**.

---

# Divers

- [Cahier de texte de la semaine](https://fcoulombeau.github.io/cours/CT-10042020.pdf).
- [Programme de colles pour la semaine suivante](https://fcoulombeau.github.io/cours/PC-14042020.pdf).