---
author: Nico
date: 2016-06-04 14:29:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Test d’une horloge temps réel DS1307 I²C
---

[![ouilogique.com][img_1]][img_1]

[img_1]: ../files/2016-06-04-test_horloge_temps_reel_i2c/2016-06-04-test_horloge_temps_reel_i2c_001_lowres.jpg

[![ouilogique.com][img_2]][img_2]

[img_2]: ../files/2016-06-04-test_horloge_temps_reel_i2c/2016-06-04-test_horloge_temps_reel_i2c_002_lowres.jpg

[![ouilogique.com][img_3]][img_3]

[img_3]: ../files/2016-06-04-test_horloge_temps_reel_i2c/2016-06-04-test_horloge_temps_reel_i2c_003_lowres.jpg

```c++
/*

TEST DE L’HORLOGE TEMPS RÉEL (RTC) DS1307 I²C

RÉFÉRENCE AliExpress DU DS1307
http://fr.aliexpress.com/item/5pcs-lot-Tiny-RTC-I2C-AT24C32-DS1307-Real-Time-Clock-Module-Board-For-Arduino-With-A/32327865928.html

ADRESSES I²C DU DS1307
0x50 (EEPROM AT24C32)
0x68 (DS1307)

VERSION ORIGINALE DU PROGRAMME
http://www.avrfreaks.net/forum/printing-leading-zero-serialprint-function

LIBRAIRIE Adafruit du DS1307
https://github.com/adafruit/RTClib.git

CONNEXIONS
GND    GND
VCC    +5V
SDA    pin A4
SCL    pin A5

MICROCONTRÔLEUR
Clone Arduino Nano

juin 2016, ouilogique.com

*/

#include "RTClib.h"

RTC_Millis RTC;

void setup()
{
  Serial.begin( 115200 );
  // Règle le DS1307 à la date et l’heure de la compilation du programme
  RTC.begin( DateTime( __DATE__, __TIME__ ) );
}

void loop()
{
  DateTime now = RTC.now();
  char buf[ 50 ];
  sprintf( buf, "\n\n%1d-%1d-%1d\n%02d:%02d:%02d", now.day(), now.month(), now.year(), now.hour(), now.minute(), now.second() );
  Serial.print( buf );
  _delay_ms( 1000 );
}
```
