---
author: Nico
date: 2019-03-27 17:00:00+01:00
image:
    feature: banner_2019-03-27-plateforme-de-stewart-esp32.jpg
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Plateforme de Stewart pilotée avec un ESP32
---

[![Plateforme de Stewart — ouilogique.com][i1]{:style="width:50%;"}][i1]

[i1]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/stewart-plateform-ouilogique.jpg

Premiers prototypes d’une plateforme de Stewart que je construis dans le cadre du projet 2019 (P19) du [Microclub][microclub].

[microclub]: https://microclub.ch
[cinématique de xoxota99]: https://github.com/xoxota99/stewy

## Code source

**Le code source et quelques détails sur GitHub**

-   <https://github.com/NicHub/stewart-platform-esp32>

## Quatrième version

Pour la quatrième version, je ne génère plus le PWM des servos avec l’ESP32, mais avec un
[driver I²C PCA9685](https://www.adafruit.com/product/815).

[![Plateforme de Stewart — ouilogique.com][i8]{:style="width:100%;"}][i8]

[i8]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2021-04-24-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i9]{:style="width:100%;"}][i9]

[i9]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2021-04-24-proto-plateforme-de-stewart_002.jpg

<iframe width="799" height="449" src="https://www.youtube-nocookie.com/embed/1ll8JVwJC50?si=UcQgFnI2AXPPRVbU" title="YouTube video player" frameborder="0" allow="web-share" allowfullscreen></iframe>

<br>

> Changement de bande adhésive pour tenir le câble du Nunshunk et ajout d’un condensateur de 10 µF entre la broches RST et GND qui permet de [ne plus être obligé de presser sur BOOT lorsqu’on flashe l’ESP].

[ne plus être obligé de presser sur BOOT lorsqu’on flashe l’ESP]: ../ne-pressez-plus-sur-boot-pour-flasher-un-esp/

[![Plateforme de Stewart — ouilogique.com][i10]{:style="width:100%;"}][i10]

[i10]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2024-04-14-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i11]{:style="width:100%;"}][i11]

<!-- Layout 2×2 -->

[i11]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2024-04-14-proto-plateforme-de-stewart_002.jpg

[![Plateforme de Stewart — ouilogique.com][i12]{:style="width:50%; float:left"}][i12]

[i12]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2023-01-30-proto-plateforme-de-stewart_003.jpg

[![Plateforme de Stewart — ouilogique.com][i13]{:style="width:50%; float:left"}][i13]

[i13]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2023-01-30-proto-plateforme-de-stewart_004.jpg

[![Plateforme de Stewart — ouilogique.com][i14]{:style="width:50%; float:left"}][i14]

[i14]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2023-01-30-proto-plateforme-de-stewart_005.jpg

[![Plateforme de Stewart — ouilogique.com][i15]{:style="width:50%; float:left; clear:right; margin-bottom:200px;"}][i15]

[i15]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2023-01-30-proto-plateforme-de-stewart_006.jpg

## Troisième version

Avec un clone de Nunchuck (joystick I²C de la console Wii), des vraie biellettes et des clones de servos Tower Pro MG90s.
J’ai abandonné les clones de servos Tower Pro MG996R qui ne fonctionnent vraiment pas bien, car ils sont beaucoup trop lents et consomment trop de courant.

<iframe width="799" height="449" src="https://www.youtube-nocookie.com/embed/1uQ3CkhVr-k?si=WrfEftOAmqUKBwQS" title="YouTube video player" frameborder="0" allow="web-share" allowfullscreen></iframe>

[![Plateforme de Stewart — ouilogique.com][i7]{:style="width:50%; margin-bottom:100px"}][i7]

[i7]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-05-31-proto-plateforme-de-stewart_001.jpg

## Deuxième version

Avec un clone de Nunchuck (joystick I²C de la console Wii), des vraie biellettes et des clones de servos Tower Pro MG996R.

