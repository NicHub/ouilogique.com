---
author: Nico
date: 2015-06-26 17:15:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from:
    - /blog/nodejs_arduino_matrices/
tags: []
title: Commander des Arduino avec Node.js
---

Le système est géré avec un Raspberry Pi B+ avec :

-   Un serveur [Node.js](https://nodejs.org){:target="\_blank"}
-   [Un hotspot WiFi](https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point?view=all){:target="\_blank"}
-   [Un hub USB](/usb_hub_test/) sur lequel sont connectés les Arduino. Il y a 6 Arduino au total : 5 pour les matrices d’affichage et un 6<sup>e</sup> pour le contrôle des 4 boutons poussoirs.

La communication se passe de la façon suivante :

-   On connecte l’iPad au réseau WiFi du RPi
-   On charge la page web de l’application dans Safari sur l’iPad
-   On envoie des requêtes de changement de chiffres depuis la page web
-   Le serveur Node.js reçoit les requêtes et les envoie via RS232 aux Arduino

<iframe width="560" height="315" src="https://www.youtube.com/embed/b8a_t5Tyg44" frameborder="0" allowfullscreen></iframe>

[![ouilogique.com][img_1]][img_1]

[img_1]: ../../files/2015-06-26-nodejs_arduino_matrices/2015-05-29_platine.jpg

[![ouilogique.com][img_2]][img_2]

[img_2]: ../../files/2015-06-26-nodejs_arduino_matrices/2015-05-30_boutons.jpg
