---
layout: page
title: "Test de vitesse entre les fonctions de manipulation de ports et les fonctions Arduino"
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


Les fonctionnalités offertes par l’écosystème Arduino sont forts pratiques, particulièrement pour les débutants, mais ne sont pas toujours des plus efficaces en terme d’utilisation des ressources, particulièrement en ce qui concerne l’utilisation des temps de cycles. Voici un petit comparatifs avec les fonctions de manipulation de port.

J’ai mesuré les résultats présentés ci-dessous sur un clone d’[Arduino Nano][1]. Les temps sont donnés en nombre de cycles d’horloge, et dans le cas présenté, un cycle vaut 62.5 ns (16 MHz).

[1]: /ch340_driver/#quelques-commandes-pour-obtenir-des-infos-sur-les-ports-usb

Le programme de test est disponible ci-dessous. Si le test est fait avec une boucle `for`, il faut ajouter 2 aux nombres de cycles indiqués dans le tableau.

| ---                                                                              |           |
| Fonction                                                                         | Nb cycles |
| -                                                                                | :-        |
| `bitSet`                                                                         | 2         |
| `bitClear`                                                                       | 2         |
| `digitalWrite`                                                                   | 81        |
| ---                                                                              |           |
| `PORTB ^= 1 << bLed13`                                                           | 3         |
| `bitRead( PORTB, bLed13 ) ? bitClear( PORTB, bLed13 ) : bitSet( PORTB, bLed13 )` | 5         |
| ---                                                                              |           |
| <code class="highlighter-rouge">DDRB &#124;= ( 1 << bLed13 )</code>              | 2         |
| `pinMode( Led13, OUTPUT )`                                                       | 68        |
| ---                                                                              |           |
| `bitRead`                                                                        | 1         |
| `digitalRead`                                                                    | 63        |


