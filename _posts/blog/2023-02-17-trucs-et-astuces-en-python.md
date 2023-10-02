---
lang: fr
layout: page
title: "Trucs et astuces en Python"
tags: []
image:
    feature:
date: 2023-02-17T12:00:00+01:00
published: false
author: Nico
---

## Python 2 vs 3

https://www.python.org/doc/sunset-python-2/

# Prérequis

> Note : Sous windows, les commandes ci-dessous doivent être exécutées dans un terminal avec les droit administrateur (Win+R, cmd + Ctrl-Shift-Enter). De plus, la commande pour invoquer python doit changée de `python3` à `py`.

-   Installer la dernière version LTS de [NodeJS](https://nodejs.org/en/download/). Actuellement, c’est la 18.14.2.
-   Installer Python (<https://www.python.org/downloads/>). La version actuelle est la 3.11.2. La version minimum pour suivre les exemples est la 3.6.
-   Mettre à jour `pip`. Choisissez la commande qui correspond à votre système d’exploitation.
    `py -m pip install --upgrade pip &REM Windows`
    `python3 -m pip install --upgrade pip # Systèmes nix`
-   Installer Wheel.
    `py -m pip install wheel --upgrade &REM Windows`
    `python3 -m pip install wheel --upgrade # Systèmes nix`
-   Installer Jupyter.
    `py -m pip install jupyter notebook --upgrade &REM Windows`
    `python3 -m pip install jupyter notebook --upgrade # Systèmes nix`

## Python shell

Les shell Python sont aussi apelé REPL (Read-Eval-Print Loop)

Les shells standards sont :

-   `python` (ou `python3`)

D’autre shells existent :

-   `ipython` (ou `ipython3`) conçu pour l’analyse de données (_data science_)
-   `bpython`

Je vous conseille d’utiliser `ipython3`.
Ses avatages sont :

-   Il ignore les chevrons `>>>` lorsqu’on fait des copier-coller d’exemple du web.
-   Coloration systaxique.
-   Autocomplétion
-   Navigation intelligente dans l’historique des commandes avec les touches `↑`, `↓` du clavier. Si une commande est répartie sur plusieurs lignes, elles sont toutes rappelées d’un coup.
-   Il intègre des “[commandes magiques](https://ipython.readthedocs.io/en/stable/interactive/magics.html)” qui peuvent être très utiles comme la [commande `save`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-save) pour enregistrer la session courante.
-   Il permet d’utiliser quelques commandes Bash directement grâce à la fonctionnalité “run_line_magic

**Voir aussi**

-   https://realpython.com/python-repl/

## Jupyter dans VSCode

Il y a plusieurs façon d’exécuter des scripts Python dans VSCode.
La façon la plus intéressante est avec Jupyter.
Pour

# Raspberry blink Python

<https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/>

Normallement, le module Python `python3-rpi.gpio` est installé d’origine.

````python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
LED_GPIOS = [37, 35, 33, 31, 29, 23]
for led_gpio in LED_GPIOS:
    GPIO.setup(led_gpio, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(LED_GPIOS[0], GPIO.OUT, initial=GPIO.HIGH)
while True:
    GPIO.output(8, GPIO.HIGH) # Turn on
    sleep(1) # Sleep for 1 second
    GPIO.output(8, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second```
````

-   environnements virtuels
-   iPython
-   f-strings
-   VSCode Jupyter

# Remote GPIO

Voir exemple remote_gpio.py
