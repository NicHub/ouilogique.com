---
layout: page
title: "Afficheur à LED 128×16"
modified:
categories:
excerpt:
tags: []
image:
     feature: 2015-11-26-afficheur_a_led_128x16_010.jpg
date: 2015-11-26T15:00:00+01:00
published: true
author: Nico
---





128 full-color display type P6-16

16×128 pixels

[Xuan Cai](szxcled.com)



# INFORMATIONS AU DÉMARRAGE

	Colorful LED V39
	System checks..
	Password Off
	Baud 9600
	Sim OK
	CSQ: 0



# CARTE SIM

Introduire la carte SIM avec son support en plastique.

Ressortir la carte en pressant le bouton vert à côté de celle-ci.

La carte SIM permet de contrôler l’afficheur à distance via SMS ou *Fetion App* (service chinois de messagerie).



# MOT DE PASSE

Pas de mot passe par défaut.



# COMMANDE PAR SMS

> ⚠ Les commandes sont sensibles à la casse !<br/>
> ⚠ Les accents ne sont pas supportés !<br/>
> ⚠ 140 caractères maximum !

## Modes de défilement

	<F1> statique
	<F2> défilement vers le haut
	<F3> défilement vers la gauche
	<F4> défilement vers le bas
	<F5> clignote

## Exemples de messages sur une ligne

> Le mode de défilement est optionnel.<br/>
> Les lignes ci-dessous doivent être envoyées dans des SMS distincts.

	*<F3>LE KIOSQUE DE MONTCHOISI VOUS SOUHAITE DE JOYEUSES FETES DE FIN D'ANNEE#01
	*<F1>LE KIOSQUE#02
	*<F2>DE MONTCHOISI#03
	*<F3>VOUS SOUHAITE#04
	*<F4>DE JOYEUSES FETES#05
	*<F5>DE FIN D'ANNEE#06

## Exemples de messages sur deux lignes

> Par défaut, la première lignes est statique et la deuxième défile vers la gauche.<br/>
> En mode deux lignes, les caractères ont une hauteur de 7 px.

	*<L1>LE KIOSQUE DE MONTCHOISI<L2>VOUS SOUHAITE DE JOYEUSES FETES DE FIN D'ANNEE#07

## Spécifier les textes qui doivent s’afficher

	*RL#01#02#03#04#05#06#07*

## Spécifier la couleur

> Si aucune couleur n’est spécifiée, les caractères s’affichent dans 7 couleurs successivement :
(rouge R, jaune Y, vert G, cyan C, bleu B, violet P, blanc W)

	*<CR>ce texte sera rouge<CY>et celui-ci sera jaune#08

## Spécifier la vitesse

> Vitesses de 1 à 6<br/>
> 1 = rapide, 6 = lent

	*S1*

## Spécifier la luminosité

> Luminosité de 1 à 6<br/>
> 1 = moins lumineux, 6 = plus lumineux

	*B1*

## Effacer tous les messages

> Si aucun message n’est enregistré, le message “Welcome!” est affiché.

	*DEL*



# COMMANDE PAR USB SUR WINDOWS

1. Brancher le câble USB entre l’afficheur et l’ordinateur.
2. Vérifier si la carte USB est reconnue dans les périphériques de Windows.
3. Si c’est le cas noter son port COM.
4. Si ce n’est pas le cas installer le driver pour le CH340 et retourner au point 2.
5. Utiliser le logiciel fourni (MiniLEDDisplayEditorV2.exe)



# COMMANDE PAR USB SUR OS X

> Pour trouver les commandes RS232 à envoyer, j’ai espionné les transmissions du logiciel `MiniLEDDisplayEditorV2.exe` avec [Free Serial Analyzer](http://freeserialanalyzer.com/) sous Win10/VirtualBox.

Utiliser un logiciel qui permet d’envoyer des caractères via RS232. Celui de l’IDE Arduino fonctionne bien.

- Installer le pilote pour la communication USB avec le CH340 <http://ouilogique.com/ch340_driver/>
- L’adresse du port RS232 est de la forme `/dev/cu.wchusbserial14240`
- Vitesse de transmission : 9600 bauds
- Attendre ~ 3 s entre chaque commande

## Exemples

	<ID01><PA><F3>LE KIOSQUE DE MONTCHOISI VOUS SOUHAITE DE JOYEUSES FETES DE FIN D'ANNEE<E>
	<ID01><PB><F1>LE KIOSQUE<E>
	<ID01><PC><F2>DE MONTCHOISI<E>
	<ID01><PD><F3>VOUS SOUHAITE<E>
	<ID01><PE><F4>DE JOYEUSES FETES<E>
	<ID01><PF><F5>DE FIN D'ANNEE<E>
	<ID01><RG>ABCDEF<E>



# IMAGES




![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_001_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_002_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_003_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_004_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_005_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_006_lowres.jpg)

## Carte GPRS + USB

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_007_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_008_lowres.jpg)

## Nape

> ⚠ Un des connecteurs de cette nape est plus bas que normal (environ 3mm du câble jusqu’au sommet). C’est nécessaire pour pouvoir assembler l’afficheur !

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_009_lowres.jpg)

## Démo

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_010_lowres.jpg)

## Logiciel `MiniLEDDisplayEditorV2.exe`

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_001.png)

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_002.png)

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_003.png)


## Profilé 118 × 25 mm

![](/files/2015-11-26-afficheur_a_led_128x16/images/profile_118x25_001_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/profile_118x25_002_lowres.jpg)


