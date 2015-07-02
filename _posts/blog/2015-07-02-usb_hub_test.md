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

![](/files/2015-07-02-usb_hub_test/test_usb_hub_001.jpg)

Sur cette image, on voit que je me suis gouré et que j’ai mis la résistance de 100 Ω en série. Comme la LED s’allume quand même, ça montre que le hub n’a pas de protection circuit ouvert (haute impédance.)

![](/files/2015-07-02-usb_hub_test/test_usb_hub_002.jpg)

---

Ce test m’a été généreusement transmis par Jean-Marc. Merci à lui.

Voici les illustrations qu’il m’a transmises :

![](/files/2015-07-02-usb_hub_test/test_usb_hub_003.png)
![](/files/2015-07-02-usb_hub_test/test_usb_hub_004.jpg)
![](/files/2015-07-02-usb_hub_test/test_usb_hub_005.jpg)

