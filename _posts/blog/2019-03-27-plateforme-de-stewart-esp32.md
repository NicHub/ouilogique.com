---
layout: page
title: "Plateforme de Stewart pilotée avec un ESP32"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2019-03-27T17:00:00+01:00
published: true
author: Nico
---

[![Plateforme de Stewart — ouilogique.com][i1]{:style="width:50%;"}][i1]

[i1]: ../../files/plateforme-de-stewart/images/stewart-plateform-ouilogique.jpg


Premiers prototypes d’une plateforme de Stewart que je construis dans le cadre du projet 2019 (P19) du [Microclub][Microclub].


[Microclub]: https://microclub.ch

[cinématique de xoxota99]: https://github.com/xoxota99/stewy


## Code source

**Le code source et quelques détails sur GitHub**

<https://github.com/NicHub/stewart-platform-esp32>


## Quatrième version

Pour la quatrième version, je vais tester un driver I²C de servomoteurs PCA9685.

<https://fr.aliexpress.com/af/32718274859.html>

## Troisième version

Avec un clone de Nunchuck (joystick I²C de la console Wii), des vraie biellettes et des clones de servos Tower Pro MG90s. J’ai abandonné les clones de servos Tower Pro MG996R qui ne fonctionnent vraiment pas bien, car ils sont beaucoup trop lents et consomment trop de courant.

<div style="display:block; margin-bottom:50px;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/1uQ3CkhVr-k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[![Plateforme de Stewart — ouilogique.com][i7]{:style="width:50%;  margin-bottom:100px"}][i7]

[i7]: ../../files/plateforme-de-stewart/images/2019-05-31-proto-plateforme-de-stewart_001.jpg


## Deuxième version

Avec un clone de Nunchuck (joystick I²C de la console Wii), des vraie biellettes et des clones de servos Tower Pro MG996R.

[![Plateforme de Stewart — ouilogique.com][i3]{:style="width:50%; float:left"}][i3]

[i3]: ../../files/plateforme-de-stewart/images/2019-05-03-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i4]{:style="width:50%; float:left"}][i4]

[i4]: ../../files/plateforme-de-stewart/images/2019-05-03-proto-plateforme-de-stewart_002.jpg

[![Plateforme de Stewart — ouilogique.com][i5]{:style="width:50%; float:left"}][i5]

[i5]: ../../files/plateforme-de-stewart/images/2019-05-03-proto-plateforme-de-stewart_003.jpg

[![Plateforme de Stewart — ouilogique.com][i6]{:style="width:50%; float:left; clear:right; margin-bottom:200px;"}][i6]

[i6]: ../../files/plateforme-de-stewart/images/2019-05-03-proto-plateforme-de-stewart_004.jpg



## Première version

Avec un joystick analogique, des biellettes en fil de fer et des clones de servos Tower Pro MG90s.

<div style="display:block; margin-bottom:50px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qbQuXtnF4H4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[![Plateforme de Stewart — ouilogique.com][i2]{:style="width:50%; float:left"}][i2]

[i2]: ../../files/plateforme-de-stewart/images/2019-03-21-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i2b]{:style="width:50%; float:left; clear:right; margin-bottom:100px"}][i2b]

[i2b]: ../../files/plateforme-de-stewart/images/2019-03-21-proto-plateforme-de-stewart_002.jpg




---

## AIDE-MÉMOIRE

Article Wikipedia
  - <https://en.wikipedia.org/wiki/Stewart_platform>

Vidéo qui m’a donné envie de réaliser une plateforme de Stewart
San-José State University
  - <https://www.youtube.com/watch?v=j4OmVLc_oDw>
  - <http://fullmotiondynamics.com>

California Polytechnic University of Pomona — Mechanical Engineering Department — Controls Class Final Project
  - <https://www.youtube.com/watch?v=7Jw8m4pbTYI>

MIPT, Department of Radio Engineering and Cybernetics
2 degrés de liberté + code Arduino
  - <https://www.youtube.com/watch?v=p65XPP53rLo>

Vidéo où l’on voit bien les imperfections métrologiques
  - <https://www.youtube.com/watch?v=QdKo9PYwGaU>
  - Ils utilisent ce controleur de servos
  <https://www.phidgets.com/?tier=3&catid=21&pcid=18&prodid=1032>

Athus Vieira
  - <https://www.linkedin.com/pulse/ball-plate-system-robotic-pid-control-athus-vieira/>
  - <https://www.youtube.com/watch?v=9XhcSSrA4Yc>
  - PID tuning <http://emanual.robotis.com/docs/en/platform/openmanipulator/>

