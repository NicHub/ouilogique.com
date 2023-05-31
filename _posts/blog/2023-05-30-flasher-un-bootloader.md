---
layout: page
title: "Flasher un bootloader"
modified:
categories:
excerpt:
tags: []
image:
    feature:
date: 2023-05-30T12:00:00+01:00
published: true
author: Nico
---

[![Flasher un bootloader — ouilogique.com][i1]{:style="width:100%;"}][i1]

[i1]: ../../files/2023-05-30-flasher-un-bootloader/images/2023-05-30-flasher-un-bootloader-001_lowres.jpg

Un de mes Arduino Nano refusait de se faire flasher et retournait systématiquement une erreur du genre `not in sync`.
En googlant, j’ai trouvé que plusieurs personnes ont résolu ce problème en changeant le type de bootloader en `ATmega328p (Old Bootloader)` dans le menu `Tools/Processor: "ATmega328p"/` de l’IDE Arduino.
Mais pour moi, ça n’a pas marché.
Du coup, j’ai décidé de reflasher le bootloader en utilisant un Arduino UNO comme programmateur.
Cette façon de faire s’appelle “ICSP” ou _In Circuit Serial Programming_.

> Source : La plupart des informations proviennent de cette page : <https://docs.arduino.cc/built-in-examples/arduino-isp/ArduinoISP>

## Câblage

Il faut connecter une à une les broches ICSP qui se trouvent à l’arrière des boards, à l’exception de la broche `reset` de la cible (l’Arduino Nano) qui est connectée à la broche 10 du programmateur (l’Arduino UNO).

| Programmateur<br>(Arduino UNO) | Cible<br>(Arduino Nano) |
| -----------------------------: | ----------------------- |
|                             10 | ICSP RESET              |
|                       ICSP SCK | ICSP SCK                |
|                      ICSP MISO | ICSP MISO               |
|                       ICSP GND | ICSP GND                |
|                      ICSP MOSI | ICSP MOSI               |
|                        ICSP 5V | ICSP 5V                 |

À noter que les broches ICSP se trouvent à deux endroits :

-   À l’arrière de la carte
-   Sur les côté de la carte (broches usuelles)

Sur l’Aduino UNO, il y a deux groupes de broches ICSP.
Celui qui nous intéresse ici est à l’arrière de la carte.
L’autre groupe qui est proche du connecteur USB permet de programmer la puce ATmega16U2 qui permet la communication sur le bus USB.

Consulter les brochages ici pour plus de détail : <https://ouilogique.com/pinouts/>.

> Attention, les broches ICSP sont tournées de 180° entre le UNO et le Nano si on prend le connecteur USB comme référence.

Voir aussi la page <https://qastack.fr/arduino/40098/icsp-pin-what-is-it-actually>.

Je conseille également de connecter trois LEDs sur les broches 7, 8 et 9.
C’est optionnel, mais ces LEDs aident beaucoup à comprendre ce qui se passe.

| Broche | Signal      |
| -----: | ----------- |
|      7 | Programming |
|      8 | Error       |
|      9 | Heartbeat   |

## Flashage du bootloader

-   Ouvrir l’IDE Arduino.
-   Flasher le programmateur avec le programme `ArduinoISP.ino` qui se trouve dans le menu `File/Examples/11.ArduinoISP`.
-   Configurer le type de programmateur à la valeur `Arduino as ISP` dans le menu `Tools/Programmer: "Arduino as ISP"`.
-   Flasher le bootloader de la cible avec la fonction `Burn bootloader` tout en bas du menu `Tools`.

## Vérification

Pour vérifier que le flashage du bootloader s’est bien déroulé, on peut programmer la cible en la connectant directement à l’ordinateur, sans passer par le programmateur.

Alternativement, on peut aussi utiliser le programme `avrdude` pour faire cette vérification.

```bash
alias avrdude='$HOME/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/bin/avrdude'
AVRDUDE_CONF=$HOME/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf
avrdude -C $AVRDUDE_CONF -v -p atmega328p -c arduino -P /dev/cu.usbmodem4012401
```

## Programmation avec le programmateur

On peut aussi programmer la cible en utilisant le programmateur.
Ceci aura pour effet d’effacer le bootloader et on récupérera donc la place qu’il prend en mémoire, soit environ 512 octets.
De plus les programmes s’exécuteront sans délai lorsque le microcontrôleur est mis sous tension.
Ceci est dû au fait que le bootloader attend 1 ou 2 secondes au démarrage pour permettre la programmation par le port série.

Pour vérifier si un bootloader est présent, il faut redémarrer la carte en appuyant sur le bouton _reset_ et observer l’état de la LED intégrée.
Si elle clignote rapidement pendant environ une seconde puis fait une pause d’environ une seconde aussi, c’est que le bootloader est présent.

Pour programmer la cible en utilisant le programmateur, il faut :

-   Câbler le programmateur et la cible comme expliqué au chapitre câblage ci-dessus.
-   Ouvrir l’IDE Arduino.
-   Vérifier que le type de programmateur est toujours configuré sur `Arduino as ISP` (voir ci-dessus)
-   Vérifier les réglages du port série et du type de carte :
    -   Le port série est celui du programmateur.
    -   Le type de carte est celui de la cible.
-   Cliquer `Upload using programmer` du menu `Sketch`.

> Attention, si on utilise la commande `Upload` conventionnelle, c’est le programmateur qui sera programmé et pas la cible.
> Dans tous les cas, ce n’est pas grave, il suffit d’uploader à nouveau le programme `ArduinoISP.ino` sur le programmateur.

> Si on essaie de programmer un microcontrôleur qui n’a pas de bootloader via le port série, l’upload échouera avec l’erreur `programmer is not responding`.

> Si on programme le microcontrôleur avec un programmateur, il faut débrancher les éventuels composants qui seraient connecté aux broches ICSP.
