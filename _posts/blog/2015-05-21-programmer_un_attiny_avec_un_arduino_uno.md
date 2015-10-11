---
layout: page
title: "Programmer un ATtiny25V avec un Arduino UNO comme programmateur"
excerpt:
categories:
tags: [ATtiny, ISP, UNO]
author: Nico
comments: true
share: true
image:
  feature: 2015-02-23_microDelta_002.jpg
published: true
---



# Matériel requis

- Un ordinateur sur OS X Yosemite (10.10)
- Un Arduino UNO
- Un ATtiny25V
- Un breadboard
- 4 LED
- 4 résistances de 220 Ω


# Sources

> Source principale

- <http://www.didel.com/diduino/ProgrammerUnAtTiny.pdf>

> Autres sources

- <http://arduino.cc/en/Tutorial/ArduinoISP>
- <http://www.atmel.com/images/atmel-2586-avr-8-bit-microcontroller-attiny25-attiny45-attiny85_datasheet.pdf>

> À voir aussi

- <http://arduino.cc/en/Main/Standalone>
- <http://arduino.cc/en/Tutorial/ArduinoToBreadboard>
- <http://codeandlife.com/2012/03/21/using-arduino-uno-as-isp/>


# Préambule

Le but de ce document est de présenter la programmation d’un microcontrôleur ATtiny25V à l’aide d’un Arduino UNO. Ce mode de programmation s’appelle en anglais *AVR ISP (in-system programmer)*. L’IDE Arduino utilisé pendant les tests était la version 1.5.8 bêta Java 6.



# Préparation matérielle

Câbler la plaque d’essai selon le schéma ci-dessous. Les trois premières LED, verte, rouge et orange, servent à afficher le statut lors de la programmation :

- pin 9: Heartbeat   - shows the programmer is running
- pin 8: Error       - Lights up if something goes wrong (use red if that makes sense)
- pin 7: Programming - In communication with the slave

et la quatrième LED, bleue, sert à vérifier que l’ATtiny a effectivement été programmé avec le programme `tinyblinky.ino`. À noter que les LED sont optionnelles.

![](/images/programmer_un_attiny_avec_un_arduino_uno/programmer_un_attiny25v_bb.svg)



# Préparation logicielle

- Télécharger les librairies (*Core Libraries*) de la famille ATtiny de <https://code.google.com/p/arduino-tiny/> en prenant garde de choisir la version correspondante à l’IDE Arduino qui va être utilisé par la suite.
- Décompresser le fichier zip et déplacer le répertoire `tiny` dans `~/Documents/Arduino/hardware/`.
- Copier le fichier `tiny/avr/Prospective Boards.txt` vers `tiny/avr/boards.txt`.
- Le fichier `boards.txt` peut optionnellement être modifié, par exemple pour enlever des définitions de microcontrôleurs inutiles. Ce fichier complète celui de l’IDE qui se trouve à `/Applications/Arduino.app/Contents/Resources/Java/hardware/arduino/avr/boards.txt` et qui peut lui aussi être édité.
- Redémarrer l’IDE. Le menu `Outils/Type de carte` doit afficher la liste des ATtiny installés ci-dessus.



# Configurer l’Arduino UNO comme un programmateur

- Ouvrir le croquis `ArduinoISP.ino` qui se trouve dans le menu `Fichier/Exemples` en onzième position.
- Vérifier que la cible est l’Arduino UNO :
    - `Outils/Type de carte/Arduino UNO`
    - `Outils/Port` : *Sélectionner le port du UNO*
    - `Outils/Programmateur/AVRISP mkII`
- Téléverser le croquis `ArduinoISP.ino` sur le UNO.



# Charger le *bootloader* dans l’ATtiny

> Normalement cette étape n’est pas nécessaire quand on programme en mode ISP. Le bootloader est justement là pour palier l’absence de programmateur. Comme je n’ai pas encore vérifié cette info, je laisse ce texte pour l’instant. De toute façon une chose est sûre : ça fonctionne comme ça.

Cette opération est nécessaire pour les microcontrôleurs qui n’ont jamais été programmés. Elle ne doit être effectuée qu’une fois.

- Changer la cible pour programmer l’ATtiny25V :
    - `Outils/Type de carte/ATtiny25 @ 1 MHz`
    - `Outils/Port` : *Sélectionner le port du UNO*
    - `Outils/Programmateur/Arduino as ISP`
- Charger le bootloader :
    - `Outils/Graver la séquence d’initialisation`

