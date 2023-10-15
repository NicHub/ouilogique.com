---
author: Nico
date: 2015-09-14 00:00:00+01:00
image:
    feature: banner_2015-09-14-bluetooth_low_energy_avec_nRF51.jpg
lang: fr
layout: page
published: true
redirect_from:
    - /blog/bluetooth_low_energy_avec_nRF51/
tags: []
title: Découverte du Bluetooth Low Energy avec la carte Nordic Semiconductor nRF51
---

[![ouilogique.com][img_1]][img_1]

[img_1]: ../files/2015-09-14-bluetooth_low_energy_avec_nRF51/images/nRF51_001.jpg

[![ouilogique.com][img_2]][img_2]

[img_2]: ../files/2015-09-14-bluetooth_low_energy_avec_nRF51/images/nRF51_002.jpg

## Brochage

[![ouilogique.com][img_3]][img_3]

[img_3]: ../files/2015-05-28-pinouts/images/xnRF51-DK_Pinout_4.png

> Seules les broches P0.01 à P0.06 peuvent être configurées en entrées analogiques.
>
> Toutes les broches peuvent être utilisées pour le SPI, l’I²C et le RS232 et pas seulement les broches indiquées sur le schéma de brochage.
>
> Il n’y a qu’un périphérique UART, deux SPI et deux I²C (appelés TWI), mais il faut choisir : soit `SPI0` ou `TWI0`, soit `SPI1` ou `TWI1`, car ils partagent visiblement des ressources communes !

## Support imprimé 3D

-   <https://www.thingiverse.com/thing:1012855>
-   <https://cad.onshape.com/documents/3f05e14ebb62415c928ff36e/w/d85b78be98c545f6ab2fd41f/e/7053fbf40382442182af2f67>

## La carte nRF51 en bref

C’est une carte de développement pour le prototypage d’applications Bluetooth LE. Le brochage est compatible avec celui de l’Arduino UNO, donc en théorie on peut utiliser les mêmes shields. Dans la pratique, il faudra faire attention au fait que la carte nRF51 ne fonctionne que sous 3.3 V et que le courant max des sorties est de 0.5 mA (5 mA sur 3 broches au maximum avec le mode “high drive” qu’il faut configurer explicitement)¹.

> ¹ [Voir “nRF51822 Product Specification v3.1 — chap 8.23 — General Purpose I/O (GPIO) specifications”, page 65](https://www.nordicsemi.com/eng/nordic/download_resource/20339/13/3799285)

## Bluetooth avec Node.js

[NoBLE](https://github.com/sandeepmistry/noble)

## Bluetooth et le marketing

> ⚠ Bluetooth ≠ Bluetooth Low Energy

| Nom courant                      | ⇒ _Nom du marketing_            |
| :------------------------------- | :------------------------------ |
| Bluetooth (v1, v2, v3)           | ⇒ _Bluetooth Classic (BR, EDR)_ |
| Bluetooth Low Energy (v4)        | ⇒ _Bluetooth Smart_             |
| Bluetooth + Bluetooth Low Energy | ⇒ _Bluetooth Smart Ready_       |

## Android

[nRF Master Control Panel (BLE)](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en)

## Quelques outils pour OS X

[HardwareIOTools_Xcode_6.3](http://adcdownload.apple.com/Developer_Tools/Hardware_IO_Tools_for_Xcode_6.3/HardwareIOTools_Xcode_6.3.dmg)

## Portée des variables

`static const` dans une fonction ⇒ stocké en flash

```c++
/* PORTÉE DES VARIABLES */
                          // VISIBILITÉ  PERSISTANCE  ALLOCATION
                          // ==========  ===========  ==========
int vg;                   // Globale     Programme    Heap
static int vg;            // Module      Programme    Heap
void f(..) {
  int vl;                 // Fonction    Fonction     Stack
  static int vlp;         // Fonction    Programme    Heap
  const int vlc = ..;     // Fonction    Fonction     Stack/opt
  static const vlcs = ..; // Fonction    Programme    Flash
```

norme C 99 ⇒ permet des déclarations spéciales de struct

## Liens

-   <http://jmkikori.no-ip.org/jmk/joomla-static/index.php/2-uncategorised/1-introduction-bluetooth-low-energy.html>{:rel="nofollow"}
-   <https://os.mbed.com/platforms/Nordic-nRF51-DK/>
-   [Bande industrielle, scientifique et médicale (Wikipédia)](https://fr.wikipedia.org/wiki/Bande_industrielle,_scientifique_et_médicale)
-   [Bluetooth (Wikipédia)](https://fr.wikipedia.org/wiki/Bluetooth)
-   [Bluetooth Accessory Design Guidelines for Apple Products](https://developer.apple.com/hardwaredrivers/BluetoothDesignGuidelines.pdf)
-   [Kit Didel](https://www.didel.com/diduino/AdanRF51.pdf)
-   [https://evothings.com](https://evothings.com){:rel="nofollow"}
-   [List of Bluetooth Smart and Bluetooth Smart Ready products available now](http://www.bluetooth.com/Pages/Bluetooth-Smart-Devices-List.aspx){:rel="nofollow"}

## Modules BLE

-   [RedBearLab](http://redbearlab.com/nrf51822/){:rel="nofollow"}
-   [Aliexpress](http://fr.aliexpress.com/item/Low-power-consumption-BLE4-0-module-with-2-4GHz-PCB-antenna16-28mm-Free-sample/32334323347.html)
-   [MDBT40 (SeeedStudio)](https://www.seeedstudio.com/MDBT40-ANT-P256V3-nRF51422-based-BLE-Module-p-2507.html)
—   [MDBT40 (Raytac)](http://www.raytac.com/download/MDBT40/MDBT40%20spec-Version%20A3.pdf){:rel="nofollow"}
-   [Banggood (avec quartz 32 kHz)](http://www.banggood.com/NRF51822-2_4GHz-Network-Bluetooth-Serial-Module-Support-For-Apple-Android-p-992468.html?p=0431091025639201412F){:rel="nofollow"}
-   [Microchip BM77](http://www.microchip.com/wwwproducts/Devices.aspx?product=bm77)
-   [HM-10 Bluetooth 4.0 Module Transparent Serial Port With Logic Level Translator](http://www.banggood.com/HM-10-Bluetooth-4_0-Module-Transparent-Serial-Port-p-967059.html?p=0431091025639201412F){:rel="nofollow"}
-   [DFRobot — Bluno](http://www.dfrobot.com/)
-   [Bluno Beetle V1.0 — AliExpress](http://fr.aliexpress.com/item/DFRoBot-100-Original-DIY-Bluno-Beetle-V1-0-wearable-mini-Micro-main-controller-Board-with-Bluetooth/32456535853.html)