[![Plateforme de Stewart — ouilogique.com][i3]{:style="width:50%; float:left"}][i3]

[i3]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-05-03-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i4]{:style="width:50%; float:left"}][i4]

[i4]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-05-03-proto-plateforme-de-stewart_002.jpg

[![Plateforme de Stewart — ouilogique.com][i5]{:style="width:50%; float:left"}][i5]

[i5]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-05-03-proto-plateforme-de-stewart_003.jpg

[![Plateforme de Stewart — ouilogique.com][i6]{:style="width:50%; float:left; clear:right; margin-bottom:200px;"}][i6]

[i6]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-05-03-proto-plateforme-de-stewart_004.jpg

## Première version

Avec un joystick analogique, des biellettes en fil de fer et des clones de servos Tower Pro MG90s.

<iframe width="799" height="449" src="https://www.youtube-nocookie.com/embed/qbQuXtnF4H4?si=dCC7E5JSER5oO-0a" title="YouTube video player" frameborder="0" allow="web-share" allowfullscreen></iframe>

[![Plateforme de Stewart — ouilogique.com][i2]{:style="width:50%; float:left; margin-bottom:100px"}][i2]

[i2]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-03-21-proto-plateforme-de-stewart_001.jpg

[![Plateforme de Stewart — ouilogique.com][i2b]{:style="width:50%; float:left; clear:right; margin-bottom:100px"}][i2b]

[i2b]: ../files/2019-03-27-plateforme-de-stewart-esp32/images/2019-03-21-proto-plateforme-de-stewart_002.jpg

---

## Aide-mémoire

Article Wikipedia

-   <https://en.wikipedia.org/wiki/Stewart_platform>

Vidéo qui m’a donné envie de réaliser une plateforme de Stewart
San-José State University

-   <https://www.youtube.com/watch?v=j4OmVLc_oDw>

Malheureusement, ils ont fermé leur site fullmotiondynamics.com.

California Polytechnic University of Pomona — Mechanical Engineering Department — Controls Class Final Project

-   <https://www.youtube.com/watch?v=7Jw8m4pbTYI>

MIPT, Department of Radio Engineering and Cybernetics
2 degrés de liberté + code Arduino

-   <https://www.youtube.com/watch?v=p65XPP53rLo>

Vidéo où l’on voit bien les imperfections métrologiques

-   <https://www.youtube.com/watch?v=QdKo9PYwGaU>
-   Ils utilisent ce controleur de servos
    <https://www.phidgets.com/?tier=3&catid=21&pcid=18&prodid=1032>

Athus Vieira

-   <https://www.linkedin.com/pulse/ball-plate-system-robotic-pid-control-athus-vieira/>
-   <https://www.youtube.com/watch?v=9XhcSSrA4Yc>
-   PID tuning <https://emanual.robotis.com/docs/en/platform/openmanipulator/>

Instructables by moosenee (avec gros plan sur le touch screen) **😃 Avec du code Arduino !**

-   <https://www.instructables.com/id/PID-Controlled-Ball-Balancing-Stewart-Platform/>
-   <https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform>
-   <https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform/blob/master/Readme.pdf>

Instructables by ThomasKNR **😃 Avec du code Arduino !**

-   <https://www.instructables.com/id/Arduino-controlled-Rotary-Stewart-Platform/>
-   <https://github.com/ThomasKNR/RotaryStewartPlatform>

xoxota99/stewy GitHub **😃 Avec du code Arduino !**

-   <https://github.com/xoxota99/stewy>

Chaine YouTube avec une collection d’une vingtaine de vidéos

-   <https://www.youtube.com/playlist?list=PLVNyl3oDY7lsYDQMKvguyPkpJ0Eaqb9z_>

Blender

-   <https://www.youtube.com/watch?v=uNKHX5B011E>

Webots

-   <https://cyberbotics.com/>
-   <https://www.youtube.com/watch?v=ddrtiwjKAaY>