D’après [Didel](http://www.didel.com/diduino/ProgrammerUnAtTiny.pdf), ce n’est pas vraiment un *bootloader* qui est chargé, mais une configuration des fusibles qui est réalisée.



# Programmer l’ATtiny

- Vérifier que la cible est effectivement l’ATtiny comme à l’étape précédente.
- Téléverser le croquis suivant :


{% highlight C++ %}
/*
    tinyblinky.ino
    Programme pour tester la programmation en mode ISP d’un ATtiny25V
    Fait clignoter une LED sur PB4, pin 3
*/

#include <avr/io.h>
#define LedPin PORTB4
#define LedToggle PORTB ^= ( 1<<LedPin )
#define delay1 250
#define delay2 500

void wait( int delay_ms )
{
    for( volatile int i=0; i<delay_ms; i++ )
    {
        for( volatile int j=0; j<50; j++ ) {}
    }
}

int main()
{
    DDRB |= ( 1<<LedPin );
    while( true )
    {
        LedToggle;  wait( delay1 );
        LedToggle;  wait( delay2 );
    }
}
{% endhighlight %}


# Résolution de problèmes

Certaines cartes UNO requièrent l’ajout d’un condensateur de  10 µF entre la pin `RESET` et la pin `GND`. Voir à ce sujet <http://forum.arduino.cc/index.php?topic=104435.0>. Pour moi, ça a fonctionné sans ce condensateur.












# Programmation des fusibles

> Les infos de ce chapitres m’ont été gracieusement transmises par [Richard](http://www.fablab-chene20.ch).

Les fusibles (*fuses* en anglais) sont des paramètres intégrés aux microcontrôleurs d’Atmel et que l’on peut modifier à l’aide du programme [`avrdude`](http://www.nongnu.org/avrdude/user-manual/avrdude.html). C’est ce même programme qui est utilisé par l’IDE Arduino pour envoyer les fichiers compilés sur le microcontrôleur. On peut d’ailleurs voir ce qu’il fait de la manière suivante :

- Ouvrir les préférences de l’IDE Arduino
- Cliquer sur le lien en bas de la fenêtre pour ouvrir le dossier contenant les préférences. Alternativement on peut directement éditer le fichier avec la commande `open ~/Library/Arduino15/preferences.txt`
- Fermer l’IDE Arduino, car il écrase le fichier des préférences lorsqu’on le quitte
- Changer la ligne `upload.verbose=false` en `upload.verbose=true`
- Redémarrer l’IDE
- Téléverser le croquis `tinyblinky.ino`
- Copier le contenu de la console et le coller dans un éditeur de texte
- Chercher la chaîne de caractère `avrdude`
- La première occurrence nous montre un message similaire à

{% highlight bash %}
/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin/avrdude -C/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf -v -v -v -v -pattiny25 -cstk500v1 -P/dev/tty.usbmodem1421 -b19200 -Uflash:w:/var/folders/3l/c6_nv3414rb_sxjkb8z9z1fr0000gn/T/build2612095162045447463.tmp/tinyblinky.cpp.hex:i
{% endhighlight %}

## Configuration d’`avrdude`

Pour utiliser `avrdude`, le plus simple est d’ajouter les deux lignes suivantes à la fin du fichier `~/.bash_profile` et de redémarrer le terminal

{% highlight bash %}
PATH=$PATH:/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin
AVRDUDECONF=/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf
{% endhighlight %}


## Lectures des fusibles

La commande utilisée par l’IDE Arduino nous donne toutes les informations de configuration pour envoyer nos propres commandes. La première chose à faire est de lire la configuration actuelle. Adaptez la commande suivante à votre configuration :

{% highlight bash %}
avrdude                      \
    -C $AVRDUDECONF          \
    -v                       \
    -p attiny25              \
    -c stk500v1              \
    -P /dev/tty.usbmodem1421 \
    -b 19200                 \
    -U lfuse:r:-:i           \
    -U hfuse:r:-:i           \
    -U efuse:r:-:i           \
    -n
{% endhighlight %}

`avrdude` renvoie une longue réponse qui se termine par :

{% highlight bash %}
avrdude: safemode: lfuse reads as 62
avrdude: safemode: hfuse reads as D7
avrdude: safemode: efuse reads as FF
avrdude: safemode: Fuses OK (H:FF, E:D7, L:62)
{% endhighlight %}

> On constate que cette version d’`avrdude` a un bug : La dernière ligne indique les fusibles dans l’ordre `H, E, L` alors qu’en fait il s’agit de l’ordre `E, H, L`. Il faut donc faire attention et ne tenir compte que des trois premières lignes.
La version d’`avrdude` utilisée pour ce test est : `Version 6.0.1, compiled on Apr  3 2014 at 22:00:33`



## Écriture des fusibles

Pour configurer les fusibles, il est conseillé d’utiliser un outil de configuration, comme <http://www.engbedded.com/fusecalc/> ou de lire le chapitre *20. Memory Programming* de la spécification <http://www.atmel.com/images/atmel-2586-avr-8-bit-microcontroller-attiny25-attiny45-attiny85_datasheet.pdf>. La vidéo <https://www.youtube.com/watch?v=jP1NTgs-a-s> donne une bonne introduction en anglais.

Dans notre cas, nous allons simplement utiliser les valeurs données par l’utilitaire *fusecalc* ci-dessus pour enlever la division par 8 de la fréquence d’horloge. La seule valeur que nous changeons est

    Divide clock by 8 internally; [CKDIV8=0]

Ce qui modifie la valeur du `Low Byte` qui passe de `62` à `e2`.

{% highlight bash %}
avrdude                      \
    -C $AVRDUDECONF          \
    -v                       \
    -p attiny25              \
    -c stk500v1              \
    -P /dev/tty.usbmodem1421 \
    -b 19200                 \
    -U lfuse:w:0xe2:m        \
    -U hfuse:w:0xd7:m        \
    -U efuse:w:0xff:m
{% endhighlight %}

Après l’exécution de la commande ci-dessus, on constate que le croquis `tinyblinky.ino` est exécuté 8 fois plus rapidement.

Si on veut retrouver les fusibles d’origine :

{% highlight bash %}
avrdude                      \
    -C $AVRDUDECONF          \
    -v                       \
    -p attiny25              \
    -c stk500v1              \
    -P /dev/tty.usbmodem1421 \
    -b 19200                 \
    -U lfuse:w:0x62:m        \
    -U hfuse:w:0xd7:m        \
    -U efuse:w:0xff:m
{% endhighlight %}


