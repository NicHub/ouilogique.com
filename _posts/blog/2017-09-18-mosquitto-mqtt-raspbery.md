---
layout: page
title: "Installer Mosquitto MQTT avec WebSocket sur un Raspberry Pi"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-09-18T18:43:00+02:00
published: true
author: Nico
---


# Matériel

- Un Raspberry Pi (testé avec un Raspberry Pi 2, Raspbian Stretch)
- Un Mac (testé avec macOS Sierra)


# Installation de Raspian Stretch

J’ai testé la procédure ci-dessous avec une installation propre de Raspian Stretch.

<https://ouilogique.com/installer-raspian-stretch/>


# Installation et compilation de mosquitto 1.4.14

Les informations ci-dessous sont tirées de ce blog avec quelques adaptations :

<https://goo.gl/BQh6hA>

{% highlight bash %}

# Installation des dépendances
sudo apt-get --assume-yes install \
build-essential \
python \
quilt \
devscripts \
python-setuptools \
python3 \
libssl-dev \
cmake \
libc-ares-dev \
uuid-dev \
daemon \
zlibc \
zlib1g \
zlib1g-dev

# Compilation de libwebsockets
git clone https://github.com/warmcat/libwebsockets.git
cd libwebsockets
mkdir build
cd build
cmake .. && sudo make install && sudo ldconfig

# Compilation de mosquitto
mkdir ~/mosquitto
cd ~/mosquitto/
MOSQUITTO_VER=mosquitto-1.4.14
wget https://mosquitto.org/files/source/$MOSQUITTO_VER.tar.gz
tar zxvf $MOSQUITTO_VER.tar.gz
cd $MOSQUITTO_VER

# Configuration des options de compilation de mosquitto
# Changer la ligne : WITH_WEBSOCKETS:=yes
sudo nano config.mk

make && sudo make install
sudo cp mosquitto.conf /etc/mosquitto

# Ajout de l’utilisateur “mosquitto”
sudo adduser mosquitto

# Configuration des options de mosquitto
sudo nano /etc/mosquitto/mosquitto.conf
# Trouver et modifier les lignes suivantes :
port 1883
listener 9001
protocol websockets
pid_file /var/run/mosquitto.pid

# Optionnellement, on peut ajouter une couche
# de sécurité en créant un fichier de mot de passe
mosquitto_passwd -c /etc/mosquitto/passwd yourloginname
sudo nano /etc/mosquitto/mosquitto.conf
allow_anonymous false

# Création d’un lien
sudo ln -s /usr/local/sbin/mosquitto /bin/mosquitto

# Redémarrage
sudo reboot

# Pour démarrer mosquitto manuellement
mosquitto -c /etc/mosquitto/mosquitto.conf

# Pour démarrer mosquitto automatiquement
# lors du boot du Raspberry
sudo nano /etc/systemd/system/mosquitto.service

# Mettre les infos suivantes
# dans le fichier “mosquitto.service”
# Voir <https://goo.gl/wMCZFv> pour plus d’infos
[Unit]
Description=Mosquitto MQTT Broker daemon
ConditionPathExists=/etc/mosquitto/mosquitto.conf
Requires=network.target

[Service]
Type=simple
ExecStartPre=/bin/rm -f /run/mosquitto.pid
ExecStart=/usr/local/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -d
ExecReload=/bin/kill -HUP $MAINPID
PIDFile=/run/mosquitto.pid
Restart=on-failure

[Install]
WantedBy=multi-user.target

# Activer le service
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

# À partir d’ici, mosquitto démarrera avec le système
sudo reboot

# Vérifier que tout fonctionne
pidof mosquitto
mosquitto -v

{% endhighlight %}

# Pour tester

{% highlight bash %}
mosquitto_sub --host raspberrypi.local --topic "SUPERTEST/#"
{% endhighlight %}

{% highlight bash %}
mosquitto_pub --retain --host raspberrypi.local --topic "SUPERTEST" \
--message '{"DATE":"'"`date "+%Y-%m-%dT%H:%M:%S+02:00"`"'"}'
{% endhighlight %}


{% comment %}
<!--

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


-->
{% endcomment %}