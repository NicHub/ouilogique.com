---
author: Nico
date: 2017-10-22 17:54:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Humour Matplotlib
---

Un peu d’humour avec Matplotlib. L’exemple vient de la page <https://matplotlib.org/1.3.0/examples/showcase/xkcd.html>.

[![Effets des pizzas sur ma santé][img_1]][img_1]

[img_1]: ../files/2017-10-22-humour-matplotlib/images/effet-des-pizzas-sur-ma-sante.png

Et le code se trouve là : [effet-des-pizzas-sur-ma-sante.py][effet-des-pizzas-sur-ma-sante]

Matplotlib fait partie des 4 bibliothèques de base pour le calcul numérique avec Python

-   NumPy (libraire de base)
-   SciPy (fonctions étendues)
-   Matplotlib (graphiques)
-   Pandas (gestion des données)

On peut écrire le code dans n’importe quel éditeur de texte, mais c’est quand même plus agréable d’utiliser _Spyder_ qui est un IDE qui ressemble comme deux gouttes d’eau à celui de _Matlab_.

> *Édit du 29 janvier 2019* : je n’utilise plus Spyder maintenant, mais [Visual Studio Code](https://code.visualstudio.com/).

_Python_, _Spyder_, les 4 bibliothèques dont j’ai parlé ainsi qu’une ribambelle d’autres outils peuvent être téléchargés et installés avec [le package _Anaconda_](https://www.anaconda.com/download/). Si vous débutez dans le monde _Python_, je vous conseille de télécharger la version _Python 3.6_. En tout cas, je vous déconseille de commencer un nouveau projet en Python 2.7, car son développement sera arrêté en 2020 et le décompte se trouve sur cette page : [pythonclock.org](https://pythonclock.org/).

Une fois _Anaconda_ installé, vous pouvez ouvrir _Spyder_ de la façon suivante :

-   Sous Windows, taper `spyder` dans le menu démarrer
-   Sous MacOS, ouvrir le Terminal et taper `spyder`. La fenêtre du Terminal doit rester ouverte pendant l’utilisation de _Spyder_.

Vous pouvez découvrir les techniques de base dans [le fichier de démo][demo].

## Références

-   [Mon aide mémoire Python](../files/2017-10-22-humour-matplotlib/docs/python_aide-memoire.py)
-   <http://www.diveintopython3.net/>
-   <https://python.developpez.com/cours/plongez_au_coeur_de_python/?page=page1>

[effet-des-pizzas-sur-ma-sante]: ../files/2017-10-22-humour-matplotlib/docs/effet-des-pizzas-sur-ma-sante.py
[demo]: ../files/2017-10-22-humour-matplotlib/docs/demo.py

## Notes

La police utilisée par xkcd est _Humor Sans_ et peut être téléchargée ici : <https://github.com/shreyankg/xkcd-desktop>. Malheureusement, elle ne fonctionne que sous Gnome.

Une police qui ressemble est _Graphite_. Adobe en propose une version payante ici : <https://fonts.adobe.com/fonts/graphite#fonts-section>. Mais on peut télécharger gratuitement une des fontes ici : <https://www.fontyukle.net/en/DownLoad-Graphite+Std.ttf> ou la famille entière ici : <https://www.wfonts.com/font/graphite-std>.
