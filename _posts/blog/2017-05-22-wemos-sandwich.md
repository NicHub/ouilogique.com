---
lang: fr
layout: page
title: "Sandwich de WEMOS"
modified:
categories:
excerpt:
tags: []
image:
    feature:
date: 2017-05-22T11:57:00+02:00
published: true
author: Nico
---

## Matériel

Étage 1 : [Battery Shield][1]
Étage 2 : [WEMOS ESP8266 V2][2]
Étage 3 : [Relay Shield][3]
Étage 4 : [nRF24][4a] custom shield avec [condensateur 2200 µF][4b]
Étage 5 : [DHT11 Shield][5]

## Notes

J’ai réalisé ce montage juste pour le plaisir des yeux. Il n’a pas d’utilité particulière dans cette configuration, mais tous les éléments fonctionnent.

J’ai réalisé le _shield nRF24_ moi-même. Pour le brochage, voir [la page sur le nRF24][4c].

Pour les connexions, j’ai utilisé des [Long 8-pin Headers][6] qui sont forts pratiques. Ils permettent également de séparer les éléments trop hauts comme le relai.

## Images

[![WEMOS Sandwich][image-1]][image-1]

[![WEMOS Sandwich][image-2]][image-2]

[image-1]: ../../files/2017-05-22-wemos-sandwich/wemos-sandwich-001.jpg
[image-2]: ../../files/2017-05-22-wemos-sandwich/wemos-sandwich-002.jpg
[1]: https://www.banggood.com/WeMos-D1-Mini-Single-Lithium-Battery-Charging-And-Battery-Boost-Shield-p-1092773.html?p=0431091025639201412F
[2]: https://www.banggood.com/WeMos-D1-Mini-V2-NodeMcu-4M-Bytes-Lua-WIFI-Internet-Of-Things-Development-Board-Based-ESP8266-p-1115398.html?p=0431091025639201412F
[3]: https://www.banggood.com/DC-5V-1CH-Relay-Shield-V2-Version-2-For-WEMOS-D1-Mini-ESP8266-WiFi-Module-p-1102379.html?p=0431091025639201412F
[4a]: https://fr.aliexpress.com/item/2pcs-lot-Special-promotions-1100-meter-long-distance-NRF24L01-PA-LNA-wireless-modules-with-antenna/32246689488.html
[4b]: https://fr.aliexpress.com/item/1LOT-10PCS-Aluminum-Capacitors-2200uF-228-20-10-17mm-10V-2200000nF-2200000000pF-Diameter10mm/32707549315.html
[4c]: https://ouilogique.com/tests_nRF24L01+/#nrf24l01-sur-esp8266
[5]: https://www.banggood.com/DHT11-Single-Bus-Digital-Temperature-Humidity-Sensor-Shield-For-WeMos-D1-Mini-p-1050049.html?p=0431091025639201412F
[6]: https://fr.aliexpress.com/item/Free-shipping-60Pcs-lot-2-54MM-6Pin-8Pin-10Pin-10MM-Long-Needle-Female-Pin-Header-Strip/32684334510.html
