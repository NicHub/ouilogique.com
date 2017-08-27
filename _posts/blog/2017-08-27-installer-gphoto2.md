---
layout: page
title: "Installer GPHOTO2"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-08-27T01:00:00+02:00
published: true
author: Nico
redirect_from:
  - http://ouilogique.com/gphoto2/
---

<!--
Ancienne URL
http://ouilogique.com/gphoto2/
-->


# Installation de GPHOTO2 sur *MacOS Sierra*

L’installation de GPHOTO2 sur *MacOS Sierra* se fait avec [Homebrew](https://brew.sh/index_fr.html)

	brew update
	brew install gphoto2
	# Ou pour mettre à jour
	brew upgrade gphoto2
	gphoto2 -v # gphoto2 2.5.14



# Installation de GPHOTO2 sur *Raspbian Stretch*

> GPHOTO2 n’est disponible qu’à la version 2.5.4 sur *Raspbian Jessie* avec la commande `sudo apt-get install gphoto2`. Il est donc préférable d’utiliser [*Raspbian Stretch*][1].

	sudo apt-get --assume-yes install gphoto2
	gphoto2 -v # gphoto2 2.5.11

> GPHOTO2 entre en conflit avec *gvfs-gphoto2-volume-monitor* et il est donc nécessaire de le désactiver avec les commandes suivantes :

	sudo chmod -x /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
	sudo reboot
	ssh pi@raspberrypi.local


# Quelques commandes utiles

	# Connecter un appareil de photo.
	# J’ai testé avec un Nikon DSC D3200 et ça fonctionne
	gphoto2 --auto-detect
	gphoto2 --abilities
	gphoto2 --summary
	gphoto2 --list-ports
	mkdir gphoto2
	cd gphoto2/
	gphoto2 --capture-image-and-download --interval 2 --frames 2 --filename=image_%Y-%m-%d_%H-%M-%S.jpg



# Quelques liens

- <http://gphoto.org/>
- <http://lists.alioth.debian.org/pipermail/pkg-phototools-devel/2017-June/010392.html>
- <https://github.com/gphoto/gphoto2>
- <https://github.com/gphoto/gphoto2/issues/72>
- <https://www.raspberrypi.org/forums/viewtopic.php?t=186405>
- <http://archive.raspbian.org/raspbian/pool/main/g/gphoto2/>

 [1]: http://ouilogique.com/installer-raspian-stretch/

