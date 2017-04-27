---
layout: page
title: "Neopixel Didel WS2813"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-04-27T18:48:00+02:00
published: true
author: Nico
---


## Projet

Test d’un strip de 2 LED que [Didel](http://www.didel.com/NewsF.html) m’a gracieusement offert.

On peut l’acheter chez Boxtec et dans ce cas, il a 11 LED adressables WS2813. <http://shop.boxtec.ch/didel-neopixel-stickbreakout-ws2813-p-42819.html>

Il y a un guide utilisateur ici : <http://cdn2.boxtec.ch/pub/didel/WS2813MiniStrip.pdf>

Et la spécification des LED WS2813 se trouve ici : <http://cdn2.boxtec.ch/pub/diverse/WS2813.pdf>

Didel propose des exemples de programme pour Arduino <http://didel.com/WS28.zip> et c’est eux que j’ai testés.


## Brochage

| Neopixel Didel | Arduino Nano |
| :-:            | :-:          |
| -              | GND          |
| +              | 5V ¹         |
| d              | A0 ²         |
| b              | NC           |


¹ Utiliser une résistance de 220 Ω à 1 kΩ pour limiter le courant.
² `A0` est utilisé par défaut dans les programmes de Didel, mais n’importe quel GPIO peut être utilisé.


## Notes

On peut aussi alimenter ce strip en 3.3 V.

Les programmes de Didel sont optimisés pour être aussi compacts que possible et tiennent sans problèmes sur un ATtiny.

| Programme       | Taille programme | Taille variables globales |
| :-:             | :-:              | :-:                       |
| WS28First.ino   | 812 o (2%)       | 9 o (0%)                  |
| RGBvsLogRGB.ino | 886 o (2%)       | 42 o (2%)                 |
| Huetest.ino     | 1264 o  (4%)     | 23 o (1%)                 |




[![Neopixel Didel WS2813][i1]{: width="90%" }][i1]

[i1]: ../../files/2017-04-27-neopixel-didel-ws2813/2017-04-27-neopixel-didel-ws2813-001.jpg


## Voir aussi

[LED adressable P9823-F8](http://ouilogique.com/leds_adressables/)