Instructables by moosenee (avec gros plan sur le touch screen) **😃 Avec du code Arduino !**
  - <https://www.instructables.com/id/PID-Controlled-Ball-Balancing-Stewart-Platform/>
  - <https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform>
  - <https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform/blob/master/Readme.pdf>

Instructables by ThomasKNR **😃 Avec du code Arduino !**
  - <https://www.instructables.com/id/Arduino-controlled-Rotary-Stewart-Platform/>
  - <https://github.com/ThomasKNR/RotaryStewartPlatform>

xoxota99/stewy GitHub **😃 Avec du code Arduino !**
  - <https://github.com/xoxota99/stewy>

Chaine YouTube avec une collection d’une vingtaine de vidéos
  - <https://www.youtube.com/playlist?list=PLVNyl3oDY7lsYDQMKvguyPkpJ0Eaqb9z_>

Blender
  - <https://www.youtube.com/watch?v=uNKHX5B011E>

Webots
  - <https://cyberbotics.com/>
  - <https://www.youtube.com/watch?v=ddrtiwjKAaY>

Projet memememememememe **😃 Avec un simulateur fonctionnel en Processing et le code pour RPi !**
  - <https://memememememememe.me/post/stewart-platform-math/>
  - <https://github.com/thiagohersan/memememe>

Cinématique inverse avec servomoteurs **😃 Meilleure source pour les calculs pour l’instant !**
> Méthode de calcul de la cinématique inverse utilisée par le projet memememememememe. C’est la seule méthode qui inclu des servomoteurs en rotation. Les autres proposent systématiquement des actuateurs linéaires.
  - <https://web.archive.org/web/20130506134518/http://www.wokinghamu3a.org.uk/Maths%20of%20the%20Stewart%20Platform%20v5.pdf>

**😃 Autres codes Arduino !**
  - <https://www.marginallyclever.com/product/rotary-stewart-platform-v2/>
  - <https://github.com/MarginallyClever/RotaryStewartPlatform/blob/master/RSPv1/RSPv1.ino>


## PLATEFORME DE STEWART AVEC 3 DEGRÉS DE LIBERTÉ

 - <https://www.instructables.com/id/Ball-Balancing-PID-System/>
 - <https://www.instructables.com/id/3DOF-Ball-on-Plate-Using-Closed-Loop-Stepper-Motor/>
 - <https://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2017/psl58_aw698_eb645/psl58_aw698_eb645/index.html#HLD>


## SPRK: A Low-Cost Stewart Platform For Motion Study In Surgical Robotics

 - <https://goldberg.berkeley.edu/pubs/2018_ISMR_stewart_design.pdf>
 - <https://github.com/BerkeleyAutomation/sprk>


## PLATEFORME DE STEWART AVEC RETOUR DE FORCE

Dynamixel motor
  - <http://www.robotis.us/dynamixel/>

Avec GUI Processing [Arun Dayal Udai]
  - <https://youtu.be/LFpyIZx2QGU?t=221>
  - <https://www.youtube.com/watch?v=rD4kTW_khXQ>
  - <https://www.youtube.com/watch?v=RqUcHulonHk>

Felix Ros **😃 Avec du code Processing et Arduino !**
  - <http://www.felixros.com/>
  - <https://github.com/felixros2401/Stewart-Platform>
  - <https://www.instructables.com/id/Controlling-a-Stewart-Platform/>


## PLATEFORME DE STEWART À BASE CIRCULAIRE (ROTOPOD)

Un rotopod permet de faire une rotation complète sans ajouter un 7e moteur.

Version de Circular-Base-Stewart-Platform

**😃 Il montre un logiciel de tunning des PID dans le 2e lien**
  - <https://www.youtube.com/channel/UCgm1PM2V9BgfP7Qaze1teAw>
  - <https://youtu.be/zna9Hw_Ei58?t=482>

Version commerciale de Mikrolar
  - <http://mikrolar.com/r3000.html>


## Versions commerciales

  - <https://motionsystems.eu/products/>


## Modelling and Simulation of a 6DOF Motion Platform with Permanent Magnet Linear Actuators for Testing in Wind Tunnel

  - <https://www.youtube.com/watch?v=AZjgcrV642c>


## SIMULATEUR SUR MATHEMATICA

  - <https://www.wolfram.com/training/videos/ENG032/>


## MATLAB FORWARD KINEMATICS SOLVER

**😃 Avec du code Matlab !**

  - <https://github.com/jotux/Steward-Platform-Forward-Kinematics-Solver>

