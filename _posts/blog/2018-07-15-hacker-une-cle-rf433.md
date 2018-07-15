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

Cette technique ne fonctionne qu’avec des émetteurs RF433 non-sécurisés. Ce genre d’émetteurs envoient toujours le même signal que l’on peut copier et programmer sur un Arduino.

À contrario, les émetteurs sécurisés, comme ceux qui sont utilisés pour vérouiller les véhicules, émettent un code différent à chaque utilisation (*rolling code*), ce qui implique qu’il ne sert à rien de copier le signal puisqu’il ne pourra être utilisé au mieux qu’une seule fois.

## Sources

Cet article m’a été inspiré par [la vidéo d’Andreas Spiess “How to Hack your 433 MHz Devices with a Raspberry and a RTL-SDR Dongle (Weather Station)”][Video Andreas].

## Matériel

- SDR-Dongle: http://s.click.aliexpress.com/e/bQ91w8QM ou http://bit.ly/2NcRMT2

- Raspberry Pi modèle 2 ou 3

## Installation d’URH

Pour lire le signal d’origine, nous allons utiliser [le logiciel URH][URH GitHub].

- Si nécessaire, [installer Raspbian Stretch][installer Raspbian Stretch]


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






[Video Andreas]: https://www.youtube.com/watch?v=L0fSEbGEY-Q

[URH GitHub]: https://github.com/jopohl/urh

[installer Raspbian Stretch]: [https://ouilogique.com/installer-raspian-stretch/]

[truc install URH]: https://github.com/jopohl/urh/issues/502

[image-1]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-001.jpg

