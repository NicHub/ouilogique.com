---
layout: page
title: "Hacker une clé RF433"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2018-07-15T15:28:00+02:00
published: true
author: Nico
---



## But

Cet article montre comment lire les signaux d’une clé RF433 à l’aide d’un adaptateur SDR (*Software Defined Radio*). De les copier à l’aide du logiciel URH sur un Raspberry Pi et de programmer un Arduino pour envoyer ces signaux à l’identique.

## Limitation

Cette technique ne fonctionne qu’avec des émetteurs RF433 non sécurisés. Ce genre d’émetteurs envoient toujours le même signal que l’on peut copier et programmer sur un Arduino.

À contrario, les émetteurs sécurisés, comme ceux qui sont utilisés pour verrouiller les véhicules, émettent un code différent à chaque utilisation (*rolling code*), ce qui implique qu’il ne sert à (presque) rien de copier le signal puisqu’il ne pourra être utilisé au mieux qu’une seule fois.

## Sources

Cet article m’a été inspiré par [la vidéo d’Andreas Spiess “How to Hack your 433 MHz Devices with a Raspberry and a RTL-SDR Dongle (Weather Station)”][Video Andreas].

## Matériel

- SDR-Dongle: http://s.click.aliexpress.com/e/bQ91w8QM ou http://bit.ly/2NcRMT2

- Raspberry Pi modèle 2 ou 3

## Installation d’URH

Pour lire le signal d’origine, nous allons utiliser [le logiciel URH][URH GitHub].

- Si nécessaire, [installez Raspbian Stretch][installer Raspbian Stretch]


{% highlight bash %}
sudo apt-get --assume-yes update
sudo apt-get --assume-yes dist-upgrade
sudo apt-get --assume-yes dist install python3-numpy python3-psutil python3-zmq python3-pyqt5 g++ libpython3-dev python3-pip cython3
sudo pip3 install urh
{% endhighlight %}

Si la dernière commande ne fonctionne pas, [il faut ruser un peu][truc install URH] en utilisant les commandes suivantes :

{% highlight bash %}
git clone https://github.com/jopohl/urh
cd urh
sudo pip3 install .
{% endhighlight %}

## Utilisation d’URH

- Connecter l’adaptateur SDR.

[![Raspberry Pi avec dongle SDR][image-1]][image-1]

- Dans l’interface graphique de Raspbian, ouvrir un terminal et taper la commande {% highlight bash %}urh{% endhighlight %}
- Dans la fenêtre qui s’ouvre, aller dans le menu `File/Record signal...`.
- Dans la nouvelle fenêtre, choisir l’adaptateur : `Device : RTL-SDR`.
- Cliquer sur la flèche arrondie en regard de `Device Identifier`. L’identifiant de l’adaptateur doit d’afficher, par exemple : `Realtek RTL2838UHIDIR (SN: 00000001)`.
- Laisser les autres options par défaut.

[![Enregistrement d’un signls RF433 avec URH][image-2]][image-2]

- Cliquer sur le bouton `Start`.
- Appuyer sur le bouton de la clé RF433.
- Cliquer sur le bouton `Stop`. Il faut arrêter l’acquisition le plus rapidement possible car le fichier de résultats grandit à une vitesse vertigineuse. En plus, le buffer est rapidement saturé.
- Cliquer sur `Save` et enregistrer le fichier pour une utilisation ultérieure.
- Fermer la fenêtre d’acqusition. La fenêtre de traitement des données s’ouvre. Cette fenêtre peut être rappelée en ouvrant le fichier enregistré précédement.
- Cliquer sur `Modulation: ASK`. ASK = *Amplitude Shift Keying*.
- Dans la partie sous le graphique, double-cliquer de façon à sélectionner une ligne. La partie correspondante du graphique est sélectionnée. Inversément, on peut sélectionner une partie du graphique et les chiffres correspondant seront automatiquement sélectionnés également.
- On peut zoomer le graphique avec la rolette de la souris. La position du curseur de la souris modifie également le point central du zoom.
- Évaluez quelle ligne de chiffres se répette le plus souvent et la copier avec le raccourci clavier `CTRL-C`.

    1110111011101000100010001000100011101110111010001000111010001000100010001110111010001000111010001


[![Enregistrement d’un signls RF433 avec URH][image-3]][image-3]





[Video Andreas]: https://www.youtube.com/watch?v=L0fSEbGEY-Q

[URH GitHub]: https://github.com/jopohl/urh

[installer Raspbian Stretch]: [https://ouilogique.com/installer-raspian-stretch/]

[truc install URH]: https://github.com/jopohl/urh/issues/502

[image-1]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-001.jpg

[image-2]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-002.jpg

[image-3]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-003.jpg