Projet memememememememe **😃 Avec un simulateur fonctionnel en Processing et le code pour RPi !**

-   <https://memememememememe.me/post/stewart-platform-math/>
-   <https://github.com/thiagohersan/memememe>

**😃 Autres codes Arduino !**

-   <https://www.marginallyclever.com/2013/09/rotary-stewart-platform-v2-now-on-thingiverse/>
-   <https://github.com/MarginallyClever/RotaryStewartPlatform/blob/master/RSPv1/RSPv1.ino>

Robots à chaînes exotiques, Jean-Pierre Merlet, INRIA Sophia-Antipolis

-   <https://www-sop.inria.fr/members/Jean-Pierre.Merlet/Archi/node17.html>

## Plateforme de Stewart avec 3 degrés de liberté

<!-- - <https://www.instructables.com/id/Ball-Balancing-PID-System/> -->

-   <https://www.instructables.com/id/3DOF-Ball-on-Plate-Using-Closed-Loop-Stepper-Motor/>
-   <https://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2017/psl58_aw698_eb645/psl58_aw698_eb645/index.html#HLD>
-   <https://youtu.be/2i5qN2XWZLk>

## MECCAD Ball and plate

https://youtu.be/bEM5AywnzKg

## SPRK: A Low-Cost Stewart Platform For Motion Study In Surgical Robotics

-   <https://goldberg.berkeley.edu/pubs/2018_ISMR_stewart_design.pdf>
-   <https://github.com/BerkeleyAutomation/sprk>

## Plateforme de Stewart avec retour de force

Dynamixel motor

-   <https://www.robotis.us/dynamixel/>

Avec GUI Processing [Arun Dayal Udai]

-   <https://youtu.be/LFpyIZx2QGU?t=221>
-   <https://www.youtube.com/watch?v=rD4kTW_khXQ>
-   <https://www.youtube.com/watch?v=RqUcHulonHk>

Felix Ros **😃 Avec du code Processing et Arduino !**

-   <https://www.felixros.com/>
-   <https://github.com/felixros2401/Stewart-Platform>
-   <https://www.instructables.com/id/Controlling-a-Stewart-Platform/>

## Plateforme de Stewart à base circulaire (Rotopod)

Un rotopod permet de faire une rotation complète sans ajouter un 7e moteur.

Version de Circular-Base-Stewart-Platform

**😃 Il montre un logiciel de tunning des PID dans le 2e lien**

-   <https://www.youtube.com/channel/UCgm1PM2V9BgfP7Qaze1teAw>
-   <https://youtu.be/zna9Hw_Ei58?t=482>

Version commerciale de Mikrolar

-   <https://mikrolar.com/r3000.html>

## Versions commerciales

-   <https://motionsystems.eu/products/>

## Modelling and Simulation of a 6DOF Motion Platform with Permanent Magnet Linear Actuators for Testing in Wind Tunnel

-   <https://www.youtube.com/watch?v=AZjgcrV642c>

## Simulateur sur Mathematica

-   <https://www.wolfram.com/wolfram-u/courses/catalog/>

## Matlab forward kinematics solver

**😃 Avec du code Matlab !**

-   <https://github.com/jotux/Steward-Platform-Forward-Kinematics-Solver>

PDF à trouver :

> Forward kinematics of the general 6-6 Stewart platform using algebraic elimination.
> Authors: Tae-Young Lee, Jae-Kyung Shim
> Department of Mechanical Engineering, Korea University, 5-Ka Anam-Dong Sungbuk-Ku, Seoul, 136-701, South Korea.
> 36th issue of Mechanism and Machine Theory magazine (2001, 1073-1085).

## Applications Microclub

### Application 1 : Labyrinthe

-   Concours de vitesse de sortie du labyrinthe
    -   plusieurs robots s’affrontent en mode auto
    -   plusieurs utilisateurs s’affrontent en mode manuel

