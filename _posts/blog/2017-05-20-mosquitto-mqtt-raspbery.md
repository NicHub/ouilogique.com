---
layout: page
title: "Installer Mosquitto MQTT sur un Raspberry Pi"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-05-20T16:00:00+02:00
published: false
author: Nico
---


## Matériel

- Un Raspberry Pi (testé avec un Raspberry Pi 2, Raspbian Jessie With Pixel)
- Un Mac (testé avec macOS Sierra)


## Installation de Raspi

Cette étape est optionnelle. Elle est surtout utile si vous voulez démarrer de zéro.

- Télécharger [Raspbian Jessie with Pixel][1] au format zip. Pas besoin de décompresser le zip.
- Télécharger [Etcher][2].
- Insérer la carte SD dans le lecteur du Mac.
- Dans les préférences (icône en forme de roue dentée en haut à droite), décocher “auto-unmount on success”.
- Flasher le fichier zip sur la carte SD avec Etcher.
- Enlever et remettre la carte SD dans le lecteur (parce que par défaut, Etcher démonte le disque après le flashage).
- Créer un fichier texte vide s’appelant `ssh` à la racine de la carte pour autoriser les connexions SSH.
- Insérer la carte SD dans le Raspberry et le démarrer


## Installation de Mosquitto MQTT

- Sur le Mac, ouvrir le Terminal et taper la commande `ssh pi@raspberrypi.local`. Quand SSH demande d’autoriser la connexion, répondre `yes` en toutes lettres, puis entrer le mot de passe par défaut `raspberry`.
- Changer la zone horaire avec `sudo raspi-config`, puis sélectionner `4 Localisation Options/I2 Change Timezone`.
- Installer les mises à jour du système :

{% highlight bash %}
sudo apt-get update # ~ 2 min
sudo apt-get upgrade # ~ 12 min
sudo apt-get dist-upgrade # ~ 0 min
{% endhighlight %}

- Installer GNU `screen` :

{% highlight bash %}
sudo apt-get install screen
nano ~/.screenrc
# Ajouter l’instruction suivante dans ~/.screenrc
shell -$SHELL
{% endhighlight %}

- Installer `mosquitto` :

{% highlight bash %}
sudo apt-get install mosquitto mosquitto-clients python-mosquitto
{% endhighlight %}


- Pour les tests, il faut commenter la ligne suivante dans le fichier `mosquitto.conf`

{% highlight bash %}
sudo nano /etc/mosquitto/conf.d/mosquitto.conf
# Et commenter la ligne ci-dessous
# password_file /etc/mosquitto/passwd
{% endhighlight %}

- Le deamon `mosquitto` accepte les commandes suivantes :
{% highlight bash %}
sudo /etc/init.d/mosquitto status
sudo /etc/init.d/mosquitto start
sudo /etc/init.d/mosquitto stop
sudo /etc/init.d/mosquitto reload
sudo /etc/init.d/mosquitto try-restart
{% endhighlight %}


Il y a deux fichiers de configuration et les deux semblent être utilisés
{% highlight bash %}
/etc/mosquitto/mosquitto.conf # ⇒ configuration globale
/etc/mosquitto/conf.d/mosquitto.conf # ⇒ configuration pour le daemon
{% endhighlight %}


/var/log/mosquitto/mosquitto.log
/var/lib/mosquitto/mosquitto.db



mosquitto_sub -h test.mosquitto.org -t "SMBA38/#" –v

pi@raspberrypi:~$ mosquitto_pub -h test.mosquitto.org -t SMBA38/temps/Ext -m 17
pi@raspberrypi:~$ mosquitto_pub -h test.mosquitto.org -t SMBA38/temps/Ext -m 15
pi@raspberrypi:~$ mosquitto_pub -h test.mosquitto.org -t SMBA38/temps/Int -m 21




brew install mosquitto

/usr/local/etc/mosquitto/mosquitto.conf

brew services start mosquitto

mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf




[1]: https://www.raspberrypi.org/downloads/raspbian/
[2]: https://etcher.io/
