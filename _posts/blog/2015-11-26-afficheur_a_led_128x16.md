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




![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_010_lowres.jpg)


128 full-color display type P6-16

16×128 pixels

[Xuan Cai](szxcled.com)



# INFORMATIONS AU DÉMARRAGE

	Colorful LED V39
	System Checks..
	Password OFF
	Baud 9600
	Sim card OK!
	CSQ Checks...
	CSQ: 9



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

## Protocole

Le message commence obligatoirement par `*`

et se termine obligatoirement par `#×` où `×` est le n° du message à afficher, × = 1 .. 59. Si x n’est pas dans l’intervalle 1 .. 59, le message `#1` est modifié. × peut être spécifié avec un `0` non significatif (#1 ou #01).

Les autres sélecteurs (mode de défilement, n° de ligne, couleur) sont optionnels.

|        |                                                                                                           |
| --     | --                                                                                                        |
| `<F×>` | Mode de défilement, × = 1 .. 6                                                                            |
| `<L×>` | N° de ligne, × = 1, 2                                                                                     |
| `<C×>` | Définition de la couleur, × = R (rouge), Y (jaune), G (vert), C (cyan), B (bleu), P (mangenta), W (blanc) |

## Modes de défilement

|        |                           |
| --     | --                        |
| `<F1>` | statique                  |
| `<F2>` | défilement vers le haut   |
| `<F3>` | défilement vers la gauche |
| `<F4>` | défilement vers le bas    |
| `<F5>` | clignote                  |

## Combinaisons de modes de défilements possibles sur deux lignes

|        |      |      |      |      |      |      |      |      |      |      |      |
| --     | --   | --   | --   | --   | --   | --   | --   | --   | --   | --   | --   |
| **L1** | `F1` | `F1` | `F1` | `F1` | `F2` | `F2` | `F2` | `F4` | `F4` | `F5` | `F5` |
| **L2** | `F1` | `F2` | `F3` | `F4` | `F1` | `F2` | `F3` | `F1` | `F4` | `F3` | `F5` |

## Exemples de messages sur une ligne

> Le mode de défilement est optionnel. Si on ne le précise pas, tous les modes de défilement sont utilisés successivement et dans l’ordre chronologique (F1, F2,...). On ne peut pas spécifier plusieurs modes de défilement sur une ligne donnée.<br/>
> Les lignes de commande ci-dessous doivent être envoyées dans des SMS distincts.

	*<F1><CG>A GAGNER EN CE MOMENT A L'EURO MILLIONS : <CR>!! 147 MILLION$ !!#02
	*<F5>!! 147 MILLION$ !!#03

## Exemples de messages sur deux lignes

> En mode deux lignes, les caractères ont une hauteur de 7 px.
> Par défaut, la première lignes est statique et la deuxième défile vers la gauche.<br/>
> On peut changer les modes de défilement des deux lignes. Voir les combinaisons possibles ci-dessus.

	*<L1><F2>KIOSQUE DE MONTCHOISI<L2><F2>JOYEUSES FETES DE FIN D'ANNEE#01
	*<L1><F4>KIOSQUE DE MONTCHOISI<L2><F4>JOYEUSES FETES DE FIN D'ANNEE#04

## Spécifier les textes qui doivent s’afficher

	*RL#01#02#03#04*

## Spécifier la couleur

> Si aucune couleur n’est spécifiée, les caractères s’affichent dans 7 couleurs successivement :
(rouge R, jaune Y, vert G, cyan C, bleu B, mangenta P, blanc W)

	*<CR>ce texte sera rouge <CY>et celui-ci sera jaune#08

## Spécifier la vitesse

> Vitesses de 1 à 6<br/>
> 1 = rapide, 6 = lent<br/>
> Utiliser de préférence les vitesses S1, S2 et S3. Les autres ont tendance à scintiller.<br/>
> La vitesse est définie pour tous les messages. On ne peut pas régler des vitesses individuelles.

	*S1*

## Spécifier la luminosité

> Luminosité de 1 à 6<br/>
> 1 = moins lumineux, 6 = plus lumineux
> La luminosité est définie pour tous les messages. On ne peut pas régler des luminosité individuelles.

	*B1*

## Mise à zéro

> La mise à zéro supprime tous les messages. Si aucun message n’est enregistré, le message “Welcome!” est affiché.

	*DEL*



# COMMANDE PAR USB SUR WINDOWS

1. Brancher le câble USB entre l’afficheur et l’ordinateur.
2. Vérifier si la carte USB est reconnue dans les périphériques de Windows.
3. Si c’est le cas, noter son port COM.
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

	<ID01><PA><L1><F2>KIOSQUE DE MONTCHOISI<L2><F2>JOYEUSES FETES DE FIN D'ANNEE<E>
	<ID01><PB><F1><CG>A GAGNER EN CE MOMENT A L'EURO MILLIONS : <CR>!! 147 MILLION$ !!<E>
	<ID01><PC><F5>!! 147 MILLION$ !!<E>
	<ID01><PD><L1><F4>KIOSQUE DE MONTCHOISI<L2><F4>JOYEUSES FETES DE FIN D'ANNEE<E>
	<ID01><RG>ABCD<E>



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


## Logiciel `MiniLEDDisplayEditorV2.exe`

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_001.png)

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_002.png)

![](/files/2015-11-26-afficheur_a_led_128x16/images/MiniLEDDisplayEditorV2_003.png)


## Profilé 118 × 25 mm

![](/files/2015-11-26-afficheur_a_led_128x16/images/profile_118x25_001_lowres.jpg)

![](/files/2015-11-26-afficheur_a_led_128x16/images/profile_118x25_002_lowres.jpg)


## Connecteur jack ⌀ 5.5 mm / ⌀ 2.5 mm

> ⚠ Le connecteur Jack de l’afficheur ne mesure que 9 mm de long. Quand on le tourne, il y a de temps en temps des mauvais contacts qui font que l’afficheur redémarre. Avec un connecteur de 11 mm de long, ce problème disparait.

![](/files/2015-11-26-afficheur_a_led_128x16/images/2015-11-26-afficheur_a_led_128x16_011_lowres.jpg)

