---
author: Nico
date: 2019-07-26 14:00:00+02:00
image:
    feature: banner_2019-07-26-debuggage-esp32.jpg
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Débuggage sur ESP32 avec un <em>ESP&#8209;Prog</em> et <em>PIO Unified Debugger</em>
---

[![ESP-Prog — ouilogique.com][img_3]{:style="width:90%;"}][img_3]

[img_3]: ../files/2019-07-26-debuggage-esp32/images/esp-prog-board-close-up-lowres.jpg

[![ESP-Prog back — ouilogique.com][img_4]{:style="width:90%;"}][img_4]

[img_4]: ../files/2019-07-26-debuggage-esp32/images/esp-prog-board-close-up-back-lowres.jpg

Cet article montre comment mettre en route un board _ESP&#8209;Prog_ et les outils intégrés à PlatformIO pour flasher et débugger un ESP32.

Le board _ESP&#8209;Prog_ permet de faire deux choses distinctes :

-   du débuggage en utilisant une interface JTAG (connecteur 10 broches) (ESP32 uniquement)
-   de flasher des programmes (ESP8266 & ESP32)

## Documentation

-   _PIO Unified Debugger_ (intégré à PlatformIO)
    -   <https://docs.platformio.org/en/latest/plus/debugging.html>
-   _ESP-Prog_
    -   <https://docs.platformio.org/en/latest/plus/debug-tools/esp-prog.html>
    -   <https://github.com/espressif/esp-iot-solution/blob/master/documents/evaluation_boards/ESP-Prog_guide_en.md>{:rel="nofollow"}

## Matériel utilisé

