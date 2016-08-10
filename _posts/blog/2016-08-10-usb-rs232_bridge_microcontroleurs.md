---
layout: page
title: "Utiliser des cartes à microcontrôleurs comme bridge USB&#8209;RS232"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2016-08-10T10:34:00+02:00
published: true
author: Nico
---

L’idée est de déterminer s’il est possible d’utiliser une carte à microcontrôleur comme le Launchpad, l’Arduino Nano ou l’ESP8266 pour remplacer un bridge USB-RS232.

# Essai avec Launchpad

## Programmation des Launchpad

{% highlight C++ %}
/*
  serial_end.ino

  Ce programme arrête la gestion du port série par le
  microcontrôleur. Contrairement à ce que suggère la
  documentation¹, cela permet d’envoyer RX et TX depuis l’USB vers
  les pins correspondantes sans pertes. Si on n’arrête pas
  le port série, il se peut que des caractères ne soient pas
  transmis, mais ce comportement n’est pas reproductible et ce
  programme permet de rendre le comportement fiable.

  L’idée m’est venue après avoir lu cette réponse sur
  StackExchange : http://goo.gl/ngbV6Q

  ¹ https://www.arduino.cc/en/Serial/End
*/

void setup()
  { Serial.end(); }
void loop()
  {}
{% endhighlight %}

## Branchements

Deux Launchpad avec RX connecté à TX et inversement. GND à GND. Les cavaliers RXD et TXD connectés horizontalement (mode `HW UART` selon le pictogramme à côté des cavaliers).

![Branchement des Launchpad](/files/2016-08-10-usb-rs232_bridge_microcontroleurs/branchement_launchpad_lowres.jpg)

## Résultat

On peut envoyer des commandes d’un Launchpad vers l’autre via CoolTerm et ça marche à 115200 bauds (voir en bas des captures d’écran de CoolTerm) alors même que le MSP430 ne supporte pas des vitesses supérieures à 9600 bauds ⇒ Cool !

![CoolTerm Launchpad 1](/files/2016-08-10-usb-rs232_bridge_microcontroleurs/coolterm_launchpad_1.png)

![CoolTerm Launchpad 2](/files/2016-08-10-usb-rs232_bridge_microcontroleurs/coolterm_launchpad_2.png)

## Sans le microcontrôleur

Ça marche aussi si on enlève le microcontrôleur

![Branchement des Launchpad sans MSP430](/files/2016-08-10-usb-rs232_bridge_microcontroleurs/branchement_launchpad_sans_msp430_lowres.jpg)
