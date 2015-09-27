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
---


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ouilogique_1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-5638118185206577"
     data-ad-slot="5843164030"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


J’ai acheté un écran TFT 2.4" chez Banggood :

<http://www.banggood.com/UNO-R3-ATmega328P-Board-2_4-Inch-TFT-LCD-Screen-Module-For-Arduino-p-945755.html>

C’est un écran tactile résistif avec un lecteur de carte micro SD intégré. Le PCB indique [www.mcufriend.com](http://www.mcufriend.com), mais ce site ne répondait pas au moment où j’ai essayé. Je me suis donc armé de patience et après quelques heures et quelques dizaines de recherches sur Google, j’ai réussi a en faire quelque chose.

> Avant de faire quoi que ce soit, il semble que ça soit une bonne idée d’isoler le connecteur USB de l’Arduino UNO avec de l’adhésif Kapton par exemple.

![](/files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_front.jpg)

Pour arriver à ce résultat, il faut tout d’abord télécharger trois librairies d’Adafruit :

- <https://github.com/adafruit/Adafruit-GFX-Library>
- <https://github.com/adafruit/TFTLCD-Library>
- <https://github.com/adafruit/Touch-Screen-Library>

et les mettre dans le dossier des librairies de l’IDE Arduino, par exemple `~/Documents/Arduino/libraries/` sur Mac. Le plus simple est d’exécuter les commandes suivantes dans un terminal :

{% highlight bash %}
cd ~/Documents/Arduino/libraries/
git clone https://github.com/adafruit/Adafruit-GFX-Library.git
git clone https://github.com/adafruit/TFTLCD-Library.git
git clone https://github.com/adafruit/Touch-Screen-Library.git
{% endhighlight %}

Il faut redémarrer l’IDE Arduino pour utiliser les librairies.

La librairie `TFTLCD-Library` contient un dossier `exemples` que vous pouvez copier pour faire des modifications et un dossier `bitmaps`. Les bitmaps peuvent être copiées à la racine d’une carte Micro SD. Celle-ci fonctionne bien pour moi :

<http://www.banggood.com/8GB-Micro-SDTF-Memory-Card-For-Cell-Phone-PDA-MP3-Player-p-926928.html>

> L’écran fonctionne aussi sans carte micro SD. Elle est juste utile pour stocker des bitmaps.


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ouilogique_1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-5638118185206577"
     data-ad-slot="5843164030"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>



## Modification de l’exemple `tftpaint.ino`

> C’est l’exemple `tftpaint` que j’ai utilisé et pas l’exemple `tftpaint_shield`.

À la ligne 47
{% highlight C++ %}
#define YP A3  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 9   // can be a digital pin
#define XP 8   // can be a digital pin
{% endhighlight %}

devient
{% highlight C++ %}
#define YP A1  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 7   // can be a digital pin
#define XP 6   // can be a digital pin
{% endhighlight %}

---

À la ligne 92
{% highlight C++ %}
uint16_t identifier = tft.readID();
{% endhighlight %}

devient
{% highlight C++ %}
uint16_t identifier = 0x9341;
{% endhighlight %}

---

À la ligne 165
{% highlight C++ %}
p.x = map(p.x, TS_MINX, TS_MAXX, tft.width(), 0);
{% endhighlight %}

devient
{% highlight C++ %}
p.x = map(p.x, TS_MINX, TS_MAXX, 0, tft.width());
{% endhighlight %}

---



![](/files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_ouilogique_com.jpg)



## Spécifications

> Source : <http://www.smokeandwires.co.nz/blog/a-2-4-tft-touchscreen-shield-for-arduino/>

| Screen Size | 2.4 inch                            |
| Resolution  | 240 x 320                           |
| LCD Color   | 65k                                 |
| LCD Driver  | ST7781                              |
| Interface   | 8080 8 data bit with 4 control bits |
| Touchscreen | 4 Wire Resistive Touchscreen        |


### Pinout

![](/files/2015-08-14-2-4-in_TFT_Touch_screen/2-4-in_TFT_Touch_screen_back.jpg)


| ARDUINO PIN | LCD SHIELD PIN    | USE                               |
| :--         | :--               | :--                               |
| 3.3V        | 3.3V              | Power                             |
| 5V          | 5V                | Power                             |
| GND         | GND               | Power                             |
| A0          | LCD_RD            | LCD Control                       |
| A1          | LCD_WR  TOUCH_YP  | LCD Control / Touch Data          |
| A2          | LCD_RS  TOUCH_XM  | LCD Control / Touch Data          |
| A3          | LCD_CS            | LCD Control                       |
| A4          | LCD_RST           | LCD Reset                         |
| A5          | ¹                 | -                                 |
| D0          | ¹                 | *(RXD pas utilisé par le shield)* |
| D1          | ¹                 | *(TXD pas utilisé par le shield)* |
| D2          | LCD_D2            | LCD Data                          |
| D3          | LCD_D3            | LCD Data                          |
| D4          | LCD_D4            | LCD Data                          |
| D5          | LCD_D5            | LCD Data                          |
| D6          | LCD_D6 / TOUCH XP | LCD Data/ Touch Data              |
| D7          | LCD_D7 / TOUCH YM | LCD Data / Touch Data             |
| D8          | LCD_D0            | LCD Data                          |
| D9          | LCD_D1            | LCD Data                          |
| D10         | SD_CS             | SD Select                         |
| D11         | SD_DI             | SD Data                           |
| D12         | SD_DO             | SD Data                           |
| D13         | SD_SCK            | SD Clock                          |


&nbsp;

> ¹ On constate que le shield ne laisse que 3 broches libres : A5, D0 et D1. Comme D0 et D1 ne sont pas utilisées, on peut faire communiquer l’Arduino avec un autre système via RS232.

&nbsp;