PDF à trouver :
  > Forward kinematics of the general 6-6 Stewart platform using algebraic elimination.
  > Authors: Tae-Young Lee, Jae-Kyung Shim
  > Department of Mechanical Engineering, Korea University, 5-Ka Anam-Dong Sungbuk-Ku, Seoul, 136-701, South Korea.
  > 36th issue of Mechanism and Machine Theory magazine (2001, 1073-1085).


## APPLICATIONS MICROCLUB

### Application 1 : Labyrinthe

  - Concours de vitesse de sortie du labyrinthe
    - plusieurs robots s’affrontent en mode auto
    - plusieurs utilisateurs s’affrontent en mode manuel

### Application 2 : Système de stabilisation pour appareil photo

  - Besoin d’un 7e axe pour augmenter l’angle de rotation autour de l’axe Z.

### Application 3 : Ball bouncing

  - <http://poe.olin.edu/2017/Bounce/>
  - <https://github.com/TShapinsky/Bounce>


## IMPLÉMENTATION

### inputs

  - Mesure de la position de la bille par tapis résistif
  - Commande depuis navigateur web
  - Commande depuis Blender
  - BLE via smartphone
  - Joystick cablé (Wii Nunchuck)

### outputs

  - Mouvements du robot (6 ou 7 axes)
  - Retour visuel sur navigateur web
  - Retour visuel sur Blender


## MATÉRIEL

### Servomoteurs

  - Tower Pro MG90s Servos
    - <https://www.banggood.com/6X-Towerpro-MG90S-Metal-Gear-RC-Micro-Servo-p-1072260.html>
    - <https://www.towerpro.com.tw/product/mg90s-3/>
    - <https://www.youtube.com/watch?v=iHPGoKHgzHo>
  - <https://servodatabase.com/>
  - KST DS115MG servos
  - GWS Micro 2BBMG servo (<https://www.youtube.com/watch?v=TgqJbneXZI8>)
  - HS5485HB (<https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform/blob/master/Readme.pdf>)
  - <http://www.robotis.us/dynamixel-mx-64t/> (Utilisé par Arun Dayal Udai)
  - MG995 (<https://www.banggood.com/MG995-High-Torgue-Mental-Gear-Analog-Servo-p-73885.html>) (Rolf)
  - Tower Pro SG-5010 servos (<https://01.org/developerjourney/recipe/building-stewart-platform>)
  - Hitec HS-5625MG (utilisé par <https://github.com/xoxota99/stewy>)
  - MG996R <https://fr.aliexpress.com/item//32636102294.html>
  - Parallax 900-00005 (utilisé par fullmotiondynamics)
    <https://www.parallax.com/product/900-00005>

### Fonctionnement des servos

  - Analogiques <https://www.youtube.com/watch?v=LXURLvga8bQ>
  - <https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/all>


### Driver de servos

  - PCA9685 (16 servos, I²C) <https://aliexpress.com/af/32718274859.html>

### Rotules + tiges

  - M3x100mm <https://aliexpress.com/af/32775630549.html>
  - En M2 <https://aliexpress.com/af/32704692789.html>
  - rotule <https://aliexpress.com/af/32887391192.html>
  - tige <https://aliexpress.com/af/32468820900.html>
  - tige + rotule <https://aliexpress.com/af/32904104171.html>
  - magnétique <https://aliexpress.com/af/32818135577.html>
  - complète <https://aliexpress.com/af/32894390128.html>

### Alim 5V

  - Courant 10A <https://aliexpress.com/af/32810906485.html>

### Levier de servo (Servo horn arm)

  - couleur tritanium <https://aliexpress.com/af/32843432977.html>
  - <https://aliexpress.com/af/32811563669.html>

### Liste complète de matériel

  - <https://01.org/developerjourney/recipe/building-stewart-platform>

### Touch screen

  - Digikey 360-3520-ND <https://www.digikey.ch/short/pj85db> (utilisé par <https://github.com/xoxota99/stewy>)
  - <https://aliexpress.com/af/32809597549.html>

### ESP32

  - WeMos ESP32 WROOM
    - <https://www.banggood.com/fr/WeMos-ESP32-WiFi-Bluetooth-Development-Board-Ultra-Low-Power-Consumption-Dual-Core-ESP-32-ESP-32S-p-1175488.html>

### Joystick

  - Wii Nunchuck <https://aliexpress.com/af/32827461737.html>

### Calculs

  - <https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/geometry/transforming-points-and-vectors>


### PCB

  - <https://jlcpcb.com>

### Système complet avec caméra [Swiftflying Store](https://swiftflying.fr.aliexpress.com/store/3246059)

  - <https://fr.aliexpress.com/item/32957141466.html>

## PINOUT

31 DIRA GPIO14
34 TC5  GPIO13
TC4  GPIO15
STPA
STPB
28 DIRB GPIO25
