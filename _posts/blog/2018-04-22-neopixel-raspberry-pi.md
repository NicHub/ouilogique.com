---
layout: page
title: "NeoPixel sur Raspberry Pi"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2018-04-22T12:33:00+02:00
published: true
author: Nico
---


Voici comment configurer un Raspberry Pi pour l’utiliser avec des LED NeoPixel WS281x. Je présente la version Python, mais d’autres langages sont supportés.

[![NeoPixel sur Raspberry Pi][image-1]][image-1]

> Les deux câbles brun et bleu à droite du *breadboard* sont connectés à une alimentation 5 V.


## Sources

Les informations de cet article proviennent des sources suivantes :

- [Adafruit NeoPixels On Raspberry Pi][Adafruit NeoPixels On Raspberry Pi]
- [rpi_ws281x from jgarff on GitHub][rpi_ws281x from jgarff on GitHub]


## Câblage

Le Rpi fonctionne en 3.3 V et les NeoPixels en 5 V. Il est donc nécessaire d’utiliser un *logic level converter*.

L’anneau de LED a 4 connexions :

- DI (signal)
- 5 V
- GND
- DO (pas connecté)


## Matériel

- [Anneau de 24 LED WS2812 — NeoPixel][Anneau de 24 LED WS2812 — NeoPixel]
- [Logic Level Converter][Logic Level Converter]
- Raspberry Pi 2 Model B / Raspbian Stretch
- Raspberry Pi 3 Model B / Raspbian Jessie


## Compilation et installation de la librairie `rpi_ws281x`

    sudo apt-get update
    sudo apt-get install build-essential python-dev git scons swig
    git clone https://github.com/jgarff/rpi_ws281x.git
    cd rpi_ws281x
    scons
    cd python
    sudo python setup.py install

## Édition du fichier `strandtest.py`

    nano strandtest.py

Modifier la variable `LED_COUNT`

    LED_COUNT   = 24


## Utilisation du PWM

Comme la bibliothèque `rpi_ws281x` et l’audio du board du Raspberry utilisent tous les deux le PWM, elles ne peuvent pas être utilisées ensemble. Pour désactiver l’audio, il faut mettre le module du kernel audio de Broadcom dans une liste noire. Pour cela, il faut créer le fichier `snd-blacklist.conf` :

    sudo nano /etc/modprobe.d/snd-blacklist.conf

Et lui ajouter la commande suivante :

    blacklist snd_bcm2835

> Il faut se rappeler de commenter cette ligne si on veut utiliser l’audio dans d’autres projets !

Et finalement, il faut redémarrer le Rpi :

    sudo reboot


## Test

Maintenant que le Rpi est redémarré, on va dans le répertoire des exemples :

    cd ~/rpi_ws281x/python/examples

Et on exécute l’exemple `strandtest.py`. L’instruction `sudo` est requise car la bibliothèque `rpi_ws281x` utilise des fonctions de bas niveau et doit donc être exécutée avec les droits de `root` :

    sudo python strandtest.py


## Utilisation du CPU

Voici ce que me retourne la commande `top`. On voit que le processus `python` consomme 1.6% des ressources CPU sur un Raspberry Pi 3 modèle B. Pour pouvoir lancer cette commande, il faut faire tourner `strandtest.py` dans un autre shell avec la commande [`screen`][GNU Screen sur ouilogique.com].

    top - 13:30:48 up 14 min,  3 users,  load average: 0.19, 0.09, 0.02
    Tasks: 155 total,   1 running, 154 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.7 us,  0.2 sy,  0.0 ni, 99.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    KiB Mem:    945512 total,   327704 used,   617808 free,    25008 buffers
    KiB Swap:   102396 total,        0 used,   102396 free.   207116 cached Mem

      PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
     3438 root      20   0   14236  10712   5960 S   1.6  1.1   0:02.39 python
     3439 pi        20   0    5276   2520   2020 R   0.7  0.3   0:00.60 top
        1 root      20   0   22780   3952   2788 S   0.0  0.4   0:02.85 systemd
        2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd


[image-1]: ../../files/2018-04-22-neopixel-raspberry-pi/2018-04-22-neopixel-raspberry-pi-001_lowres.jpg

[Adafruit NeoPixels On Raspberry Pi]: https://learn.adafruit.com/neopixels-on-raspberry-pi/software

[rpi_ws281x from jgarff on GitHub]: https://github.com/jgarff/rpi_ws281x

[Anneau de 24 LED WS2812 — NeoPixel]: https://www.banggood.com/CJMCU-24-Bit-WS2812-5050-RGB-LED-Driver-Development-Board-p-974188.html?p=0431091025639201412F)

[Logic Level Converter]: https://www.banggood.com/Logic-Level-Converter-Bi-Directional-IIC-4-Way-Level-Conversion-Module-p-938774.html?p=0431091025639201412F)

[GNU Screen sur ouilogique.com]: http://ouilogique.com/installer-raspian-stretch/#gnu-screen
