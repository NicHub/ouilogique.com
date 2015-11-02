---
layout: page
title: "Mise en route d’un capteur de pression, température et humidité <em>Strinity Sensors Cobber</em>"
modified:
categories:
excerpt:
tags: []
image:
     feature: Strinity_Sensors_Cobber_001.jpg
date: 2015-11-01T00:26:00+01:00
published: true
author: Nico
---



J’ai acheté une petite carte fort sympathique chez Banggood

<http://www.banggood.com/4-in-1-Temperature-Pressure-Altitude-Light-Sensor-Module-p-965547.html>.

C’est une carte “trois en un” qui permet de mesurer :

- la luminosité ambiante `(U3:TSL2561, 0x39)`
- la pression et l’altitude `(U4:BMP180, 0x77)`
- la température et l’humidité `(U5:AM2321, 0x5C)`

La mise en route fut un peu fastidieuse vu qu’il n’y a pas de doc. Heureusement, Adafruit propose deux pilotes pour la carte `BMP180` :

- <https://github.com/adafruit/Adafruit_BMP085_Unified>
- <https://github.com/adafruit/Adafruit-BMP085-Library>

> La version “Unified” nécessite également cette librairie :
<https://github.com/adafruit/Adafruit_Sensor>

et un pilote pour la carte `TSL2561` :

- <https://github.com/adafruit/Adafruit_TSL2561>

Pour la mesure de température, ça se corse parce qu’Adafruit n’a qu’un pilote pour la carte `AM2315` et il ne fonctionne pas avec la carte `AM2321` :

- <https://github.com/adafruit/Adafruit_AM2315>

Sinon Wangdong propose un pilote qui ne fonctionne pas non plus :

- <https://github.com/wangdong/AM2321>

Alors pour l’instant, j’ai testé la luminosité et la pression et les mesures ont l’air cohérentes, ce qui est un bon point. À noter quand même que la carte `BMP180` retourne aussi la température.

> Les pinoches de la carte sont trop courtes (ou placées trop en retrait) et elle ne tient pas bien dans le breadboard. C’est pour ça que j’ai utilisé les fils.

> J’ai utilisé des pullups de 4.7 kΩ sur le bus I²C.

![](/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_001.jpg)

