---
layout: page
title: "La manipulation des entrées-sorties à l’aide des registres de port"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2014-12-03T12:00:00+01:00
published: true
author: Nico
---




# Description des registres AVR & MSP

| R/W | MSP     | AVR     | USAGE                                                                                   |
| :-- | :--     | :--     | :--                                                                                     |
| r/w | `PxDIR` | `DDRx`  | DIRECTION DES E/S : `0` = input  / `1` = output                                         |
| r   | `PxIN`  | `PINx`  | LECTURE DES E/S                                                                         |
| r/w | `PxOUT` | `PORTx` | ÉCRITURE DES E/S OU SÉLECTION DES RÉSISTANCES DE TIRAGE : `1` = pullup / `0` = pulldown |
| r/w | `PxREN` |         | Pullup / Pulldown : `0` = disabled / `1` = enabled                                      |
| r/w | `PxSEL` |         | Sélection des fonctions                                                                 |

> AVR n’a que les pullups
> doc AVR, voir [datasheet chap. 14 p.75](http://www.atmel.com/images/atmel-8271-8-bit-avr-microcontroller-atmega48a-48pa-88a-88pa-168a-168pa-328-328p_datasheet_complete.pdf)
> doc MSP, voir [slau144j.pdf p.329, 333](http://www.ti.com/lit/ug/slau144j/slau144j.pdf)


# Exemple de programme

{% highlight C++ %}

/*
  BLINK pin 2 to 9
*/
void setup()
{
  DDRD |= B11111100; // Pin 2 to 7 as outputs
  DDRB |= B00000011; // Pin 8 to 9 as outputs
}

void loop()
{
  // Pin 2 to 7 HIGH
  PORTD |= ( 1<<2 ) | ( 1<<3 ) | ( 1<<4 ) | ( 1<<5 ) | ( 1<<6 ) | ( 1<<7 );
  // Pin 8 to 9 HIGH
  PORTB |= ( 1<<0 ) | ( 1<<1 );

  _delay_ms( 500 );

  // Pin 2 to 7 LOW
  PORTD &= ~( 1<<2 ) & ~( 1<<3 ) & ~( 1<<4 ) & ~( 1<<5 ) & ~( 1<<6 ) & ~( 1<<7 );
  // Pin 8 to 9 LOW
  PORTB &= ~( 1<<0 ) & ~( 1<<1 );

  _delay_ms( 500 );
}

{% endhighlight %}






# Liens

<http://www.mon-club-elec.fr/pmwiki_reference_arduino/pmwiki.php?n=Main.PortManipulation>


