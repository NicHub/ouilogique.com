---
layout: page
title: 'Test d’un écran TFT 2.4"'
modified:
categories:
excerpt:
tags: []
image:
    feature: TFT_screen_2.jpg
date: 2015-07-14T14:20:00+01:00
published: true
author: Nico
redirect_from:
    - /blog/2-4-in_TFT_Touch_screen/
---

J’ai acheté un écran TFT 2.4" chez Banggood :

<https://www.banggood.com/UNO-R3-ATmega328P-Board-2_4-Inch-TFT-LCD-Screen-Module-For-Arduino-p-945755.html?p=0431091025639201412F>

C’est un écran tactile résistif avec un lecteur de carte micro SD intégré. Le PCB indique [www.mcufriend.com](https://www.mcufriend.com), mais ce site ne répondait pas au moment où j’ai essayé. Je me suis donc armé de patience et après quelques heures et quelques dizaines de recherches sur Google, j’ai réussi à en faire quelque chose.

> Avant de faire quoi que ce soit, il semble que ça soit une bonne idée d’isoler le connecteur USB de l’Arduino UNO avec de l’adhésif Kapton par exemple.

[![mcufriend LCD touch screen][1]][1]

Pour arriver à ce résultat, il faut tout d’abord télécharger trois librairies d’Adafruit :

-   <https://github.com/adafruit/Adafruit-GFX-Library>
-   <https://github.com/adafruit/TFTLCD-Library>
-   <https://github.com/adafruit/Touch-Screen-Library>

et les mettre dans le dossier des librairies de l’IDE Arduino, par exemple `~/Documents/Arduino/libraries/` sur Mac. Le plus simple est d’exécuter les commandes suivantes dans un terminal :

```bash
cd ~/Documents/Arduino/libraries/
git clone https://github.com/adafruit/Adafruit-GFX-Library.git
git clone https://github.com/adafruit/TFTLCD-Library.git
git clone https://github.com/adafruit/Touch-Screen-Library.git
```

Il faut redémarrer l’IDE Arduino pour utiliser les librairies.

La librairie `TFTLCD-Library` contient un dossier `exemples` que vous pouvez copier pour faire des modifications et un dossier `bitmaps`. Les bitmaps peuvent être copiées à la racine d’une carte Micro SD. Celle-ci fonctionne bien pour moi :

~~www.banggood.com/8GB-Micro-SDTF-Memory-Card-For-Cell-Phone-PDA-MP3-Player-p-926928.html?p=0431091025639201412F~~

> L’écran fonctionne aussi sans carte micro SD. Elle est juste utile pour stocker des bitmaps.

## Modification de l’exemple `tftpaint.ino`

> C’est l’exemple `tftpaint` que j’ai utilisé et pas l’exemple `tftpaint_shield`.

À la ligne 47

```c++
#define YP A3  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 9   // can be a digital pin
#define XP 8   // can be a digital pin
```

devient

```c++
#define YP A1  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 7   // can be a digital pin
#define XP 6   // can be a digital pin
```

---

À la ligne 92

```c++
uint16_t identifier = tft.readID();
```

devient

```c++
uint16_t identifier = 0x9341;
```

---

À la ligne 165

```c++
p.x = map(p.x, TS_MINX, TS_MAXX, tft.width(), 0);
```

devient

```c++
p.x = map(p.x, TS_MINX, TS_MAXX, 0, tft.width());
```

---

[![mcufriend LCD touch screen][2]][2]

## Spécifications

> Source : ~~www.smokeandwires.co.nz/blog/a-2-4-tft-touchscreen-shield-for-arduino/~~

| Screen Size | 2.4 inch |
| Resolution | 240 x 320 |
| LCD Color | 65k |
| LCD Driver | ST7781 |
| Interface | 8080 8 data bit with 4 control bits |
| Touchscreen | 4 Wire Resistive Touchscreen |

### Pinout

[![mcufriend LCD touch screen][3]][3]

| ARDUINO PIN | LCD SHIELD PIN    | USE                      |
| :---------- | :---------------- | :----------------------- |
| 3.3V        | 3.3V              | Power                    |
| 5V          | 5V                | Power                    |
| GND         | GND               | Power                    |
| A0          | LCD_RD            | LCD Control              |
| A1          | LCD_WR TOUCH_YP   | LCD Control / Touch Data |
| A2          | LCD_RS TOUCH_XM   | LCD Control / Touch Data |
| A3          | LCD_CS            | LCD Control              |
| A4          | LCD_RST           | LCD Reset                |
| A5 ¹        | ¹                 | -                        |
| D0 ¹        | ¹                 | -                        |
| D1 ¹        | ¹                 | -                        |
| D2          | LCD_D2            | LCD Data                 |
| D3          | LCD_D3            | LCD Data                 |
| D4          | LCD_D4            | LCD Data                 |
| D5          | LCD_D5            | LCD Data                 |
| D6          | LCD_D6 / TOUCH XP | LCD Data/ Touch Data     |
| D7          | LCD_D7 / TOUCH YM | LCD Data / Touch Data    |
| D8          | LCD_D0            | LCD Data                 |
| D9          | LCD_D1            | LCD Data                 |
| D10 ²       | SD_CS ²           | SD Select                |
| D11 ²       | SD_DI ²           | SD Data                  |
| D12 ²       | SD_DO ²           | SD Data                  |
| D13 ²       | SD_SCK ²          | SD Clock                 |

&nbsp;

> ¹ On constate que le shield ne laisse que 3 broches libres : A5, D0 et D1. Comme D0 et D1 ne sont pas utilisées, on peut faire communiquer l’Arduino avec un autre système via RS232.

> ² Si on n’utilise pas la carte SD, on peut libérer les 4 broches D10 à D13 (bus SPI), ce qui fait un total de 7 broches libres.

&nbsp;

## LCD Drivers

Les deux drivers LCD sont des TM74HC245.

[Datasheet en chinois](https://www.szjdf.net/Private/ProductFiles/595775de665f4acba6a1.pdf)
Datasheet traduite par Google ~~goo.gl/hKB7W1~~

[![TM74HC245][10]][10]

[1]: ../../files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_front.jpg
[2]: ../../files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_ouilogique_com.jpg
[3]: ../../files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_back.jpg
[10]: ../../files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_ouilogique_TM74HC245_videoinverse.jpg
