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
redirect_from:
  - /blog/manipulation_des_ports/
---




## Description des registres AVR & MSP

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


## Exemple de programme

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






## Liens

<http://www.mon-club-elec.fr/pmwiki_reference_arduino/pmwiki.php?n=Main.PortManipulation>



## Manipulation des registres de l’ESP8266

Je n’ai pas trouvé de page qui décrit comment manipuler les registres de l’ESP, mais en fouillant dans les librairie, j’ai réussi à trouver comment réaliser un programme Blink.


{% highlight C++ %}
/*
  Blink ESP8266 avec manipulation directe du registre GPO.

~/Library/Arduino15/packages/esp8266/hardware/esp8266/2.3.0/cores/esp8266/core_esp8266_wiring_digital.c
~/Library/Arduino15/packages/esp8266/hardware/esp8266/2.3.0/cores/esp8266/esp8266_peri.h

#define ESP8266_REG(addr) *((volatile uint32_t *)(0x60000000+(addr)))
#define GPOS   ESP8266_REG(0x304) //GPIO_OUT_SET WO
#define GPOC   ESP8266_REG(0x308) //GPIO_OUT_CLR WO
#define GP16O  ESP8266_REG(0x768)

GPIO disponibles
0, 1, 2, 3, 4, 5,
9, 10,
12, 13, 14, 15, 16


!! 1 et 3 sont pour l’UART
!! 6, 7, 8 et 11 n’existent pas

*/

#define LED_PIN LED_BUILTIN

void setup()
{
  pinMode( LED_PIN, OUTPUT );
  Serial.begin( 115200 );
  Serial.print( "\n\nLED_PIN = " );
  Serial.println( LED_PIN );
}

void loop()
{
  GPO &= ~(1<<LED_PIN);
  delay( 100 );
  GPO |= (1<<LED_PIN);
  delay( 1000 );
}
{% endhighlight %}
