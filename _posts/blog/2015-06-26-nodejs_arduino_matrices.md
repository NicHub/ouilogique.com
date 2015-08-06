---
layout: post
title: "Commander des Arduino avec Node.js"
modified:
categories: blog
excerpt:
tags: []
image:
  feature:
date: 2015-06-26T17:15:00+01:00
---



Le système est géré avec un Raspberry Pi B+ avec :

- Un serveur Node.js
- Un hotspot WiFi
- Un hub USB sur lequel sont connectés les Arduino

La communication se passe de la façon suivante :

- On connecte l’iPad au réseau WiFi du RPi
- On charge la page web de l’application dans Safari
- On envoie des requêtes de changement de chiffre sur la page web
- Le serveur Node.js reçoit les requêtes et les envoie via RS232 aux Arduino


<iframe width="560" height="315" src="https://www.youtube.com/embed/b8a_t5Tyg44" frameborder="0" allowfullscreen></iframe>



![](/files/2015-06-26-nodejs_arduino_matrices/2015-05-29_platine.jpg)

