---
layout: post
title: "Test d’un hub USB"
modified:
categories: blog
excerpt:
tags: []
image:
  feature:
date: 2015-07-02T09:47:00+01:00
---

Test du hub USB de la marque *Anne*, modèle *LXL4072201A*, acheté sur [Aliexpress](http://fr.aliexpress.com/item/2014-newest-7-Port-USB-3-0-HUB-High-Speed-With-Power-Adapter-For-Laptop-Notebook/1997348166.html).


Le test consiste à placer une diode entre les pattes d’alimentation de la fiche USB qui est normalement connectée à l’ordinateur. Une résistance de 100 Ω peut être ajoutée en parallèle pour s’assurer que le hub détecte une charge et éviter ainsi l’enclenchement de la sécurité de haute impédance du hub. Le hub testé n’a visiblement pas cette protection puisque la LED s’est allumée sans la résistance de 100 Ω. Le hub doit être alimenté pendant le test.

> Vu que la LED s’allume, je ne recommande pas le hub LXL4072201A !

À noter en plus que la LED s’allume même si la résistance de 100 Ω n’est pas connectée.

<img src="/files/2015-07-02-usb_hub_test/test_usb_hub_003.png" alt="" width="300">

![](/files/2015-07-02-usb_hub_test/test_usb_hub_001.jpg)

![](/files/2015-07-02-usb_hub_test/test_usb_hub_004.jpg)


