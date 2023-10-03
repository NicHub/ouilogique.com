---
author: Nico
date: 2015-06-12 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from:
    - /blog/analyseur_logique_Arduino/
tags: []
title: Un analyseur logique Arduino
---

> Les informations ci-dessous viennent à l’origine d’un tuto qui n’est malheureusement plus en ligne ~~(letsmakerobots.com/node/31422)~~.

En résumé, cette solution nécessite deux programmes :

1. Le croquis Arduino : <https://github.com/gillham/logic_analyzer>
2. Le programme de capture _Logic Sniffer_ sur l’ordinateur : <https://lxtreme.nl/projects/ols/>

Il y a un article sur le site de Mouser qui en parle aussi : <https://www.mouser.com/blog/arduino-powerful-yet-overlooked-uses>

Et voilà ce que ça donne en action :

[![ouilogique.com][img_1]][img_1]

[img_1]: ../../files/2015-06-12-analyseur_logique_Arduino/2015-04-22_analyseur_logique.png

[![ouilogique.com][img_2]][img_2]

[img_2]: ../../files/2015-06-12-analyseur_logique_Arduino/2015-04-22_RF433_proto_1.jpg

[![ouilogique.com][img_3]][img_3]

[img_3]: ../../files/2015-06-12-analyseur_logique_Arduino/2015-04-22_RF433_proto_2.jpg

## Logiciels pour la visualisation des traces

Pour l’analyse post-mortem, il y a :

-   [GTKWave](https://gtkwave.sourceforge.net/)
-   Scansion — Logic Poet ~~(www.logicpoet.com/scansion/)~~
-   [Et d’autres sur Wikipedia](https://en.wikipedia.org/wiki/Waveform_viewer)

Le format d’enregistrement des traces que j’utilise est le [VCD (Value Change Dump)](https://en.wikipedia.org/wiki/Value_change_dump)
