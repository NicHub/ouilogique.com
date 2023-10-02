---
lang: fr
layout: page
title: "Test de hubs USB"
modified: 2015-11-20T12:00:00+01:00
categories:
excerpt:
tags: []
image:
    feature:
date: 2015-07-02T09:47:00+01:00
author: Nico
redirect_from:
    - /blog/usb_hub_test/
---

-   [Test du hub _Anne LXL4072201A_](#test-du-hub-anne-lxl4072201a)
-   [Test du hub _Delock 61857_](#test-du-hub-delock-61857)

## Test du hub _Anne LXL4072201A_

Test du hub USB de la marque _Anne_, modèle _LXL4072201A_, acheté sur AliExpress ~~(fr.aliexpress.com/item/2014-newest-7-Port-USB-3-0-HUB-High-Speed-With-Power-Adapter-For-Laptop-Notebook/1997348166.html)~~.

Le test consiste à placer une diode entre les pattes d’alimentation de la fiche USB qui est normalement connectée à l’ordinateur. Une résistance de 100 Ω peut être ajoutée en parallèle pour s’assurer que le hub détecte une charge et éviter ainsi l’enclenchement de la sécurité de haute impédance du hub. Le hub testé n’a visiblement pas cette protection puisque la LED s’est allumée sans la résistance de 100 Ω. On peut remplacer la résistance de 220 Ω par une résistance plus élevée pour diminuer l’intensité lumineuse. Avec une résistance d’1 kΩ par exemple, ça marche bien aussi.

**Le hub doit être alimenté pendant le test.**


[![ouilogique.com][img_1]{:style="width:50%;"}][img_1]

[img_1]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_003.svg


[![ouilogique.com][img_2]{:style="width:50%;"}][img_2]

[img_2]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_001.jpg

[![ouilogique.com][img_3]{:style="width:50%;"}][img_3]

[img_3]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_004.jpg

### Conclusion

> Vu que la LED s’allume, je ne recommande pas le hub *Anne LXL4072201A* !

## Test du hub _Delock 61857_

20 nov. 2015. Test du hub [Delock 61857](https://www.delock.de/produkte/S_61857/merkmale.html) acheté chez [NewConcept Informatique](https://store.ncinformatique.ch/).

### Conclusion

> Vu que la LED ne s’allume pas, je recommande le hub _Delock 61857_ !

### Remarques

Le _Delock 61857_ coûte environ 60 CHF, ce qui est nettement plus cher que les 14 CHF que m’ont coûtés le hub _Anne LXL4072201A_. Mais vu le résultat du test, je pense que c’est de l’argent bien investi.

Ce hub a 10 ports USB (6 devant, 2 derrière et 2 qui peuvent pivoter). Il serait parfait s’il y avait des interrupteurs pour activer et désactiver les ports sans avoir besoin de débrancher les cordons comme sur le hub _Anne LXL4072201A_.

Il a quand même deux défauts agaçants :

-   On entend clairement le sifflement de l’alim à découpage quand il n’y a pas assez de charge. Il y a peut-être aussi une influence de mon MacBook Pro qui a un problème d’alimentation électrique. Je me reçois des châtaignes de temps à autre quand il connecté au 240 V.
-   Ce hub est un véritable sapin de Noël avec sa gigantesque LED bleue qui illumine tout. Le patron de [NewConcept Informatique](https://store.ncinformatique.ch/) utilise d’ailleurs de l’adhésif noir pour la cacher.

Un autre souci de ma config, c’est mon écran Apple Thunderbolt 27". Il a un hub USB intégré sur lequel je branche mon clavier et ma souris. Lorsque j’ai branché le hub Delock sur le hub de l’écran pour la première fois, ça a fait planter l’ordi. Ça m’était déjà arrivé en connectant des cartes Arduino et c’est d’ailleurs pour ça que je préfère les connecter à un hub plutôt que directement sur le Mac ou sur le hub de l’écran. Résultat des courses, il me semble que mon Mac et mon écran ont quelques soucis électriques...

---

Sur cette image, on voit que la LED ne s’allume pas ⇒ donc c’est bon.

[![ouilogique.com][img_4]{:style="width:50%;"}][img_4]

[img_4]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_005_lowres.jpg

---

Sur cette image, on voit que le montage de test fonctionne et que si la LED ne s’est pas allumée dans le test ci-dessus, c’est vraiment parce qu’il n’y avait pas de jus.

[![ouilogique.com][img_5]{:style="width:50%;"}][img_5]

[img_5]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_006_lowres.jpg

---

Pour info, le hub vu de dessous

[![ouilogique.com][img_6]{:style="width:50%;"}][img_6]

[img_6]: ../../files/2015-07-02-usb_hub_test/test_usb_hub_007.jpg

## Référence du matériel de test

-   Connecteur Jack-rapide ~~(https://www.banggood.com/DC-Power-Male-Female-5_5X-2_1mm-Connector-Adapter-Plug-Cable-Pressed-connected-for-LED-Strips-12V-p-998683.html?p=0431091025639201412F)~~
-   [Câble Jack-USB](https://www.banggood.com/USB-Port-to-5_5mm-2_1mm-5V-DC-Barrel-Jack-Power-Cable-Connector-p-997025.html?p=0431091025639201412F) ⇒ ⚠ ce câble a une grande résistance de ligne qui fait chuter considérablement la tension !
-   USB Femelle-Femelle ~~(https://fr.aliexpress.com/item/laptop-High-Speed-blue-USB-3-0-cable-A-Female-TO-A-Female-Adapter-cables-converter/1855157465.html)~~