### Application 2 : Système de stabilisation pour appareil photo

-   Besoin d’un 7e axe pour augmenter l’angle de rotation autour de l’axe Z.

### Application 3 : Ball bouncing

-   <https://poe.olin.edu/2017/Bounce/>{:rel="nofollow"}
-   <https://github.com/TShapinsky/Bounce>

## IMPLÉMENTATION

### inputs

-   Mesure de la position de la bille par tapis résistif
-   Commande depuis navigateur web
-   Commande depuis Blender
-   BLE via smartphone
-   Joystick cablé (Wii Nunchuck)

### outputs

-   Mouvements du robot (6 ou 7 axes)
-   Retour visuel sur navigateur web
-   Retour visuel sur Blender

## Matériel

### Servomoteurs

-   Tower Pro MG90s Servos
    -   <https://www.banggood.com/6X-Towerpro-MG90S-Metal-Gear-RC-Micro-Servo-p-1072260.html>
    -   <https://www.towerpro.com.tw/product/mg90s-3/>
    -   <https://www.youtube.com/watch?v=iHPGoKHgzHo>
-   <https://servodatabase.com/>
-   KST DS115MG servos
-   GWS Micro 2BBMG servo (<https://www.youtube.com/watch?v=TgqJbneXZI8>)
-   HS5485HB (<https://github.com/a6guerre/Ball-balanced-on-Stewart-Platform/blob/master/Readme.pdf>)
-   <https://www.robotis.us/dynamixel-mx-64t/> (Utilisé par Arun Dayal Udai)
-   [MG995](https://www.banggood.com/MG995-High-Torgue-Mental-Gear-Analog-Servo-p-73885.html){:rel="nofollow"} (Rolf)
-   Tower Pro SG-5010 servos <https://www.intel.com/content/www/us/en/developer/topic-technology/open/overview.html>{:rel="nofollow"}
-   Hitec HS-5625MG (utilisé par <https://github.com/xoxota99/stewy>)
-   MG996R <https://fr.aliexpress.com/item/32636102294.html>
-   Parallax 900-00005 (utilisé par fullmotiondynamics)
    <https://www.parallax.com/product/900-00005>

### Fonctionnement des servos

-   Analogiques <https://www.youtube.com/watch?v=LXURLvga8bQ>
-   <https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/all>

### Driver de servos

-   PCA9685 (16 servos, I²C) <https://www.aliexpress.com/af/32718274859.html>

### Rotules + tiges

-   M3x100mm <https://www.aliexpress.com/af/32775630549.html>
-   En M2 <https://www.aliexpress.com/af/32704692789.html>
-   rotule <https://www.aliexpress.com/af/32887391192.html>
-   tige <https://www.aliexpress.com/af/32468820900.html>
-   tige + rotule <https://www.aliexpress.com/af/32904104171.html>
-   magnétique <https://www.aliexpress.com/af/32818135577.html>
-   complète <https://www.aliexpress.com/af/32894390128.html>

### Alim 5V

-   Courant 10A <https://www.aliexpress.com/af/32810906485.html>

### Levier de servo (Servo horn arm)

-   couleur tritanium <https://www.aliexpress.com/af/32843432977.html>
-   <https://www.aliexpress.com/af/32811563669.html>{:rel="nofollow"}

### Liste complète de matériel

-   <https://www.intel.com/content/www/us/en/developer/topic-technology/open/overview.html>{:rel="nofollow"}

### Touch screen

-   [Digikey 360-3520-ND](https://www.digikey.ch/short/pj85db){:rel="nofollow"} (utilisé par <https://github.com/xoxota99/stewy>)
-   <https://www.aliexpress.com/af/32809597549.html>

### ESP32

-   WeMos ESP32 WROOM
    -   <https://www.banggood.com/de/ESP32-WiFi-+-bluetooth-Development-Board-Ultra-Low-Power-Consumption-Dual-Core-ESP-32-ESP-32S-Similar-ESP8266-Geekcreit-for-Arduino-products-that-work-with-official-Arduino-boards-p-1175488.html>

### Joystick

-   Wii Nunchuck <https://www.aliexpress.com/af/32827461737.html>

### Calculs

-   <https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/geometry/transforming-points-and-vectors.html>

### PCB

-   <https://jlcpcb.com>

### Système complet avec caméra [Swiftflying Store](https://swiftflying.fr.aliexpress.com/store/3246059)

-   Le lien ne fonctionne plus : fr.aliexpress.com/item/32957141466.html

## Pinout

31 DIRA GPIO14
34 TC5 GPIO13
TC4 GPIO15
STPA
STPB
28 DIRB GPIO25

## DELTA-ROBOT ONE — Robot Delta Arduino

-   <https://www.hackster.io/deltarobotone/delta-robot-one-8386a1?utm_campaign=new_projects&utm_content=2&utm_medium=email&utm_source=hackster&utm_term=project_name>

## Calcul de la cinématique inverse

Cinématique inverse avec servomoteurs **😃 Meilleure source pour les calculs pour l’instant !**

> Méthode de calcul de la cinématique inverse utilisée par le projet memememememememe.
> C’est la seule méthode qui inclu des servomoteurs en rotation.
> Les autres proposent systématiquement des actuateurs linéaires.

-   <https://memememememememe.me/assets/posts/stewart-platform-math/MathsOfStewartPlatformV5.pdf>

Analyse vectorielle des lieux de singularité de la plate-forme de Gough-Stewart

-   <https://corpus.ulaval.ca/jspui/bitstream/20.500.11794/23444/1/28962.pdf>{:rel="nofollow"}
-   <https://stringfixer.com/fr/Stewart_platform>{:rel="nofollow"}
-   <https://fr.lambdageeks.com/parallel-robot-kinematics/>
-   <https://fr.wikipedia.org/wiki/Reymond_Clavel>
-   <https://fr.wikipedia.org/wiki/Robot_Delta>
-   <https://vimeo.com/129643275>
-   <https://www.ni.com/fr-ch/shop/product/6-dof-stewart-platform-control-library.html>
-   <https://www.ni.com/fr-ch/shop/product/stewart-platform-trainer-toolkit.html>
-   <https://www.xarg.org/paper/inverse-kinematics-of-a-stewart-platform/>
-   <https://youtu.be/1jrP3_1ML9M>

## Divers

-   <https://youtu.be/S-_VvNg_4cE>
-   <https://youtu.be/N1g_KwHqew8>

Stewart’s Platform.
Microcontrollers: ATMega 1284PA, ATMega 8.
Servos: TowerPro MG995

-   <https://grabcad.com/oleksandr.stepanenko-1/models>
-   <https://youtu.be/eXULfD94gho>
-   <https://youtu.be/Bf_1pUyjNiM>
-   <https://youtu.be/c1oxyk2IIOQ>
-   <https://youtu.be/vlCH4zhIqmM>
-   <https://acrome.net/product/stewart-platform>
-   <https://youtu.be/5wCK6XGC3ig>
-   <https://motionsystems.eu/product-category/motion-platforms/>
-   <https://youtu.be/VeD4_FghKhQ>
-   <https://youtu.be/PzOGIeGEyHY>
-   <https://upcommons.upc.edu/bitstream/handle/2117/101560/Memoria_TFG_Aitor_Ramirez.pdf?sequence=1&isAllowed=y>

[Fast Programming of 6-DOF Hexapod 6-Axis Motion Stewart Platform: Software, Mechanics, Controller](https://youtu.be/hkoTRNfivbU)

[Stewart Platform Joystick](https://youtu.be/fDgqAfzSy0c)

[I Built a Ball Balancing Robot](https://youtu.be/v4F-cGDGiEw)
