---
layout: page
title: "Humour Matplotlib"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-10-22T17:54:00+02:00
published: true
author: Nico
---


Un peu d’humour avec Matplotlib. L’exemple vient de la page <https://matplotlib.org/1.3.0/examples/showcase/xkcd.html>.


[![Effets des pizzas sur ma santé][image-1]][image-1]

[image-1]: ../../files/2017-10-22-humour-matplotlib/effet-des-pizzas-sur-ma-sante.png


Et le code se trouve là : [effet-des-pizzas-sur-ma-sante.py][effet-des-pizzas-sur-ma-sante]



Matplotlib fait partie des 4 bibliothèques de base pour le calcul numérique avec Python

- NumPy (libraire de base)
- SciPy (fonctions étendues)
- Matplotlib (graphiques)
- Pandas (gestion des données)

On peut écrire le code dans n’importe quel éditeur de texte, mais c’est quand même plus agréable d’utiliser *Spyder* qui est un IDE qui ressemble comme deux gouttes d’eau à celui de *Matlab*.

> *Edit du 29 janvier 2019* : je n’utilise plus Spyder maintenant, mais [Visual Studio Code](https://code.visualstudio.com/).

*Python*, *Spyder*, les 4 bibliothèques dont j’ai parlé ainsi qu’une ribambelle d’autres outils peuvent être téléchargés et installés avec [le package *Anaconda*](https://www.anaconda.com/download/). Si vous débutez dans le monde *Python*, je vous conseille de télécharger la version *Python 3.6*. En tout cas, je vous déconseille de commencer un nouveau projet en Python 2.7, car son développement sera arrêté en 2020 et le décompte se trouve sur cette page : [pythonclock.org](https://pythonclock.org/).

Une fois *Anaconda* installé, vous pouvez ouvrir *Spyder* de la façon suivante :

- Sous Windows, taper `spyder` dans le menu démarrer
- Sous MacOS, ouvrir le Terminal et taper `spyder`. La fenêtre du Terminal doit rester ouverte pendant l’utilisation de *Spyder*.

Vous pouvez découvrir les techniques de base dans [le fichier de démo][demo].


## Références

- [Mon aide mémoire Python](../../files/2017-10-22-humour-matplotlib/python_aide-memoire.py)
- <http://www.diveintopython3.net/>
- <https://python.developpez.com/cours/plongez_au_coeur_de_python/?page=page1>


[effet-des-pizzas-sur-ma-sante]: ../../files/2017-10-22-humour-matplotlib/effet-des-pizzas-sur-ma-sante.py

[demo]:  ../../files/2017-10-22-humour-matplotlib/demo.py

## Notes

La police utilisée par xkcd est *Humor Sans* et peut être téléchargée ici : <https://github.com/shreyankg/xkcd-desktop>. Malheureusement, elle ne fonctionne que sous Gnome.

Une police qui ressemble est *Graphite*. Adobe en propose une version payante ici : <https://fonts.adobe.com/fonts/graphite#fonts-section>. Mais on peut télécharger gratuitement une des fontes ici : <https://www.fontyukle.net/en/DownLoad-Graphite+Std.ttf> ou la famille entière ici : <https://www.wfonts.com/font/graphite-std>.
