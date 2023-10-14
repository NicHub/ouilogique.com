---
author: Nico
date: 2017-04-27 18:48:00+02:00
image:
    feature: banner_2017-04-27-neopixel-didel-ws2813.jpg
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Neopixel Didel WS2813
---

## Projet

Test d’un strip de 2 LED que [Didel](http://www.didel.com/NewsF.html) m’a gracieusement offert.

On peut l’acheter chez Boxtec et dans ce cas, il a 11 LED adressables WS2813. <http://shop.boxtec.ch/didel-neopixel-stickbreakout-ws2813-p-42819.html>{:rel="nofollow"}

Il y a un guide utilisateur ici : <http://cdn2.boxtec.ch/pub/didel/WS2813MiniStrip.pdf>{:rel="nofollow"}

Et la spécification des LED WS2813 se trouve ici : <http://cdn2.boxtec.ch/pub/diverse/WS2813.pdf>{:rel="nofollow"}

Didel propose des exemples de programme pour Arduino <http://didel.com/WS28.zip>{:rel="nofollow"} et c’est eux que j’ai testés.

## Brochage

| Neopixel Didel | Arduino Nano |
| :------------: | :----------: |
|       -        |     GND      |
|       +        |     5V ¹     |
|       d        |     A0 ²     |
|       b        |      NC      |

¹ ~~Utiliser une résistance de 220 Ω à 1 kΩ pour limiter le courant.~~ Faux ! Voir [l’édition de février-mars 2018 ci-dessous][édit-de-février-mars-2018].
² `A0` est utilisé par défaut dans les programmes de Didel, mais n’importe quel GPIO peut être utilisé.

## Notes

On peut aussi alimenter ce strip en 3.3 V.

Les programmes de Didel sont optimisés pour être aussi compacts que possible et tiennent sans problèmes sur un ATtiny.

|    Programme    | Taille programme | Taille variables globales |
| :-------------: | :--------------: | :-----------------------: |
|  WS28First.ino  |    812 o (2%)    |         9 o (0%)          |
| RGBvsLogRGB.ino |    886 o (2%)    |         42 o (2%)         |
|   Huetest.ino   |   1264 o (4%)    |         23 o (1%)         |

[![Neopixel Didel WS2813][img_1]{:style="width:90%"}][img_1]

## Édit de février-mars 2018

J’ai refait des tests avec ces LED pour évaluer leur luminosité et je me suis rendu compte que j’avais fait une grosse bourde : il ne faut pas utiliser de résistance de limitation de courant !

Dans la foulée, j’ai aussi essayé de les alimenter de deux façons différentes :

-   Avec l’Arduino Nano.
-   Avec une alimentation externe 5 V.

> Résultat des courses : l’intensité lumineuse est identique dans les deux cas.

Le programme de test se trouve [sur mon GitHub][programme de test].

**Alimentation avec l’Arduino Nano**

[![Neopixel Didel WS2813 alimentée par l’Arduino Nano][img_2]{:style="width:90%"}][img_2]

**Alimentation avec une source externe 5 V**

[![Neopixel Didel WS2813 alimentée par une source externe 5 V][img_3]{:style="width:90%"}][img_3]

## Test avec un Raspberry Pi

J’ai aussi fait un test avec un Raspberry Pi pour voir s’il est possible de faire fonctionner des LED adressables lorsque le processeur du RPi est utilisé au maximum de sa capacité.

Pour les LED, j’ai utilisé [la solution logicielle proposée par Adafruit][neopixels-rpi].

Pour le stress-test, j’ai utilisé [`vcgencmd`][stress-test].

Pour convertir le 3.3 V en 5 V, j’ai utilisé un _Logic Level Converter_ bidirectionnel.

La broche de données est la 18.

> Résultat du test : ça fonctionne parfaitement. Le RPi peut sans problème être utilisé à 100 % de sa capacité et en même temps piloter les deux LED. Peut-être que ça sera plus dur avec plus de LED... à voir.

[![Neopixel Didel WS2813 avec un Raspberry Pi][img_4]{:style="width:90%"}][img_4]

## Voir aussi

-   [LED adressable P9823-F8][led adressable p9823-f8]
-   [RGBstrips.pdf][rgbstrips]

[édit-de-février-mars-2018]: #édit-de-février-mars-2018
[led adressable p9823-f8]: https://ouilogique.com/leds_adressables/
[rgbstrips]: ../../files/2017-04-27-neopixel-didel-ws2813/docs/RGBstrips.pdf
[programme de test]: https://github.com/NicHub/ouilogique-Arduino/tree/master/neopixel-didel-ws2813
[img_1]: ../../files/2017-04-27-neopixel-didel-ws2813/images/2017-04-27-neopixel-didel-ws2813-001.jpg
[img_2]: ../../files/2017-04-27-neopixel-didel-ws2813/images/2017-04-27-neopixel-didel-ws2813-002.jpg
[img_3]: ../../files/2017-04-27-neopixel-didel-ws2813/images/2017-04-27-neopixel-didel-ws2813-003.jpg
[img_4]: ../../files/2017-04-27-neopixel-didel-ws2813/images/2017-04-27-neopixel-didel-ws2813-004.jpg
[neopixels-rpi]: https://learn.adafruit.com/neopixels-on-raspberry-pi?view=all
[stress-test]: https://core-electronics.com.au/tutorials/stress-testing-your-raspberry-pi.html
