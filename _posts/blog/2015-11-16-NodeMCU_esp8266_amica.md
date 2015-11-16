---
layout: page
title: "Mise en route d’une carte <em>Amica</em> avec le firmware NodeMCU et un module WiFi ESP8266"
modified:
categories:
excerpt:
tags: []
image:
     feature: NodeMCU_esp8266_amica.jpg
date: 2015-11-16T14:51:00+01:00
published: true
author: Nico
---



> Voir aussi [l’article sur l’ESP8266 LoLin](/NodeMCU_esp8266/)



# Référence AliExpress

<http://fr.aliexpress.com/item/V2-4M-4FLASH-NodeMcu-Lua-WIFI-Networking-development-board-Based-ESP8266/32448694790.html>



# Premières impressions

- Le chip Silabs CP2102 semble plus rapide que le CH340G utilisé par LoLin.
- Le pinout est différent de LoLin sur la 2<sup>e</sup> et la 3<sup>e</sup> pin en haut à gauche sur l’image du pinout ci-dessous.
- La largeur des cartes Amica et LoLin sont différentes, et leurs deux rangées de pins sont aussi espacées de valeurs différentes :<br/>
LoLin ⇒ 11 × 2.54 = 27.94 mm<br/>
Amica ⇒ 9 × 2.54 = 22.86 mm
- Au premier test, la carte à refusé de communiquer sur le port série. Sur le dessous de la carte, il est indiqué 9600 bauds, mais il me semble qu’en fait c’est 115200 bauds. De toute façon, aucune vitesse ne semblait fonctionner, donc j’ai flashé un nouveau firmware et ça a fonctionné.
- Pour flasher le firmware, j’ai dû appuyer sur le bouton “FLASH” et tout en le maintenant appuyé, presser une fois le bouton “RST”. Sur LoLin, ce n’est pas nécessaire.


![](/files/2015-11-16-NodeMCU_esp8266_amica/NodeMCU_esp8266_amica_001_lowres.jpg)

![](/files/2015-11-16-NodeMCU_esp8266_amica/NodeMCU_esp8266_amica_002_lowres.jpg)

![](/files/2015-11-16-NodeMCU_esp8266_amica/NodeMCU_esp8266_amica_003_lowres.jpg)



# Pinout

![](/files/2015-05-28-pinouts/images/NodeMCU_esp8266_amica_pinout.png)



# Drivers Silabs CP2102

<https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx>

