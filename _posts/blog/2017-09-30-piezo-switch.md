---
layout: page
title: "Bouton piézoélectrique sur Arduino"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-09-30T12:54:00+02:00
published: true
author: Nico
---


## Matériel

- Un Arduino Nano
- Un bouton piézoélectrique (piezo-switch)

## Image

[![WEMOS Sandwich][image-1]][image-1]

[image-1]: ../../files/2017-09-30-piezo-switch/2017-09-30-piezo-switch-001-lowres.jpg

## Fonctionnement

Un bouton piézoélectrique n’envoie qu’une brève impulsion lorsqu’on appuie dessus. On peut donc détecter les pressions de l’utilisateur, mais pas leur durée.

## Câblage

Le bouton que j’ai testé n’a que deux fils que l’on câble comme un bouton mécanique standard, c’est-à-dire avec une résistance de tirage vers le haut (pullup). Pour simplifier le câblage, on peut utiliser une pullup interne de l’Arduino.

## Code

Le code sur GitHub montre trois façons d’utiliser ce bouton avec un Arduino :

- `simple-piezo-switch-001.ino` n’est pas utilisable en tant que tel. Il montre juste que le switch envoie une impulsion et qu’il va falloir être un peu plus malin que ça pour l’utiliser.
- `simple-piezo-switch-002.ino` montre comment faire du _polling_ pour lire le bouton.
- `simple-piezo-switch-003.ino` montre comment utiliser les interruptions.

[https://github.com/NicHub/ouilogique-Arduino/tree/master/piezo-switch][1]

[1]: https://github.com/NicHub/ouilogique-Arduino/tree/master/piezo-switch
