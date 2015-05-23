---
layout: post
title: "LEDs adressables"
excerpt: "LEDs adressables"
categories: blog
tags: [LED, PWM, NeoPixel, FastLED]
author: Nicolas
comments: true
share: true
image:
  feature: 2015-02-23_microDelta_002.jpg
published: true
---



Pour mon [projet de programmation d’un MSP430 en mode ISP](/blog/programmer_un_msp430_en_mode_ISP/), j’ai utilisé une LED RGB. C’est simplement trois LEDs dans un seul boîtier avec quatre pattes : une pour chaque couleur et une pour la masse.

Jusque là, rien de bien méchant. Mais comme je n’avais qu’une LED de ce type et que je l’ai soudée sur mon [Perma-Proto d’Adafruit](http://www.adafruit.com/blog/2011/11/18/adafruit-perma-proto-half-sized-breadboard-pcb-3-pack/), il m’en fallait des nouvelles. Ni une, ni deux, j’ai commandé quatre [LEDs P9823-F8](http://shop.boxtec.ch/led-neopixel-8mm-p9823-p-42265.html)  chez Boxtec.

![](/files/2015-05-22-leds_adressables/images/67053.jpg)

Mal m’en a pris, elles ne sont pas du tout du même type que ma LED RGB de base. En fait ce sont des LED adressables en PWM. Eh oui, elles contiennent de la logique capable de comprendre un signal PWM et de s’allumer en conséquence. Avec en plus la possibilité d’être mise en série.

Pour la programmation sur Arduino, j’ai trouvé deux librairies :


- [NeoPixels d’Adafruit](https://github.com/adafruit/Adafruit_NeoPixel)
- [FastLED](http://fastled.io)


