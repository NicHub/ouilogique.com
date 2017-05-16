---
layout: page
title: "BMP280 avec Arduino Pro Mini"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-05-11T16:12:00+02:00
published: true
author: Nico
---


## Matériel

- [BMP280 (pression et température) acheté chez Banggood pour 1.98 $][2]
- [ATmega328P-AU Pro Mini 3.3V 8MHz, acheté chez Banggood pour 13 $ les 5 pièces][1]
- [Programmateur FTDI][3]


## Code de test

[Adafruit_BMP280_Library](https://github.com/adafruit/Adafruit_BMP280_Library)

## Notes

Comme ce modèle de BMP280 n’a pas de régulateur de tension 3.3 V, j’en ai ajouté un ([LP2950][7]) soudé sur *veroboard* entre le programmateur FTDI et l’Arduino.

Ce capteur peut être utilisé sur le bus I²C ou le bus SPI. Les dénominations des broches indiquées sur le PCB sont pour l’I²C. Pour le SPI, la table ci-dessous indique la conversion.

## Brochage SPI

| BMP280 | SPI Arduino   |
| :-:    | :-:           |
| VCC    | VCC           |
| GND    | GND           |
| SCL    | SCK    pin 13 |
| SDA    | MOSI   pin 11 |
| CSB    | SS     pin 10 |
| SDO    | MISO   pin 12 |

## Résultats

Je n’ai testé que le mode SPI (hardware) et pas le mode I²C et ça fonctionne bien.

[![BMP280 + Arduino Pro Mini][image-1]][image-1]

## Voir aussi

- [Article d’Adafruit sur le BMP280][4]
- [BMP280 sur le site de Bosch][5]
- [Datasheet du BMP280][6]

[image-1]: ../../files/2017-05-11-bmp280-arduino-pro-mini/2017-05-11-bmp280-arduino-pro-mini-001.jpg
[1]: http://www.banggood.com/5Pcs-3_3V-8MHz-ATmega328P-AU-Pro-Mini-Microcontroller-Board-For-Arduino-p-980292.html?p=0431091025639201412F
[2]: https://www.banggood.com/GY-BMP280-3_3-High-Precision-Atmospheric-Pressure-Sensor-Module-For-Arduino-p-1111135.html?p=0431091025639201412F
[3]: http://www.miniinthebox.com/fr/programme-downloader-ftdi-basic-usb-a-ttl-ft232-pour-arduino_p903425.html
[4]: https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/wiring-and-test
[5]: https://www.bosch-sensortec.com/bst/products/all_products/bmp280
[6]: https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMP280-DS001-18.pdf
[7]: http://www.ti.com/lit/ds/symlink/lp2951-n.pdf
