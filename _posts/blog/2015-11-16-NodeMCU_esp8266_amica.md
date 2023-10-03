---
author: Nico
date: 2015-11-16 14:51:00+01:00
image:
    feature: NodeMCU_esp8266_amica.jpg
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title:
    Mise en route d’une carte <em>Amica</em> avec le firmware NodeMCU et un module
    WiFi ESP8266
---

> Voir aussi [l’article sur l’ESP8266 LoLin](/NodeMCU_esp8266/)

## Référence AliExpress

-   ~~http://fr.aliexpress.com/item/V2-4M-4FLASH-NodeMcu-Lua-WIFI-Networking-development-board-Based-ESP8266/32448694790.html~~

## Installation du pilote pour le Silabs CP2102

-   ~~https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx~~

La version _4.x.13 - August 31_, 2016 fonctionne sous macOS Sierra.

## Premières impressions

-   Le chip Silabs CP2102 semble plus rapide que le CH340G utilisé par LoLin.
-   Le pinout est différent de LoLin sur la 2<sup>e</sup> et la 3<sup>e</sup> pin en haut à gauche sur l’image du pinout ci-dessous.
-   Les largeurs des cartes Amica et LoLin sont différentes, et leurs deux rangées de pins sont aussi espacées de valeurs différentes :<br/>
    LoLin ⇒ 11 × 2.54 = 27.94 mm<br/>
    Amica ⇒ 9 × 2.54 = 22.86 mm
-   Au premier test, la carte a refusé de communiquer sur le port série. Sur le dessous de la carte, il est indiqué 9600 bauds, mais il me semble qu’en fait c’est 115200 bauds. De toute façon, aucune vitesse ne semblait fonctionner, donc j’ai flashé un nouveau firmware et ça a fonctionné.
-   Pour flasher le firmware, j’ai dû appuyer sur le bouton “FLASH” et tout en le maintenant appuyé, presser une fois le bouton “RST”. Sur LoLin, ce n’est pas nécessaire.
-   Les barrettes de pins ne sont pas perpendiculaires au PCB, mais ça entre quand même dans un breadboard.
-   Cette carte a deux LED : une bleue sur GPIO 4 à côté de l’antenne et une rouge sur GPIO 0 à 7 mm du bouton “RST”. La carte LoLin n’a que la LED bleue.

[![ouilogique.com][img_1]][img_1]

[img_1]: ../../files/2015-11-16-NodeMCU_esp8266_amica/images/NodeMCU_esp8266_amica_001_lowres.jpg

[![ouilogique.com][img_2]][img_2]

[img_2]: ../../files/2015-11-16-NodeMCU_esp8266_amica/images/NodeMCU_esp8266_amica_002_lowres.jpg

[![ouilogique.com][img_3]][img_3]

[img_3]: ../../files/2015-11-16-NodeMCU_esp8266_amica/images/NodeMCU_esp8266_amica_003_lowres.jpg

## Pinout

[![ouilogique.com][img_4]][img_4]

[img_4]: ../../files/2015-05-28-pinouts/images/NodeMCU_esp8266_amica_pinout.png

## Vitesse de la liaison série

Le test consiste à flasher un firmware identique sur LoLin et Amica et de comparer les temps nécessaires.

### Script de flashage

```bash
#!/bin/bash

# USBPORT=/dev/cu.SLAB_USBtoUART
USBPORT=/dev/tty.wchusbserial14140
FIRMWARE=nodemcu_integer_0.9.6-dev_20150704.bin
esptool.py           \
    --port $USBPORT  \
    --baud 230400    \
    write_flash      \
    --flash_mode qio \
    --flash_size 32m \
    --flash_freq 40m \
    0x00000 $FIRMWARE
```

### Résultat LoLin

```bash
Connecting...
Erasing flash...
Wrote 450560 bytes at 0x00000000 in 33.2 seconds (108.6 kbit/s)...

Leaving...
```

### Résultat Amica

```bash
Connecting...
Erasing flash...
Wrote 450560 bytes at 0x00000000 in 22.8 seconds (158.0 kbit/s)...

Leaving...
```

### Conclusion

Le chip Silabs CP2102 est 50 % plus rapide que le CH340G ! J’ai réalisé ce test sur mon MacBook Pro (Retina, 13 pouces, mi-2014, 2.8 GHz Intel Core i5, 8 Go 1600 MHz DDR3) avec un hub USB [Delock 61857](http://www.delock.de/produkte/S_61857/merkmale.html).

## Drivers Silabs CP2102

-   ~~https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx~~
