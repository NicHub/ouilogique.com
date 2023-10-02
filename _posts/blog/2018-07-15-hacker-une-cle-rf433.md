---
author: Nico
date: 2018-07-15 15:28:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Hacker une clé RF433
---

## But

Cet article montre comment lire les signaux d’une clé RF433 à l’aide d’un adaptateur SDR (_Software Defined Radio_). De les copier à l’aide du logiciel URH sur un Raspberry Pi et de programmer un Arduino pour envoyer ces signaux à l’identique.

## Limitation

Cette technique ne fonctionne qu’avec des émetteurs RF433 non sécurisés. Ces émetteurs envoient toujours le même signal que l’on peut copier et programmer sur un Arduino.

À contrario, les émetteurs sécurisés, comme ceux qui sont utilisés pour verrouiller les véhicules, émettent un code différent à chaque utilisation (_rolling code_), ce qui implique qu’il ne sert à (presque) rien de copier le signal puisqu’il ne pourra être utilisé au mieux qu’une seule fois.

## Sources

Cet article m’a été inspiré par [la vidéo d’Andreas Spiess “How to Hack your 433 MHz Devices with a Raspberry and a RTL-SDR Dongle (Weather Station)”][video andreas].

## Matériel

-   SDR-Dongle: <http://s.click.aliexpress.com/e/bQ91w8QM> ou <http://bit.ly/2NcRMT2>
-   Raspberry Pi modèle 2 ou 3. On peut aussi utiliser URH sur Windows, Linux et sur Mac, donc le RPi est optionnel. À noter que l’adaptateur SDR que j’ai n’est pas reconnu par URH sur mon Mac et j’ai donc opté pour la solution RPi.
-   Un Arduino UNO ou équivalent
-   Un bouton
-   Un _breadboard_
-   Un [émetteur RF433][émetteur rf433]
-   Une [clé RF433][clé rf433] à copier (mais normalement vous devriez déjà avoir cet article)

## Installation d’URH

Pour lire le signal d’origine, nous allons utiliser [le logiciel URH][urh github].

-   Si nécessaire, [installez Raspbian Stretch][installer raspbian stretch]

```bash
sudo apt-get --assume-yes update
sudo apt-get --assume-yes dist-upgrade
sudo apt-get --assume-yes dist install python3-numpy python3-psutil python3-zmq python3-pyqt5 g++ libpython3-dev python3-pip cython3
sudo pip3 install urh
```

Si la dernière commande ne fonctionne pas, [il faut ruser un peu][truc install urh] en utilisant les commandes suivantes :

```bash
git clone https://github.com/jopohl/urh
cd urh
sudo pip3 install .
```

## Utilisation d’URH

-   Connecter l’adaptateur SDR.

[![Raspberry Pi avec dongle SDR][image-1]][image-1]

-   Dans l’interface graphique de Raspbian, ouvrir un terminal et taper la commande `urh`.
-   Dans la fenêtre qui s’ouvre, aller dans le menu `File/Record Signal...`.
-   Dans la nouvelle fenêtre, choisir l’adaptateur : `Device : RTL-SDR`.
-   Cliquer sur la flèche arrondie en regard de `Device Identifier`. L’identifiant de l’adaptateur doit d’afficher, par exemple : `Realtek RTL2838UHIDIR (SN: 00000001)`.
-   Laisser les autres options par défaut.

[![Enregistrement d’un signal RF433 avec URH][image-2]][image-2]

-   Cliquer sur le bouton `Start`.
-   Appuyer sur le bouton de la clé RF433.
-   Cliquer sur le bouton `Stop`. Il faut arrêter l’acquisition le plus rapidement possible car le fichier de résultats grandit à une vitesse vertigineuse. En plus, le buffer est rapidement saturé.
-   Cliquer sur `Save` et enregistrer le fichier pour une utilisation ultérieure.
-   Fermer la fenêtre d’acquisition. La fenêtre de traitement des données s’ouvre. Cette fenêtre peut être rappelée en ouvrant le fichier enregistré précédemment.
-   Cliquer sur `Modulation: ASK`. ASK = _Amplitude Shift Keying_.
-   Dans la partie sous le graphique, double-cliquer de façon à sélectionner une ligne. La partie correspondante du graphique est sélectionnée. Inversement, on peut sélectionner une partie du graphique et les chiffres correspondants seront automatiquement sélectionnés également.
-   On peut zoomer le graphique avec la roulette de la souris. La position du curseur de la souris modifie également le point central du zoom.
-   Évaluer quelle ligne de chiffres se répète le plus souvent et la copier avec le raccourci clavier `CTRL-C`.

    1110111011101000100010001000100011101110111010001000111010001000100010001110111010001000111010001

-   Il faut aussi noter la valeur `Bit Length`. Sur l’image ci-dessous, elle est de 276 µs. À d’autres endroits du signal cette valeur peut être légèrement différente. J’ai opté pour une valeur de 280 µs qui convient très bien.
-   Maintenant, on a les bits du signal (97 bits dans mon cas). Mais il faut encore évaluer combien de bits sont dans l’intervalle sans signal. Dans mon cas, il y en a 31, donc une période complète comprend 97 + 31 = 128 bits.
-   Il faut également ajouter les zéros au code copié. Dans mon cas, il y en a 31.

[![Enregistrement d’un signal RF433 avec URH][image-3]][image-3]

## Tester le code copié

Pour tester le code que nous venons de copier avec URH, il faut tout d’abord réaliser le montage de la photo ci-dessous. À noter que le récepteur RF433 à gauche de la photo n’est pas utilisé dans le cadre de cet article.

L’émetteur RF433 est connecté à la broche 7.

Les boutons sont connectés aux broches 8, 9 et 10. Pour un premier test, un seul bouton suffit.

[![Enregistrement d’un signal RF433 avec URH][image-4]][image-4]

Le code de test se trouve ici : [rf433-spoof sur GitHub][rf433-spoof sur github].

On peut aussi télécharger tous les exemples de ce blog d’un coup avec la commande git :

```bash
git clone https://github.com/NicHub/ouilogique-Arduino.git
```

Ensuite il faut modifier le code du signal, la durée d’un bit et le nombre de bits dans le fichier `rf433-messages.h`.

Et il ne reste plus qu’à flasher l’Arduino et faire un test.

## À voir aussi

-   <https://github.com/merbanan/rtl_433>
-   [RTL-SDR Blog V3 R820T2 RTL2832U 1PPM TCXO SMA Software Defined Radio (Dongle Only)](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/)
-   <http://gqrx.dk/>
-   <https://airspy.com>

[video andreas]: https://www.youtube.com/watch?v=L0fSEbGEY-Q
[urh github]: https://github.com/jopohl/urh
[installer raspbian stretch]: https://ouilogique.com/installer-raspian-stretch/
[truc install urh]: https://github.com/jopohl/urh/issues/502
[image-1]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-001.jpg
[image-2]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-002.jpg
[image-3]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-003.jpg
[image-4]: ../../files/2018-07-15-hacker-une-cle-rf433/hacker-une-cle-rf433-004.jpg
[rf433-spoof sur github]: https://github.com/NicHub/ouilogique-Arduino/tree/master/rf433-spoof
[émetteur rf433]: https://fr.aliexpress.com/item/1Lot-1-pair-2pcs-RF-wireless-receiver-module-transmitter-module-Ordinary-super-regeneration-315-433MHZ-DC5V/968306683.html
[clé rf433]: https://fr.aliexpress.com/item/Universal-2-Channels-Electric-Garage-Door-Cloning-Remote-Control-Key-Fob-433mhz/32816768549.html
