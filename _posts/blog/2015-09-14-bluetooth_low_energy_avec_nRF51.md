---
layout: page
title: "Découverte du Bluetooth Low Energy avec la carte Nordic Semiconductor nRF51"
modified:
categories:
excerpt:
tags: []
image:
     feature: nRF51.jpg
date: 2015-09-14T00:00:00+01:00
published: true
author: Nico
---



![](/files/2015-09-14-bluetooth_low_energy_avec_nRF51/nRF51_001.jpg)

![](/files/2015-09-14-bluetooth_low_energy_avec_nRF51/nRF51_002.jpg)


# Brochage

![](/files/2015-05-28-pinouts/images/xnRF51-DK_Pinout_4.png)

> Seules les broches P0.01 à P0.06 peuvent être configurées en entrées analogiques.
>
> Toutes les broches peuvent être utilisées pour le SPI, l’I²C et le RS232 et pas seulement les broches indiquées sur le schéma de brochage.
>
> Il n’y a qu’un périphérique UART, deux SPI et deux I²C (appelés TWI), mais il faut choisir : soit `SPI0` ou `TWI0`, soit `SPI1` ou `TWI1`, car ils partagent visiblement des ressources communes !


# Support imprimé 3D

<http://www.thingiverse.com/thing:1012855>

<https://cad.onshape.com/documents/3f05e14ebb62415c928ff36e/w/d85b78be98c545f6ab2fd41f/e/7053fbf40382442182af2f67>


# La carte nRF51 en bref

C’est une carte de développement pour le prototypage d’applications Bluetooth LE. Le brochage est compatible avec celui de l’Arduino UNO, donc en théorie on peut utiliser les mêmes shields. Dans la pratique, il faudra faire attention au fait que la carte nRF51 ne fonctionne que sous 3.3 V et que le courant max des sorties est de 0.5 mA (5 mA sur 3 broches au maximum avec le mode “high drive” qu’il faut configurer explicitement)¹.

> ¹ [Voir “nRF51822 Product Specification v3.1 — chap 8.23 — General Purpose I/O (GPIO) specifications”, page 65](https://www.nordicsemi.com/eng/nordic/download_resource/20339/13/3799285)


# Bluetooth avec Node.js

[NoBLE](https://github.com/sandeepmistry/noble)


# Android

[nRF Master Control Panel (BLE)](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en)


# Quelques outils pour OS X

[HardwareIOTools_Xcode_6.3](http://adcdownload.apple.com/Developer_Tools/Hardware_IO_Tools_for_Xcode_6.3/HardwareIOTools_Xcode_6.3.dmg)


# Portée des variables

`static const` dans une fonction ⇒ stocké en flash

{% highlight C %}

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

{% endhighlight %}


norme C 99 ⇒ permet des déclarations spéciales de struct



# Liens

- <http://jmkikori.no-ip.org/jmk/joomla-static/index.php/2-uncategorised/1-introduction-bluetooth-low-energy.html>
- <https://developer.mbed.org/platforms/Nordic-nRF51-DK/>
- [Bande industrielle, scientifique et médicale (Wikipédia)](https://fr.wikipedia.org/wiki/Bande_industrielle,_scientifique_et_médicale)
- [Bluetooth (Wikipédia)](https://fr.wikipedia.org/wiki/Bluetooth)
- [Bluetooth Accessory Design Guidelines for Apple Products](https://developer.apple.com/hardwaredrivers/BluetoothDesignGuidelines.pdf)
- [Kit Didel](http://www.didel.com/diduino/AdanRF51.pdf)
- [https://evothings.com](https://evothings.com)
- [List of Bluetooth Smart and Bluetooth Smart Ready products available now](http://www.bluetooth.com/Pages/Bluetooth-Smart-Devices-List.aspx)

# Modules BLE

- [RedBearLab](http://redbearlab.com/nrf51822/)
- [Aliexpress](http://fr.aliexpress.com/item/Low-power-consumption-BLE4-0-module-with-2-4GHz-PCB-antenna16-28mm-Free-sample/32334323347.html)
- [MDBT40 (SeeedStudio)](http://www.seeedstudio.com/depot/MDBT40P%C2%A0%C2%A0nRF51822%C2%A0based%C2%A0BLE%C2%A0module-p-2503.html) — [MDBT40 (Raytac)](http://www.raytac.com/download/MDBT40/MDBT40%20spec-Version%20A3.pdf)
- [Banggood (avec quartz 32 kHz)](http://www.banggood.com/NRF51822-2_4GHz-Network-Bluetooth-Serial-Module-Support-For-Apple-Android-p-992468.html)
