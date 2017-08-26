---
layout: page
title: "Installer Raspian Stretch sur Raspberry Pi"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-08-26T18:26:00+02:00
published: true
author: Nico
---

## Matériel utilisé pour cette procédure

- Un Raspberry Pi modèle 2
- Une carte SD 32 GB
- Un ordinateur Mac OS Sierra
- Un routeur
- Un câble ethernet

> Pas besoin d’écran, de clavier ou de souris pour le Raspberry, nous utiliserons uniquement SSH pour nous connecter au RPi depuis le Mac.

## Préparation (~15 min)

- Télécharger RASPBIAN STRETCH WITH DESKTOP (1.76 Go) <https://www.raspberrypi.org/downloads/raspbian/>
- Décompresser l’archive `2017-08-16-raspbian-stretch.zip`. Elle contient une image disque qui se nomme `2017-08-16-raspbian-stretch.img`. Sur MacOS Sierra, l’utilitaire d’archive par défaut se débrouille très bien pour la décompression.
- Télécharger et installer Etcher <https://etcher.io/>
- Ouvrir Etcher et dans les options (icône en forme de roue dentée en haut à droite), décocher l’option “Auto-unmount on success”, puis cliquer sur “Back” pour revenir à l’écran d’accueil.

## Procédure d’installation (~30 min)

- Dans Etcher, cliquer sur “Select image” et choisir le fichier “2017-08-16-raspbian-stretch.img”.
- Insérer la carte SD et vérifier qu’Etcher l’a bien détectée.
- Cliquer sur “Flash”. Entrez votre mot de passe lorsque le dialogue le demande. L’écriture de l’image disque prend environ 15 min et la vérification (si elle a été sélectionnée dans les préférences) prend aussi 15 min. Ces temps peuvent beaucoup varier en fonction de votre matériel.
- Quand Etcher a terminé, créer un fichier vide appelé “ssh” à la racine de la carte SD. N’importe quel éditeur de texte fera l’affaire. On peut aussi utiliser la commande suivante dans le terminal<br/>`touch /Volumes/boot/ssh`.
- Éjecter la carte SD dans le Finder.
- Insérer la carte SD dans le Raspberry.
- Connecter le câble Ethernet.
- Brancher le câble d’alimentation du Raspberry.
- Après environ 30 secondes, se connecter au Raspberry avec la commande<br/>`ssh pi@raspberrypi.local`. Le mot de passe par défaut est `raspberry`. Si une entrée existe déjà pour `raspberrypi.local` dans le fichier `~/.ssh/known_hosts`, il faut la supprimer.

## Mise à jour de Raspbian

    sudo apt-get --assume-yes update # ~23 s
    sudo apt-get --assume-yes dist-upgrade # ~3min

## Configuration

	nano ~/.bash_profile

	PS1=$'\n\n\xf0\x9f\x98\xBA'"  \t – \[\033[01;32m\]\u@\h\[\033[00m\]:\W > "
	alias ls='ls -lGhF'
	alias la='ls -a'
	alias gs='git status'

	source ~/.bash_profile

	sudo raspi-config
	# Localisation Options
	# Update


