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
Mais pour moi, ça n’a pas marché. Du coup, j’ai décidé de reflasher le bootloader en utilisant un Arduino UNO comme programmateur.

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

Le brochage se trouve ici : <https://ouilogique.com/pinouts/>.

> Attention, les broches ICSP sont tournées de 180° entre le UNO et le Nano si on prend le connecteur USB comme référence.

Je conseille également de connecter trois LEDs sur les broches 7, 8 et 9.
C’est optionnel, mais ces LEDs aident beaucoup à comprendre ce qui se passe.

| Broche | Signal      |
| -----: | ----------- |
|      7 | Programming |
|      8 | Error       |
|      9 | Heartbeat   |

## Flashage du bootloader

Le flashage du bootloader se fait en trois temps.

-   D’abord on flashe le programmateur avec le programme `ArduinoISP.ino` qui se trouve dans le menu `File/Examples/11.ArduinoISP`.
-   Ensuite on configure le type de programmateur à la valeur `Arduino as ISP` dans le menu `Tools/Programmer: "Arduino as ISP"`.
-   Enfin, on flashe le bootloader de la cible avec la fonction `Burn bootloader` tout en bas du menu `Tools`.

# Vérification

Pour vérifier que le flashage s’est bien déroulé, on peut programme la cible en utilisant le programmeteur. Pour cela, il faut vérifier que le type de programmateur est toujours configuré à `Arduino as ISP` (voir ci-dessus), puis utiliser la commande `Upload using programmer` du menu `Sketch`.

> Attention, si on utilise la commande `Upload` conventionnelle, c’est le programmateur qui sera programmé et pas la cible. Dans tous les cas, ce n’est pas grave, il suffit d’uploader à nouveau le programme `Arduino as ISP` sur le programmateur.

Alternativement, on peut aussi utiliser le programme `avrdude` pour faire cette vérification.

```bash
alias avrdude='$HOME/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/bin/avrdude'
AVRDUDE_CONF=$HOME/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf
avrdude -C $AVRDUDE_CONF -v -p atmega328p -c arduino -P /dev/cu.usbmodem4012401
```
