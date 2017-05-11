---
layout: page
title: "Mise en route d’un Arduino Pro Mini 3.3 V"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2016-11-14T16:00:00+01:00
published: true
author: Nico
---


L’Arduino Pro Mini n’a pas d’UART visible sur le port USB de l’ordinateur qui va le programmer. On doit donc utiliser un programmateur externe. Dans cet article, je présente deux solutions :

- [Programmation de l’Arduino Pro Mini avec un Arduino UNO (mode Arduino as ISP)](#prog1)
- [Programmation de l’Arduino Pro Mini avec un convertisseur USB-série](#prog2)



## Matériel

- [ATmega328P-AU Pro Mini 3.3V 8MHz (oscillateur interne ⇒ pas de quartz), acheté chez Banggood pour 13 $ les 5 pièces][1]
- [Programmateur FTDI][3]

{: #prog1 }
## Programmation de l’Arduino Pro Mini avec un Arduino UNO (mode Arduino as ISP)


La définition des fusibles dans l’IDE 1.6.12 pour `Arduino Pro or Pro Mini` a un problème et l’IDE renvoie l’erreur suivante quand on veut graver un nouveau bootloader :

{% highlight bash %}
 ***failed;
avrdude: WARNING: invalid value for unused bits in fuse "efuse", should be set to 1 according to datasheet
This behaviour is deprecated and will result in an error in future version
You probably want to use 0xfd instead of 0x05 (double check with your datasheet first).
{% endhighlight %}

Donc, je mes suis rabattu sur MiniCore : <https://github.com/MCUdude/MiniCore>, d’après la suggestion trouvée à <http://arduino.stackexchange.com/a/31199/13995>.

La procédure d’utilisation est très bien détaillée sur la page GitHub de MiniCore, donc je ne la répète pas ici.

La configuration que j’ai utilisée est la suivante :

![Configuration MiniCore programmation d’Arduino Pro Mini][7]

![Programmation d’Arduino Pro Mini][8]

La programmation ISP fonctionne nickel, mais je n’arrive pas à [utiliser l’ESP8266 comme bridge USB‑RS232][9].

⚠ Comme j’ai Arduino Pro Mini 3.3 V, j’ai connecté le 5 V du UNO sur l’entrée RAW du Pro Mini, car cette entrée est connectée à un régulateur de tension qui accepte de 3.3 à 12 V. Si on a du 3.3 V déjà régulé, on peut utiliser la broche `VCC`. [Voir le brochage][4].

### Brochage

| UNO | Pro Mini |
| :-: | :-:      |
| 5V  | RAW  ⚠   |
| GND | GND      |
| 10  | RST      |
| 11  | 11       |
| 12  | 12       |
| 13  | 13       |


{: #prog2 }
## Programmation de l’Arduino Pro Mini avec un convertisseur USB-série MiniInTheBox

J’ai également fait un test de programmation avec [un convertisseur USB-série][3]. Là aussi, j’ai dû utiliser MiniCore avec les paramètres détaillés dans le chapitre précédent. La seule chose qui change, c’est qu’il faut téléverser le programme avec la commande `Croquis/Téléverser ⌘+U`, alors qu’avec le UNO comme programmateur, il fallait utiliser la commande `Croquis/Téléverser avec un programmateur ⇧+⌘+U`.

![convertisseur USB-série][6]

![Arduino Pro Mini][11]

![Arduino Pro Mini Back][12]

![Arduino Pro Mini + convertisseur USB-série][5]

<!--

{: #prog3 }
## Programmation de l’Arduino Pro Mini avec un convertisseur USB-série Banggood

Et j’ai aussi testé un [convertisseur USB-série de chez Banggood][13] qui a l’avantage de se présenter sous la forme d’un cordon USB entièrement isolé. Il est aussi livré avec un connecteur 5 broches fort pratique.

Par contre les fils ne sont pas branchés dans le bon ordre, donc il faut corriger cela selon la table ci-dessous :

| Arduino Pro Mini | Convertisseur |
| :-               | :-            |
| BLK              | blue CTS      |
| GND              | black GND     |
| VCC              | red 5V        |
| RXI              | green TXD     |
| TX0              | white RXD     |
| GRN              | yellow RTS    |


| Arduino Pro Mini | Convertisseur |
| :-               | :-            |
| BLK              | black GND     |
| GND              | blue CTS      |
| VCC              | red 5V        |
| RXI              | green TXD     |
| TX0              | white RXD     |
| GRN              | yellow RTS    |


-->


[1]: http://www.banggood.com/5Pcs-3_3V-8MHz-ATmega328P-AU-Pro-Mini-Microcontroller-Board-For-Arduino-p-980292.html?p=0431091025639201412F

[2]: https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v

[3]: http://www.miniinthebox.com/fr/programme-downloader-ftdi-basic-usb-a-ttl-ft232-pour-arduino_p903425.html

[4]: /pinouts/#pinout-arduino-pro-mini

[5]: ../../files/2016-11-14-arduino-pro-mini/arduino-pro-mini-usb-serial_lowres.jpg

[6]: ../../files/2016-11-14-arduino-pro-mini/usb-serial-converter_lowres.jpg

[7]: ../../files/2016-11-14-arduino-pro-mini/config_MiniCore.png

[8]: ../../files/2016-11-14-arduino-pro-mini/arduino-pro-mini-arduino-uno_lowres.jpg

[9]: /usb-rs232_bridge_microcontroleurs/

[10]: ../../files/2016-11-14-arduino-pro-mini/arduino-pro-mini-arduino-uno_lowres.jpg

[11]: ../../files/2016-11-14-arduino-pro-mini/arduino-pro-mini_lowres.jpg

[12]: ../../files/2016-11-14-arduino-pro-mini/arduino-pro-mini-back.jpg

[13]: https://www.banggood.com/6Pin-FTDI-FT232RL-USB-To-Serial-Adapter-Module-USB-TO-TTL-RS232-Arduino-Cable-p-1035802.html?p=0431091025639201412F

