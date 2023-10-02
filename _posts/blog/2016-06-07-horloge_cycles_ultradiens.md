---
author: Nico
date: 2016-06-07 10:13:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Horloge à cycles ultradiens
---

## Version pour Arduino Nano

**Première version avec un bouton poussoir**

[![Horloge à cycles ultradiens — Arduino Nano][img_1]][img_1]

[img_1]: ../../files/2016-06-07-horloge_cycles_ultradiens/images/horloge_cycles_ultradiens_002_lowres.jpg

**Deuxième version avec un encodeur rotatif KY-040**

> L’encodeur rotatif peut être remplacé par un simple bouton poussoir pour l’instant parce que je n’utilise que cette fonction. J’ai commencé à tester cet encodeur avec le traceur série de l’IDE Arduino et [le programme de test se trouve sur mon GitHub](https://github.com/NicHub/ouilogique-Arduino/blob/master/encodeur-rotatif-KY-040/encodeur-rotatif-KY-040-test-1/encodeur-rotatif-KY-040-test-1.ino). Je modifierai bientôt le programme de l’horloge pour y intégrer un menu que l’on pourra utiliser avec l’encodeur.

[![Horloge à cycles ultradiens — Arduino Nano][img_2]][img_2]

[img_2]: ../../files/2016-06-07-horloge_cycles_ultradiens/images/horloge_cycles_ultradiens_004_lowres.jpg

### Code source

[horloge-cycles-ultradiens-arduino.ino + aTunes.h](https://github.com/NicHub/ouilogique-Arduino/tree/master/horloge-cycles-ultradiens-arduino)

### Description du programme

C’est une horloge qui affiche les pourcentages d’attention par cycles d’une heure et demie. On définit la valeur de la constante `heureAttentionMax` au nombre de secondes du pic d’attention du cycle. Par exemple, si votre cycle a un pic à 7 h 15 (= 26100 s), cela correspond à `heureAttentionMax = 26100 % 5400 = 4500` où `%` est l’opérateur _modulo_ et 5400 est le nombre de secondes dans 1 h 30. La constante `heureAttentionMax` doit être ajustée manuellement dans le programme.

L’heure de horloge temps réel DS1307 peut être mise à jour via le port RS232. Comme le programme utilise beaucoup de RAM, j’ai désactivé cette fonctionnalité par défaut. Pour la réactiver, il suffit de changer la valeur de `avecSerial false` à `avecSerial true` à la ligne 46 et de recharger le programme sur le microcontrôleur.

### Notes

-   Les pullups ont une résistance de 4.7 kΩ.
-   Le carillon sonne lorsque le cycle est à 100 %.
-   Le bouton connecté à `D2` permet d’activer ou de désactiver le carillon.

### Voir aussi

-   [Test d’une horloge temps réel DS1307 I²C](https://ouilogique.com/test_horloge_temps_reel_i2c/)
-   [Test d’un écran OLED 128×64 I²C](https://ouilogique.com/test_ecran_oled_i2c_128x64/)

## Version pour ESP8266

La version pour l’ESP8266 synchronise l’heure de horloge temps réel DS1307 avec un serveur NTP.

[![Horloge à cycles ultradiens — ESP8266][img_3]][img_3]

[img_3]: ../../files/2016-06-07-horloge_cycles_ultradiens/images/horloge_cycles_ultradiens_003_lowres.jpg

### Code source

-   <https://github.com/NicHub/ouilogique-ESP8266-Arduino/tree/master/horloge-cycles-ultradiens-esp8266>
