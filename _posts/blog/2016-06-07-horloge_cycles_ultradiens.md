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

![...](/files/horloge_cycles_ultradiens/horloge_cycles_ultradiens_lowres.jpg)

Le programme se trouve ici :

<https://github.com/NicHub/ouilogique.com/blob/gh-pages/files/horloge_cycles_ultradiens/horloge_cycles_ultradiens.ino>


## Description du programme

C’est une horloge qui affiche des cycles de 1 h 30. On définit la valeur de la constante `heureMax` au nombre de secondes du pic du cycle. Par exemple, si votre cycle a un pic à 7 h 15 (= 26100 s), le cycle a son pic à `heureMax = 26100 % 5400 = 4500` où `%` est l’opérateur *modulo* et 5400 est le nombre de secondes dans 1 h 30. La constante `heureMax` doit être adaptée manuellement dans le programme à la ligne 192.

L’horloge peut être mise à jour via le port RS232. Comme le programme utilise beaucoup de RAM, j’ai désactivé cette fonctionnalité par défaut. Pour la réactiver, il suffit de changer la valeur de `avecSerial false` à `avecSerial true` à la ligne 46 et de recharger le programme sur le microcontrôleur.

## Notes

- Les pullups ont une résistance de 4.7 Ω.
- Le bouton sur `D2` n’est pas utilisé dans le programme.
- Le buzzer sur `A0` non plus.

