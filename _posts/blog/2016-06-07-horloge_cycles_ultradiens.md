---
layout: page
title: "Horloge à cycles ultradiens"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2016-06-07T10:13:00+02:00
published: true
author: Nico
---

![...](/files/horloge_cycles_ultradiens/images/horloge_cycles_ultradiens_002_lowres.jpg)

## Description du programme

_**Téléchargez le code source ici :** [horloge_cycles_ultradiens.ino + aTunes.h](https://github.com/NicHub/ouilogique.com/tree/gh-pages/files/horloge_cycles_ultradiens)_

C’est une horloge qui affiche les pourcentages d’attention par cycles d’une heure et demie. On définit la valeur de la constante `heureAttentionMax` au nombre de secondes du pic d’attention du cycle. Par exemple, si votre cycle a un pic à 7 h 15 (= 26100 s), cela correspond à `heureAttentionMax = 26100 % 5400 = 4500` où `%` est l’opérateur *modulo* et 5400 est le nombre de secondes dans 1 h 30. La constante `heureAttentionMax` doit être ajustée manuellement dans le programme.

L’horloge peut être mise à jour via le port RS232. Comme le programme utilise beaucoup de RAM, j’ai désactivé cette fonctionnalité par défaut. Pour la réactiver, il suffit de changer la valeur de `avecSerial false` à `avecSerial true` à la ligne 46 et de recharger le programme sur le microcontrôleur.

## Notes

- Les pullups ont une résistance de 4.7 kΩ.
- Le carillon sonne lorsque le cycle est à 100 %.
- Le bouton connecté à `D2` permet d’activer ou de désactiver le carillon.

## Voir aussi

- [Test d’une horloge temps réel DS1307 I²C](http://ouilogique.com/test_horloge_temps_reel_i2c/)
- [Test d’un écran OLED 128×64 I²C](http://ouilogique.com/test_ecran_oled_i2c_128x64/)
