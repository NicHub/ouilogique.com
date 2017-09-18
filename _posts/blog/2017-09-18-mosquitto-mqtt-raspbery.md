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


## Matériel

- Un Raspberry Pi (testé avec un Raspberry Pi 2, Raspbian Stretch)
- Un Mac (testé avec macOS Sierra)


## Installation de Raspian Stretch

J’ai testé la procédure ci-dessous avec une installation propre de Raspian Stretch.

<http://ouilogique.com/installer-raspian-stretch/>


# Installation et compilation de mosquitto 1.4.14

Les informations ci-dessous sont tirées de ce blog :

<https://jolabsblog.wordpress.com/2016/10/31/setting-up-a-custom-home-automation-server/>

{% highlight bash %}

mkdir ~/mosquitto
cd ~/mosquitto/

sudo apt-get --assume-yes install build-essential python quilt devscripts python-setuptools python3 libssl-dev cmake libc-ares-dev uuid-dev daemon
sudo apt-get --assume-yes install zlibc zlib1g zlib1g-dev

git clone https://github.com/warmcat/libwebsockets.git
cd libwebsockets
mkdir build
cd build
cmake .. && sudo make install && sudo ldconfig

cd ~/mosquitto
MOSQUITTO_VER=mosquitto-1.4.14
wget https://mosquitto.org/files/source/$MOSQUITTO_VER.tar.gz
tar zxvf $MOSQUITTO_VER.tar.gz
cd $MOSQUITTO_VER
sudo nano config.mk # WITH_WEBSOCKETS:=yes

make && sudo make install
sudo cp mosquitto.conf /etc/mosquitto
sudo adduser mosquitto

sudo nano /etc/mosquitto/mosquitto.conf
# Trouver et modifier les lignes suivantes :
port 1883
listener 9001
protocol websockets
pid_file /var/run/mosquitto.pid

# Optional: I'm going to add security by forcing credentials
# You can do so by creating as password file:
mosquitto_passwd -c /etc/mosquitto/passwd yourloginname
sudo nano /etc/mosquitto/mosquitto.conf
allow_anonymous false


sudo ln -s /usr/local/sbin/mosquitto /bin/mosquitto
sudo reboot

# Pour démarrer mosquitto manuellement
mosquitto -c /etc/mosquitto/mosquitto.conf

# Pour démarrer mosquitto automatiquement lors du boot du Raspberry
sudo nano /etc/systemd/system/mosquitto.service

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


sudo systemctl enable mosquitto
sudo systemctl start mosquitto

sudo reboot

pidof mosquitto
mosquitto -v

{% endhighlight %}



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
