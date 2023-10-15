---
author: Nico
date: 2017-05-11 16:12:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: BMP280 avec Arduino Pro Mini
---

## Matériel

-   [BMP280 (pression et température) acheté chez Banggood pour 1.98 $][2]
-   [ATmega328P-AU Pro Mini 3.3V 8MHz, acheté chez Banggood pour 13 $ les 5 pièces][1]
-   [Programmateur FTDI][3]

## Code de test

[Adafruit_BMP280_Library](https://github.com/adafruit/Adafruit_BMP280_Library)

## Notes

Comme ce modèle de BMP280 n’a pas de régulateur de tension 3.3 V, j’en ai ajouté un ([LP2950][7]) soudé sur _veroboard_ entre le programmateur FTDI et l’Arduino.

Ce capteur peut être utilisé sur le bus I²C ou le bus SPI. Les dénominations des broches indiquées sur le PCB sont pour l’I²C. Pour le SPI, la table ci-dessous indique la conversion.

## Brochage SPI

| BMP280 | SPI Arduino |
| :----: | :---------: |
|  VCC   |     VCC     |
|  GND   |     GND     |
|  SCL   | SCK pin 13  |
|  SDA   | MOSI pin 11 |
|  CSB   |  SS pin 10  |
|  SDO   | MISO pin 12 |

## Résultats

Je n’ai testé que le mode SPI (hardware) et pas le mode I²C et ça fonctionne bien.

[![BMP280 + Arduino Pro Mini][img_1]][img_1]

[img_1]: ../files/2017-05-11-bmp280-arduino-pro-mini/images/2017-05-11-bmp280-arduino-pro-mini-001.jpg

## Voir aussi

-   [Article d’Adafruit sur le BMP280][4]
-   [BMP280 sur le site de Bosch][5]{:rel="nofollow"}
-   [Datasheet du BMP280][6]{:rel="nofollow"}

[1]: https://usa.banggood.com/5Pcs-3_3V-8MHz-ATmega328P-AU-Pro-Mini-Microcontroller-With-Pins-Development-Board-p-980292.html?imageAb=2&akmClientCountry=America&p=0431091025639201412F&a=1697373190.4133&akmClientCountry=America
[2]: https://www.banggood.com/GY-BMP280-3_3-High-Precision-Atmospheric-Pressure-Sensor-Module-For-Arduino-p-1111135.html?p=0431091025639201412F
[3]: https://m.miniinthebox.com/fr/p/programme-downloader-ftdi-basic-usb-a-ttl-ft232-pour-arduino_p903425.html
[4]: https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/wiring-and-test
[5]: https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp280/
[6]: https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf
[7]: http://www.ti.com/lit/ds/symlink/lp2951-n.pdf