-   [ESP32](https://www.banggood.com/Geekcreit-ESP32-WiFi-bluetooth-Development-Board-Ultra-Low-Power-Consumption-Dual-Core-ESP-32-ESP-32S-p-1175488.html)
-   [ESP-Prog](https://fr.aliexpress.com/item/33022365662.html)
-   [Câble JTAG 2.54 mm (2×5 broches)](https://fr.aliexpress.com/item/32981928255.html)

## Vidéo d’Andreas Spiess

Source d’inspiration de cet article. Merci Andreas.

-   <https://www.youtube.com/watch?v=psMqilqlrRQ>

## Connexions JTAG

> Le débuggage JTAG utilise les GPIO 12 à 15, ce qui veut dire que ces broches ne peuvent pas être utilisées par le programme en cours de test !

Les couleurs sont indicatives et correspondent simplement aux fils que j’ai utilisés et que l’on peut voir sur la photo.

```bash
       ESP32        PROG BOARD      |      PROG BOARD    ESP32
====================================|=================================
jaune  3.3V      1. VDD             |   2. ESP_TMS       IO_14  vert
bleu   GND       3. GND             |   4. ESP_TCK       IO_13  violet
       -         5. GND             |   6. ESP_TDO       IO_15  gris
       -         7. GND             |   8. ESP_TDI       IO_12  blanc
       -         9. GND             |  10. NC            -
```

[![Debuggage d’un ESP32 avec un ESP-Prog et PIO Unified Debugger — ouilogique.com][img_1]{:style="width:90%;"}][img_1]

[img_1]: ../files/2019-07-26-debuggage-esp32/images/esp-prog-board-lowres.jpg

## Mise en route

-   S’assurer que les cavaliers sont configurés correctement (voir l’image ci-dessus).
-   Connecter le câble JTAG comme indiqué dans le tableau ci-dessus.
-   Ouvrir un projet PlatformIO existant ou en créer un nouveau.
-   Ajouter les informations suivantes dans le fichier `platformio.ini`.

```ini
debug_tool = esp-prog
upload_protocol = esp-prog
debug_init_break = tbreak setup
```

-   Pour info, voici le fichier `platformio.ini` que j’ai utilisé :

```ini

[platformio]
default_envs =
    esp32doit-devkit-v1


[env]
monitor_speed = 115200
build_flags =
    -D VERSION="0.1"
    -D BAUD_RATE=${env.monitor_speed}


[env:esp32doit-devkit-v1]
platform = espressif32
board = esp32doit-devkit-v1
framework = arduino
debug_tool = esp-prog
upload_protocol = esp-prog
debug_init_break = tbreak setup
```

-   Brancher le connecteurs USB de l’ESP&#8209;Prog à l’ordinateur. L’ESP&#8209;Prog utilise deux ports série. Il n’y a pas besoin de brancher le connecteur USB de l’ESP, mais ça peut être pratique pour accéder à l’interface série. L’ESP&#8209;Prog a aussi une interface série que je n’ai pas testé.
-   Sous Mac, il faut installer libusb avec [Homebrew][homebrew] (`brew update && brew upgrade && brew install libusb`).
-   Sous Windows, il faut modifier le pilote par défaut avec le logiciel [Zadig][zadig]. Voir [la procédure dans la vidéo d’Andreas Spiess à 14:52][zadig andreas].
-   Uploader le programme avec la commande standard de PlatformIO (`ctrl alt u`).
-   Placer quelques points d’arrêts dans le programme.
-   Démarrer le débuggage (menu `Debug/Start Debugging F5`).

[zadig andreas]: https://youtu.be/psMqilqlrRQ?t=892
[zadig]: https://zadig.akeo.ie
[homebrew]: https://brew.sh/

[![Debuggage d’un ESP32 avec un ESP-Prog et PIO Unified Debugger — ouilogique.com][img_2]{:style="width:90%;"}][img_2]

[img_2]: ../files/2019-07-26-debuggage-esp32/images/pio-unified-debugger-001.jpg

<!--

# ESP-Prog Board


OpenOCD

ESP-Prog





## Mise en route pour macOS

- Télécharger le pilote VCP (Virtual COM Port) (FTDIUSBSerialDriver_v2_4_2.dmg) <https://www.ftdichip.com/Drivers/VCP.htm>
- Télécharger le pilote D2XX (direct access) (D2XX1.4.4.dmg) <https://www.ftdichip.com/Drivers/D2XX.htm>
- Lors de l’installation, le pilote VCP demande des autorisations dans `Préférences système/Sécurité et confidentialité/Confidentialité`.
-

cd /usr/local/lib
cp /Volumes/release/D2XX/libftd2xx.1.4.4.dylib .
sudo ln -sf libftd2xx.1.4.4.dylib libftd2xx.dylib

cd /Volumes/release/D2XX/Samples/



cd /System/Library/Extensions
ls AppleUSBFTDI.kext/
drwxr-xr-x  6 root  wheel   192B 22 mai 15:31 Contents/

sudo mv AppleUSBFTDI.kext/ AppleUSBFTDI.disabled/

sudo kextunload –b com.apple.driver.AppleUSBFTDI

ls /dev | grep usb

cu.usbserial-141300
cu.usbserial-141301
tty.usbserial-141300
tty.usbserial-141301




violet
bleu
blanc
vert




## Ressources

  - Documentation officielle
    - <https://github.com/espressif/esp-iot-solution/blob/master/documents/evaluation_boards/ESP-Prog_guide_en.md>{:rel="nofollow"}
  - Installation du driver pour macOS
    - <https://www.ftdichip.com/Support/Documents/AppNotes/AN_134_FTDI_Drivers_Installation_Guide_for_MAC_OSX.pdf>




https://docs.platformio.org/en/latest/plus/debug-tools/esp-prog.html


## libusb

    brew install libusb
    brew link libusb
    brew link --overwrite libusb


## Set up OpenOCD

Download latest release archive with macos in its name, for example openocd-esp32-macos-0.10.0-esp32-20180418.tar.gz.

https://github.com/espressif/openocd-esp32/releases

    mkdir ~/esp
    cd ~/esp
    tar -xzf ~/Downloads/openocd-esp32-macos-0.10.0-esp32-20190708.tar.gz


    cd ~/esp/openocd-esp32
    bin/openocd -s share/openocd/scripts -f interface/ftdi/esp32_devkitj_v1.cfg -f board/esp-wroom-32.cfg



Failed to launch GDB: .pioinit:11: Error in sourced command file:
Undefined command: "tbreak_setup".  Try "help". (from interpreter-exec console "source .pioinit")



sudo kextunload /Library/Extensions/FTDIUSBSerialDriver.kext


-->
