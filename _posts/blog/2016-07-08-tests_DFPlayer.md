---
layout: page
title: "Tests de modules DFPlayer"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2016-07-08T16:23:00+02:00
published: true
author: Nico
---


Voici un petit module fort pratique pour lire des fichiers MP3. Il ne coûte presque rien (~8 € pour trois pièces) et il permet d’utiliser des cartes micro SD jusqu’à 32 Go. Il communique via le port série et pour éviter de monopoliser l’unique port série matériel de l’Arduino Nano, la bibliothèque fournie par DFRobot permet d’utiliser facilement un port série logiciel que l’on peut configurer sur à peu près n’importes quelles entrées-sorties digitales. J’ai testé avec les paires 10 & 11 et A0 & A1 et ça fonctionne bien.

> **Et pour que ça fonctionne, il faut croiser les signaux TX et RX :**
> TX Arduino ⇒ RX DFPlayer
> RX Arduino ⇒ TX DFPlayer


À priori, ce module peut être utilisé de 3.2 V à 5 V, mais à 5 V il y a un ronflement prononcé sur le haut-parleur. La solution consiste à placer une résistance de 1 kΩ en série sur la sortie TX de l’Arduino.

Pour la qualité du son, je ne peux pas me prononcer, puisqu’au moment du test, je n’avais pas de haut-parleur sous la main. Mais pour le déverminage, mon buzzer a très bien fait l’affaire avec un son complètement pourri évidemment.

J’ai testé deux cartes micro SD : une de 32 Go et une autre de 8 Go et les deux ont fonctionné sans problème. Le formatage en FAT32 sous OSX avec l’utilitaire de disques n’a pas posé de problème non plus.

![...](/files/2016-07-08-tests_DFPlayer/images/2016-07-08-tests_DFPlayer_001_lowres.jpg)


# Programme d’exemple

<https://github.com/NicHub/ouilogique-Arduino/blob/master/DFPlayer/DFPlayer-test-1/DFPlayer-test-1.ino>

Pour utiliser le programme ci-dessus, il faut installer la bibliothèque `DFPlayer-Mini-mp3` de *DFRobot* :

<https://github.com/DFRobot/DFPlayer-Mini-mp3.git>

> !! Attention, le dépôt Git contient un sous-répertoire `DFPlayer_Mini_Mp3` et c’est lui seul qui doit se trouver dans `~/Documents/Arduino/libraries/` !!



# RÉFÉRENCES
- <http://www.banggood.com/3Pcs-DFPlayer-Mini-MP3-Player-Module-For-Arduino-p-981366.html>
- <http://www.dfrobot.com/wiki/index.php/DFPlayer_Mini_SKU:DFR0299>
- <http://www.dfrobot.com/image/data/DFR0299/DFPlayer%20Mini%20Manul.pdf>
- <http://www.trainelectronics.com/Arduino/MP3Sound/TalkingTemperature/FN-M16P%20Embedded%20MP3%20Audio%20Module%20Datasheet.pdf>

# NOTES

Le DFPlayer communique avec le port série. Comme l’Arduino Nano n’a qu’un UART, la librairie de DFPlayer permet d’utiliser un port série logiciel. À priori, n’importe quelle broche digitale de l’Arduino Nano peut être utilisée à cet effet. J’ai testé avec les couples de broches 10 & 11 ainsi que A0 & A1 et ça fonctionne.

> !!! IL FAUT FAIRE ATTENTION DE CONNECTER LE RX DU DFPlayer AU TX DE L’ARDUINO ET INVERSEMENT POUR LES DEUX AUTRES SIGNAUX !!!

Pour le déverminage, il peut être utile de passer au morceau suivant ou précédent en mettant les broches 11 (IO2) et 9 (IO1) à la masse pour forcer la lecture.

Si on a pas de haut-parleur, un buzzer peut faire l’affaire lors de la mise en route.


# NOTES SUR LA  CARTE SD

- Jusqu’à 32 Go (testé avec 32 Go ⇒ OK)
- Formaté en FAT16 ou en FAT32 (testé FAT32 formaté avec OSX ⇒ OK)
- Doit contenir un répertoire appelé “mp3”
- Le répertoire appelé “mp3” peut optionnellement contenir des répertoires appelés “001”, “002”, ...
- Les noms des fichiers doivent commencer par 4 digits et finir par l’extension “.mp3”

~~~
	/Volumes/DFPLAYER/mp3
	├── 0001×××.mp3
	├── 0002×××.mp3
	├── 0003×××.mp3
	├── 0004×××.mp3
~~~

## CONNEXIONS DFPlayer

	VCC   (pin 1)     ⇒     5V Arduino Nano
	RX    (pin 2)  ¹  ⇒     software TX Arduino Nano (pin 10) ²
	TX    (pin 3)     ⇒     software RX Arduino Nano (pin 11) ³
	SPK2  (pin 6)     ⇒     Haut-parleur - (ou buzzer -)
	GND   (pin 7)     ⇒     GND Arduino Nano
	SPK1  (pin 8)     ⇒     Haut-parleur + (ou buzzer +)

¹ Ajouter une résistance de 1 kΩ en série pour éviter les ronflements
² fonctionne aussi sur A0
³ fonctionne aussi sur A1

