---
layout: page
title: "Test d’un écran OLED 128×64 I²C"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2016-05-25T17:22:00+02:00
published: true
author: Nico
---

![...](/files/2016-05-25-test_ecran_oled_i2c_128x64/test_ecran_oled_i2c_128x64_001_lowres.jpg)

![...](/files/2016-05-25-test_ecran_oled_i2c_128x64/test_ecran_oled_i2c_128x64_002_lowres.jpg)

~~~ c++

/*

PROGRAMME BASIQUE POUR TESTER L’ÉCRAN OLED 128×64 I²C

RÉFÉRENCE AliExpress DE L’ÉCRAN
http://fr.aliexpress.com/item/1Pcs-Yellow-blue-double-color-128X64-OLED-LCD-LED-Display-Module-For-Arduino-0-96/32305641669.html

VERSION ORIGINALE DU PROGRAMME
http://www.projetsdiy.fr/ssd1306-mini-ecran-oled-i2c-128x64-arduino/

LIBRAIRIE Adafruit_SSD1306
https://github.com/adafruit/Adafruit_SSD1306.git

CONNEXIONS
GND    GND
VDD    +5V
SCK    pin A5
SDA    pin A4

MICROCONTRÔLEUR
Clone Arduino Nano

REMARQUES
Il faut éditer le fichier Adafruit_SSD1306.h de la manière suivante :
- À la ligne 69, décommenter le code `#define SSD1306_128_64`
- À la ligne 70, commenter le code `#define SSD1306_128_32`

Cet écran est séparé en deux zones verticales
- Une zone de 16 px de haut avec des pixels jaunes
- Une zone de 48 px de haut avec des pixels bleus
Les deux zones sont séparées d’une largeur d’environ
1 pixel qui apparaît donc toujours noire.

La communication I²C fonctionne sans les résistances de pull-up.
Cela dit, il est sans doute préférable d’ajouter deux résistances
de 4.7 kΩ entre SCK et VDD ainsi qu’entre SDA et VDD.


mai 2016, ouilogique.com

*/

#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 4
Adafruit_SSD1306 display( OLED_RESET );

#if( SSD1306_LCDHEIGHT != 64 )
#error( "Height incorrect, please fix Adafruit_SSD1306.h!" );
#endif

void setup()
{
  // Initialise la communication I²C à l’adresse 0x3C.
  display.begin( SSD1306_SWITCHCAPVCC, 0x3C );
  display.clearDisplay();

  // Affiche des textes
  afficheTextes();
}

void loop()
{

}

void afficheTextes( void )
{
  display.setTextSize( 2 );
  display.setTextColor( WHITE );
  display.clearDisplay();

  display.setCursor( 4, 0 );
  display.println( "ouilogique" );

  display.setCursor( 4, 16 );
  display.println( "ouilogique" );

  display.setTextSize( 1 );

  display.setCursor( 35, 32 );
  display.println( "ouilogique" );

  display.setCursor( 35, 40 );
  display.println( "ouilogique" );

  display.setCursor( 35, 48 );
  display.println( "ouilogique" );

  cadreEcran();
  display.display();
}

void cadreEcran( void )
{
  display.drawRect( 0, 0, display.width()-2, display.height()-2, WHITE );
}

~~~
