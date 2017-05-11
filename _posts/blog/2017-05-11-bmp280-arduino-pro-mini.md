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

- [BMP280 acheté chez Banggood pour 1.98 $][2]
- [ATmega328P-AU Pro Mini 3.3V 8MHz, acheté chez Banggood pour 13 $ les 5 pièces][1]
- [Programmateur FTDI][3]


## Code de test

[Adafruit_BMP280_Library](https://github.com/adafruit/Adafruit_BMP280_Library)

## Note

Comme ce modèle de BMP280 n’a pas de régulateur de tension 3.3 V, j’en ai ajouté un soudé sur *veroboard* entre le programmateur FTDI et l’Arduino.

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

Je n’ai testé que le mode SPI (hardware) et pas le mode I²C. Les valeurs de température ont l’air un peu trop élevées et celles de pression trop faibles... à investiguer.


[![BMP280 + Arduino Pro Mini][image-1]][image-1]


[image-1]: ../../files/2017-05-11-bmp280-arduino-pro-mini/2017-05-11-bmp280-arduino-pro-mini-001.jpg
[1]: http://www.banggood.com/5Pcs-3_3V-8MHz-ATmega328P-AU-Pro-Mini-Microcontroller-Board-For-Arduino-p-980292.html?p=0431091025639201412F
[2]: https://www.banggood.com/GY-BMP280-3_3-High-Precision-Atmospheric-Pressure-Sensor-Module-For-Arduino-p-1111135.html?p=0431091025639201412F
[3]: http://www.miniinthebox.com/fr/programme-downloader-ftdi-basic-usb-a-ttl-ft232-pour-arduino_p903425.html