```c++
/*
 *
 * Mesure des temps d’exécution de diverses fonctions.
 * Les n° de test impairs sont exécutés avec une boucle for.
 * Les n° de test pairs  sont exécutés sans boucle for (dépliés).
 * La boucle for consomme typiquement 2 cycles d’horloge à chaque itération.
 *
 * avril 2016, ouilogique.com
 *
 */

#define type_test 104 // Modifier le n° de test

#define Led13 13
#define bLed13 PORTB5
#define  Led13Read  bitRead  ( PORTB, bLed13 )
#define  Led13Set   bitSet   ( PORTB, bLed13 )
#define  Led13Clear bitClear ( PORTB, bLed13 )
#define  Led13Toggle1 PORTB ^= 1 << bLed13
#define  Led13Toggle2 Led13Read ? Led13Clear : Led13Set

// Tests en OUTPUT
#if type_test == 1 || type_test == 2
    #define w1 Led13Set
    #define w2 Led13Clear
#elif type_test == 3 || type_test == 4
    #define w1 digitalWrite( Led13, HIGH );
    #define w2 digitalWrite( Led13, LOW );
#elif type_test == 5 || type_test == 6
    #define w1 Led13Toggle1;
    #define w2 Led13Toggle1;
#elif type_test == 7 || type_test == 8
    #define w1 Led13Toggle2;
    #define w2 Led13Toggle2;
#elif type_test == 9 || type_test == 10
    #define w1 Led13Set
    #define w2 Led13Set
#elif type_test == 11 || type_test == 12
    #define w1 Led13Clear
    #define w2 Led13Clear
#elif type_test == 13 || type_test == 14
    #define w1 Led13Clear
    #define w2 Led13Set
#elif type_test == 15 || type_test == 16
    #define w1 DDRB |= ( 1 << bLed13 )
    #define w2 DDRB |= ( 1 << bLed13 )
#elif type_test == 17 || type_test == 18
    #define w1 pinMode( Led13, OUTPUT )
    #define w2 pinMode( Led13, OUTPUT )

// Tests en INPUT
#elif type_test == 101 || type_test == 102
    #define w1 Led13Read
    #define w2 Led13Read
#elif type_test == 103 || type_test == 104
    #define w1 digitalRead( Led13 )
    #define w2 digitalRead( Led13 )
#endif

const int iMax = 1E3;
const float iMax2 = 2 * iMax;
const int F_CPU_MHz = F_CPU / 1E6;


void setup()
{
    #if type_test < 101
        DDRB |= ( 1 << bLed13 );
    #else
        DDRB &= ~( 1 << bLed13 );
    #endif
    Serial.begin( 115200 );
    _delay_ms( 100 );

    #if   defined( __AVR_ATtinyX5__ )
        Serial.print( "\n__AVR_ATtinyX5__" );
    #elif defined( __AVR_ATtinyX313__ )
        Serial.print( "\n__AVR_ATtinyX313__" );
    #elif defined( __AVR_ATtinyX4__ )
        Serial.print( "\n__AVR_ATtinyX4__" );
    #elif defined( __AVR_ATmega32U4__ )
        Serial.print( "\n__AVR_ATmega32U4__" );
    #elif defined( __AVR_ATmega328P__ )
        Serial.print( "\n__AVR_ATmega328P__" );
    #else
        Serial.print( "\nAutre processeur" );
    #endif

    Serial.print( "\n###" );
    Serial.print( "\nTest de vitesse" );
    Serial.print( "\n\nFrequence d'horloge = " );
    Serial.print( F_CPU_MHz );
    Serial.print( " MHz" );
    Serial.print( "\n periode d'horloge = " );
    Serial.print( 1.0 / ( F_CPU_MHz / 1000.0 ) );
    Serial.print( " ns" );
 }


void loop()
{
    unsigned long T1;
    unsigned long T2;
    float dT;


    Serial.print( "\n\n###" );
    Serial.print( "\nTEST " );
    Serial.print( type_test );
    #if type_test == 1 || type_test == 2
        Serial.print( "\n  bitSet + bitClear" );
    #elif type_test == 3 || type_test == 4
        Serial.print( "\n  digitalWrite" );
    #elif type_test == 5 || type_test == 6
        Serial.print( "\n  Led13Toggle1" );
    #elif type_test == 7 || type_test == 8
        Serial.print( "\n  Led13Toggle2" );
    #elif type_test == 9 || type_test == 10
        Serial.print( "\n  bitSet + bitSet" );
    #elif type_test == 11 || type_test == 12
        Serial.print( "\n  bitClear + bitClear" );
    #elif type_test == 13 || type_test == 14
        Serial.print( "\n  bitClear + bitSet" );
    #elif type_test == 15 || type_test == 16
        Serial.print( "\n  DDRB |= ( 1 << bLed13 )" );
    #elif type_test == 17 || type_test == 18
        Serial.print( "\n  pinMode( Led13, OUTPUT )" );
    #elif type_test == 101 || type_test == 102
        Serial.print( "\n  bitRead; bitRead;" );
    #elif type_test == 103 || type_test == 104
        Serial.print( "\n  digitalRead; digitalRead;" );
    #else
        Serial.print( "\n  Test non defini" );
    #endif

    #if type_test % 2 == 1
        Serial.print( "\n  boucle 'for'" );
    #else
        Serial.print( "\n  boucle 'for' depliee" );
    #endif


    // Il faut attendre un peu après le dernier Serial.print,
    // sinon les temps mesurés sont plus longs d’environ 12 ns.
    _delay_ms( 20 );

    // Début du test
    T1 = micros();

    #if type_test % 2 == 1
        // Cette boucle for utilise 2 cycles d’horloge.
        for( int i=0; i<iMax; i++ )
            { w1; w2; }
    #else
        // Ici, la boucle for est dépliée pour ne pas consommer les 2 cycles d’horloge. Il y a 1000 w1 et 1000 w2.
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
        w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;w1;w2;
    #endif

    T2 = micros(); // Fin du test
    dT = ( T2 - T1 );

    Serial.print( "\n  Temps necessaire pour effectuer " );
    Serial.print( iMax2, 0 );
    Serial.print( " operations : " );
    Serial.print( dT, 0 );
    Serial.print( " us\n  " );

    Serial.print( ( dT * F_CPU_MHz ) / iMax2 );
    Serial.print( " cycles d'horloge / operation\n  " );

    Serial.print( ( dT * 1000.0 ) / iMax2, 0 );
    Serial.print( " ns / operation" );

    _delay_ms( 2000 );
}
```



## À lire également

[Benchmarking Arduino’s digitalWrite() with a Logic Analyzer](https://www.baldengineer.com/digitalwrite-on-a-logic-analyzer.html)
