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
  - /blog/gphoto2/
---

<!--
Ancienne URL
http://ouilogique.com/gphoto2/
-->

# Installation de GPhoto2 sur Raspbian Stretch

	sudo apt-get --assume-yes install gphoto2
	sudo chmod -x /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
	sudo reboot

	ssh pi@raspberrypi.local
	mkdir gphoto2
	cd gphoto2/
	gphoto2 -v # gphoto2 2.5.11
	# Connecter un appareil de photo au RPi
	gphoto2 --auto-detect
	gphoto2 --capture-image-and-download --interval 2 --frames 2 --filename=image_%Y-%m-%d_%H-%M-%S.jpg
