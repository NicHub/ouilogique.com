---
layout: page
title: "Test de taille entre les fonctions de manipulation de ports et les fonctions Arduino"
modified:
categories:
excerpt:
tags: []
image:
    feature:
date: 2016-04-25T19:35:00+02:00
published: true
author: Nico
---

Voici un comparatif de la taille mémoire du programme `blink` lorsqu’on utilise les fonctions de port ou les fonctions Arduino.

## Progamme Blink fourni dans les exemples Arduino

```bash
Le croquis utilise 1 066 octets (3%) de l'espace de stockage de programmes. Le maximum est de 32 256 octets.
Les variables globales utilisent 9 octets (0%) de mémoire dynamique, ce qui laisse 2 039 octets pour les variables locales. Le maximum est de 2 048 octets.
```

## Programme avec les manipulations de port

_Voir le programme `BlinkPort.ino` ci-dessous._

```bash
Le croquis utilise 492 octets (1%) de l'espace de stockage de programmes. Le maximum est de 32 256 octets.
Les variables globales utilisent 9 octets (0%) de mémoire dynamique, ce qui laisse 2 039 octets pour les variables locales. Le maximum est de 2 048 octets.
```

## Conclusion

On voit que la taille en mémoire de stockage de programme est 2.16 fois plus élevée avec les fonctions Arduino qu’en manipulant directement les ports. Et la taille, c’est une chose, mais il y a aussi un net avantage dans la vitesse d’exécution, comme vous pouvez le découvrir dans l’article suivant : [Test de vitesse entre les fonctions de manipulation de ports et les fonctions Arduino](/test_vitesse_port_vs_arduino/).

```c++
// BlinkPort.ino
// Clignote la LED 13 toute les secondes avec les manipulations de port

static const double wait = 1000;

#define LED13Toggle              PORTB ^= 1UL<<PORTB5
#define LED13Read                bitRead (  PINB, PORTB5 )
#define LED13Set                 bitSet  ( PORTB, PORTB5 )
#define LED13Clear               bitClear( PORTB, PORTB5 )
#define LED13OutputPinMode       bitSet  (  DDRB, PORTB5 )
#define LED13InputPinMode        bitClear(  DDRB, PORTB5 )
#define LED13InputPullupPinMode  LED13InputPinMode;LED13Set

void setup()
{
  LED13OutputPinMode;
}

void loop()
{
  LED13Set;
  _delay_ms( wait );
  LED13Clear;
  _delay_ms( wait );
}
```
