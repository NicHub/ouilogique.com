---
layout: page
title: "Un analyseur logique Arduino"
modified:
categories:
excerpt:
tags: []
image:
  feature:
date: 2015-06-12T12:00:00+01:00
author: Nico
---


> Les informations ci-dessous viennent à l’origine d’un tuto qui n’est malheureusement plus en ligne (<http://letsmakerobots.com/node/31422>).

En résumé, cette solution nécessite deux programmes :

1. Le croquis Arduino : <https://github.com/gillham/logic_analyzer>
2. Le programme de capture *Logic Sniffer* sur l’ordinateur : <https://www.lxtreme.nl/ols/#download>



Il y a un article sur le site de Mouser qui en parle aussi : <http://www.mouser.com/blog/arduino-3-powerful-yet-overlooked-uses/>

Et voilà ce que ça donne en action :



![](https://www.lxtreme.nl/ols/img/logo.png)

![](/files/2015-06-12-logic_sniffer/2015-04-22_analyseur_logique.png)

![](/files/2015-06-12-logic_sniffer/2015-04-22_RF433_proto_1.jpg)



---

## Logiciels pour la visualisation des traces

Pour l’analyse post-mortem, il y a :

- [GTKWave](http://gtkwave.sourceforge.net/)
- [Scansion — Logic Poet](http://www.logicpoet.com/scansion/)
- [Et d’autres sur Wikipedia](https://en.wikipedia.org/wiki/Waveform_viewer)

Le format d’enregistrement des traces que j’utilise est le [VCD (Value Change Dump)](https://en.wikipedia.org/wiki/Value_change_dump)

---



