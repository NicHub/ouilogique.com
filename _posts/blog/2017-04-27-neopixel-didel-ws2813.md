---
layout: page
title: "Neopixel Didel WS2813"
modified:
categories:
excerpt:
tags: []
image:
     feature: 2017-04-27-neopixel-didel-ws2813-000.jpg
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


¹ ~~Utiliser une résistance de 220 Ω à 1 kΩ pour limiter le courant.~~ Faux ! Voir [l’édition de février-mars 2018 ci-dessous][édit-de-février-mars-2018].
² `A0` est utilisé par défaut dans les programmes de Didel, mais n’importe quel GPIO peut être utilisé.


## Notes

On peut aussi alimenter ce strip en 3.3 V.

Les programmes de Didel sont optimisés pour être aussi compacts que possible et tiennent sans problèmes sur un ATtiny.

| Programme       | Taille programme | Taille variables globales |
| :-:             | :-:              | :-:                       |
| WS28First.ino   | 812 o (2%)       | 9 o (0%)                  |
| RGBvsLogRGB.ino | 886 o (2%)       | 42 o (2%)                 |
| Huetest.ino     | 1264 o  (4%)     | 23 o (1%)                 |



[![Neopixel Didel WS2813][image-1]{: width="90%" }][image-1]


## Édit de février-mars 2018

J’ai refait des tests avec ces LED pour évaluer leur luminosité et je me suis rendu compte que j’avais fait une grosse bourde : il ne faut pas utiliser de résistance de limitation de courant !

Dans la foulée, j’ai aussi essayé de les alimenter de deux façons différentes :

- Avec l’Arduino Nano.
- Avec une alimentation externe 5 V.

> Résultat des courses : l’intensité lumineuse est identique dans les deux cas.

Le programme de test se trouve [sur mon GitHub][Programme de test].

**Alimentation avec l’Arduino Nano**

[![Neopixel Didel WS2813 alimentée par l’Arduino Nano][image-2]{: width="90%" }][image-2]

**Alimentation avec une source externe 5 V**

[![Neopixel Didel WS2813 alimentée par une source externe 5 V][image-3]{: width="90%" }][image-3]


## Test avec un Raspberry Pi

J’ai aussi fait un test avec un Raspberry Pi pour voir s’il est possible de faire fonctionner des LED adressables lorsque le processeur du RPi est utilisé au maximum de sa capacité.

Pour les LED, j’ai utilisé [la solution logicielle proposée par Adafruit][neopixels-rpi].

Pour le stress-test, j’ai utilisé [`vcgencmd`][stress-test].

Pour convertir le 3.3 V en 5 V, j’ai utilisé un *Logic Level Converter* bidirectionnel.

La broche de données est la 18.

> Résultat du test : ça fonctionne parfaitement. Le RPi peut sans problème être utilisé à 100 % de sa capacité et en même temps piloter les deux LED. Peut-être que ça sera plus dur avec plus de LED... à voir.

[![Neopixel Didel WS2813 avec un Raspberry Pi][image-4]{: width="90%" }][image-4]



## Voir aussi

- [LED adressable P9823-F8][LED adressable P9823-F8]
- [RGBstrips.pdf][RGBstrips]


[édit-de-février-mars-2018]: #édit-de-février-mars-2018

[LED adressable P9823-F8]: https://ouilogique.com/leds_adressables/

[RGBstrips]: ../../files/2017-04-27-neopixel-didel-ws2813/RGBstrips.pdf

[Programme de test]: https://github.com/NicHub/ouilogique-Arduino/tree/master/neopixel-didel-ws2813

[image-1]: ../../files/2017-04-27-neopixel-didel-ws2813/2017-04-27-neopixel-didel-ws2813-001.jpg

[image-2]: ../../files/2017-04-27-neopixel-didel-ws2813/2017-04-27-neopixel-didel-ws2813-002.jpg

[image-3]: ../../files/2017-04-27-neopixel-didel-ws2813/2017-04-27-neopixel-didel-ws2813-003.jpg

[image-4]: ../../files/2017-04-27-neopixel-didel-ws2813/2017-04-27-neopixel-didel-ws2813-004.jpg

[neopixels-rpi]: https://learn.adafruit.com/neopixels-on-raspberry-pi/software

[stress-test]: https://core-electronics.com.au/tutorials/stress-testing-your-raspberry-pi.html
