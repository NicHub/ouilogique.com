---
layout: page
title: "Mise en route d’un capteur de pression, température et humidité <em>Strinity Sensors Cobber</em> I²C"
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



J’ai acheté une carte chez Banggood pour me faire une mini station météo :

<http://www.banggood.com/4-in-1-Temperature-Pressure-Altitude-Light-Sensor-Module-p-965547.html?p=0431091025639201412F>.

C’est une carte “trois en un” qui permet de mesurer :

- la luminosité ambiante `(U3:TSL2561, 0x39)`
- la pression et l’altitude `(U4:BMP180, 0x77)`
- la température et l’humidité `(U5:AM2321, 0x5C)`

Elle offre la possibilité de sélectionner la tension (3.3 V ou 5V) à l’aide d’un bouton.

La mise en route fut un peu fastidieuse vu qu’il n’y a pas de doc sur Banggood. Heureusement, Adafruit propose deux pilotes pour la carte `BMP180` :

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

Il me reste plus qu’à lire la spec en chinois ;-) <https://www.microduino.cc/wiki/images/d/d1/AM2321.pdf>

En attendant, j’ai testé la luminosité et la pression et les mesures ont l’air cohérentes, ce qui est un bon point. À noter quand même que la carte `BMP180` retourne aussi la température.

> Les pinoches de la carte sont trop courtes (ou placées trop en retrait) et elle ne tient pas bien dans le breadboard. C’est pour ça que j’ai utilisé les fils.

> J’ai utilisé des pullups de 4.7 kΩ sur le bus I²C.

Bon, j’ai décidé de m’y remettre après une semaine de pause et comme le capteur de température ne veut rien savoir, j’ai utilisé un scanner I²C disponible ici :

<http://playground.arduino.cc/Main/I2cScanner>

> Résultat des courses : Le capteur de température ne répond pas ! Et il semble que je ne sois pas le seul dans ce cas, un autre client de Banggod a mentionné ce problème aussi. Bon, je peux quand même lire la température indiquée par le capteur de pression...

> Et comme une image vaut mille mots, j’ai fait une jolie photo du PCB et je me suis rendu compte que le capteur de température n’y est pas... je pouvais le chercher longtemps sur le bus I²C ! Grrr ! La morale de cette histoire, c’est qu’il vaut mieux commencer par prendre le temps de regarder de près les cartes bon marché !


# Liens

- [BMP180 Digital pressure sensor — Bosch Sensortec](/files/2015-11-01-Strinity_Sensors_Cobber/BST-BMP180-DS000-09.pdf)
- [TSL2560, TSL2561 Light-to-Digital Converter — TAOS](/files/2015-11-01-Strinity_Sensors_Cobber/TSL2561.pdf)
- [Lien fourni sur page support Banggood](http://pan.baidu.com/s/1qWjYtqs)

<!--
<figure class="half">
	<a href="/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_002.jpg">
		<img src="/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_002_low_res.jpg" alt="image" />
	</a>
	<a href="/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_003.jpg">
		<img src="/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_003_low_res.jpg" alt="image" />
	</a>
</figure>
-->

![](/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_004_low_res.jpg)

![](/files/2015-11-01-Strinity_Sensors_Cobber/Strinity_Sensors_Cobber_001.jpg)




