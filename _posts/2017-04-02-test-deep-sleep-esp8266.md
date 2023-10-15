---
author: Nico
date: 2017-04-02 18:30:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Test du deep sleep de l’ESP8266
---

## Matériel

-   [WeMos® D1 Mini V2 NodeMcu 4M Bytes Lua WIFI Internet Of Things Development Board Based ESP8266][1]

[1]: https://usa.banggood.com/D1-Mini-V2-NodeMcu-4M-Bytes-Lua-WIFI-Internet-Of-Things-Development-Board-Based-ESP8266-p-1115398.html?imageAb=2&akmClientCountry=America&p=0431091025639201412F&a=1697372252.7894&akmClientCountry=America

## Différences entre les 3 modes de veille

-   <https://www.espressif.com/sites/default/files/9b-esp8266-low_power_solutions_en_0.pdf>

-   Modem-sleep
-   Light-sleep
-   Deep-sleep

| Item                      | Modem-sleep | Light-sleep | Deep-sleep |
| ------------------------- | ----------- | ----------- | ---------- |
| Wi-Fi                     | OFF         | OFF         | OFF        |
| System clock              | ON          | OFF         | OFF        |
| RTC                       | ON          | ON          | ON         |
| CPU                       | ON          | Pending     | OFF        |
| Substrate current         | 15 mA       | 0.4 mA      | ~ 20 µA    |
| Average current DTIM = 1  | 16.2 mA     | 1.8 mA      | -          |
| Average current DTIM = 3  | 15.4 mA     | 0.9 mA      | -          |
| Average current DTIM = 10 | 15.2 mA     | 0.55 mA     | -          |

**Pour comparaison**

-   un MSP430 consomme 230 µA en mode _Active_, 0.5 µA en mode _Standby_ et 0.1 µA en mode _Off_ ([Datasheet du MSP430](https://www.ti.com/lit/ds/symlink/msp430g2453.pdf)).
-   un ATtiny consomme 300 µA en mode _Active_ et 0.1 µA en mode _Power-down_ ([Datasheet de l’ATtiny](https://ww1.microchip.com/downloads/en/devicedoc/atmel-2586-avr-8-bit-microcontroller-attiny25-attiny45-attiny85_datasheet.pdf)).

### Deep Sleep

Il y a deux manières de sortir du _Deep Sleep_

1. Débrancher et rebrancher l’alimentation
2. Créer une pulse vers `GND` sur `RST`. Le reset aura lieu au flanc montant. En temps normal, `RST` doit être maintenu à `VCC` ou éventuellement laissé flottant. Cette impulsion peut être crée :
    - Avec une interruption temporelle : on spécifie la durée d’endormissement dans le programme et l’ESP génère la pulse sur `GPIO16` qui doit être connecté à `RST`.
    - Avec une interruption matérielle : on connecte un signal en _pull up_ sur `RST`. Ce signal doit être exempt de rebonds, sinon l’ESP sera remis à zéro en saccades.

**Notes**

Si on spécifie une durée de `0`, l’ESP reste en `deep sleep` jusqu’au prochain `reset` sur `RST` ou lors du prochain branchement.

Si `GPIO 16` n’est pas connecté à `RST`, certaines fonctions de l’ESP sont quand même redémarrées à la fin du temps de veille, car sa consommation augmente à ~10 mA, même avec la RF désactivée...

## Montage 1 — Interruption temporelle

L’ESP sort du _deep sleep_ à intervales réguliers. Lors de ce reset, D0 passe à `0` pendant 273.70 µs et doit être connecté à `RST`. Le `reset` a lieu lors du flanc montant.

_Note : 273.70 µs correspond à 21896 cycles d’horloge à 80 MHz (= 80E+6 \* 273.7E-6)._

[![Deep Sleep ESP8266 — Test 1][img_1]][img_1]

[img_1]: ../files/2017-04-02-test-deep-sleep-esp8266/images/2017-04-02-test-deep-sleep-esp8266-montage-1.jpg

[![Deep Sleep ESP8266 — Signal de reset sur D0][img_2]][img_2]

[img_2]: ../files/2017-04-02-test-deep-sleep-esp8266/images/2017-04-02-test-deep-sleep-esp8266-signal-DO-reset.jpg

## Montage 2 — Interruption externe

L’ESP sort du _deep sleep_ lorsque le bouton connecté en _pull-up_ est pressé. Problème garanti avec ce montage parce que l’ESP sera _reseté_ autant de fois que le bouton sera pressé, y compris lors des rebonds du bouton. Une solution serait d’utiliser une bascule en entrée (<https://github.com/esp8266/Arduino/issues/1488>).

[![Deep Sleep ESP8266 — Test 2][img_3]][img_3]

[img_3]: ../files/2017-04-02-test-deep-sleep-esp8266/images/2017-04-02-test-deep-sleep-esp8266-montage-2.jpg

## Programme de test

Note : c’est le même programme qui est utilisé pour les deux montages.

```c++
/*

Test Deep Sleep Wemos

avril 2017, ouilogique.com

*/

#include <ESP8266WiFi.h>
extern "C" {
#include "user_interface.h"
}

static const uint8_t LEDverte  = D1; // GPIO 5
static const uint8_t LEDorange = D2; // GPIO 4
static const uint8_t LEDbleue  = D4; // GPIO 2 ⇒ LED du board

#define LEDverteHIGH  digitalWrite( LEDverte, HIGH )
#define LEDverteLOW   digitalWrite( LEDverte, LOW )
#define LEDorangeHIGH digitalWrite( LEDorange, HIGH )
#define LEDorangeLOW  digitalWrite( LEDorange, LOW )
#define LEDbleueHIGH  digitalWrite( LEDbleue, LOW )   // LED du board ⇒ logique inversée
#define LEDbleueLOW   digitalWrite( LEDbleue, HIGH )

const int sleepTimeS = 2;

void initHardware()
{
  WiFi.mode( WIFI_OFF );

  Serial.begin( 115200 );
  Serial.print( F( "\n\nSTART\n" ) );

  pinMode( LEDverte,  OUTPUT );
  pinMode( LEDorange, OUTPUT );
  pinMode( LEDbleue,  OUTPUT );
  for( int i=0; i<10; i++ )
  {
    LEDverteLOW;
    LEDorangeLOW;
    LEDbleueLOW;
    delay( 50 );
    LEDverteHIGH;
    LEDorangeHIGH;
    LEDbleueHIGH;
    delay( 50 );
  }

  Serial.print( F( "FIN DU SETUP\n" ) );
}

void initSleep()
{
  rst_info *rsti;
  rsti = ESP.getResetInfoPtr();
  Serial.println( String( "ResetInfo.reason = " ) + rsti->reason );

  // system_deep_sleep_set_option( 0 );
  // system_deep_sleep( sleepTimeS * 1000000 );
  ESP.deepSleep( sleepTimeS * 1000000, WAKE_RF_DISABLED );
}

void setup()
{
  initHardware();
  initSleep();
}

void loop()
{}
```

## Sources

-   <https://www.esp8266.com/viewtopic.php?f=13&t=8315>
-   <https://www.youtube.com/watch?v=9G-nMGcELG8&index=11&list=PL3XBzmAj53Rlu3Byy_GkqG6b-nwEpWku0>
