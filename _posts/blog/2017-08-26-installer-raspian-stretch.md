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
- Un ordinateur macOS Sierra
- Un routeur
- Un câble Ethernet

> Pas besoin d’écran, de clavier ou de souris pour le Raspberry, nous utiliserons uniquement SSH pour nous connecter au RPi depuis le Mac.

## Préparation (~15 min)

- Télécharger RASPBIAN STRETCH WITH DESKTOP (1.76 Go) <https://www.raspberrypi.org/downloads/raspbian/>
- Décompresser l’archive `2017-08-16-raspbian-stretch.zip`. Elle contient une image disque qui se nomme `2017-08-16-raspbian-stretch.img`. Sur macOS Sierra, l’utilitaire d’archive par défaut se débrouille très bien pour la décompression.
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

{% highlight bash %}
sudo apt-get --assume-yes update # ~23 s
sudo apt-get --assume-yes dist-upgrade # ~3min
{% endhighlight %}

## Configuration

{% highlight bash %}
nano ~/.bash_profile
{% endhighlight %}

Copier-coller les commandes suivantes dans .bash_profile

{% highlight bash %}
PS1=$'\n\n\xf0\x9f\x98\xBA'"  \t – \[\033[01;32m\]\u@\h\[\033[00m\]:\W > "
alias ls='ls -lGhF'
alias la='ls -a'
alias gs='git status'
IP=$(hostname -I | awk '{print $1}')
alias pyserver='PORT=4000; echo -e "\nhttp://localhost:$PORT"; echo -e "http://$IP:$PORT\n"; /usr/bin/python3 -m http.server $PORT'
{% endhighlight %}

{% highlight bash %}
source ~/.bash_profile
{% endhighlight %}

{% highlight bash %}
sudo raspi-config
# Localisation Options
# Update
# Advanced Options / Expand filesystem
{% endhighlight %}



## VNC

{% highlight bash %}
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
{% endhighlight %}

{% highlight bash %}
sudo raspi-config
# - Navigate to Interfacing Options.
# - Scroll down and select VNC > Yes.
{% endhighlight %}


## Enlever les programmes inutiles

Enfin, inutiles pour moi....

{% highlight bash %}
df -h # Pour voir la capacité de la carte SD
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
df -h # Vous venez de libérer 1.1 GB !
{% endhighlight %}


## Ajouter quelques programmes utiles

### GNU screen

{% highlight bash %}
sudo apt-get --assume-yes install screen
echo "shell -$SHELL" > ~/.screenrc # Pour que screen lise .bash_profile

screen # Démarre un nouveau shell
# ctrl-A ctrl-D # revient au shell principal
screen -ls # liste des shells
screen -r xxxx # xxxx = no du shell que l’on veut activer

# ctrl-A K # arrête le shell en cours
screen -X -S xxxx quit # quitte le shell no xxxx
screen -X -S xxxx kill # arrête le shell no xxxx

# RS232
python -m serial.tools.list_ports
screen /dev/ttyACM0 115200
# ctrl-A K # pour arrêter la transmission série
{% endhighlight %}


## Partager un espace disque avec samba

> Source : <https://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/>

### Sur le Raspberry

Installer samba

    sudo apt-get install --assume-yes samba samba-common-bin

Éditer la configuration

    sudo nano /etc/samba/smb.conf

Au début du fichier, vérifier les informations suivantes :

    workgroup = WORKGROUP
    wins support = yes

À la fin du fichier, ajouter les informations suivantes :

    # Source
    # https://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/
    [PiShare]
     comment = Raspberry Pi Share
     path = /home/pi
     browseable = yes
     writeable = yes
     only guest = no
     create mask = 0777
     directory mask = 0777
     public = no

Le flag `public = no` indique que l’accès en temps qu’invité est désactivé. Si on le change en `public = yes`, le disque partagé est en lecture seule.

    sudo smbpasswd -a pi

### Monter le disque partagé sur macOS

Dans le Finder :

    ⌘ K
    smb://raspberrypi.local

### Monter le disque partagé sur Windows

Voir <https://support.microsoft.com/fr-ch/help/4026635/windows-map-a-network-drive>

    smb://raspberrypi.local


## Installer Python 3.6.7

Source : <https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/>

Temps d’installation environ 40 min.
Cette procédure n’écrase pas les versions de Python existantes.

{% highlight bash %}
sudo apt-get --assume-yes install build-essential checkinstall
sudo apt-get --assume-yes install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
mkdir ~/temp && cd ~/temp
wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz
sudo tar xzf Python-3.6.7.tgz
cd Python-3.6.7
sudo -s
TIMEFORMAT='time : %E'
time (bash configure && make -j4 altinstall)
exit
cd ~ && rm -r temp
{% endhighlight %}

Créer un lien pour que Python 3.6 soit la version de Python 3 par défaut

{% highlight bash %}
which python3.6 # /usr/local/bin/python3.6
python3.6 -V # Python 3.6.7
sudo ln -s /usr/local/bin/python3.6 python3
/usr/bin/env python3 -V # Python 3.6.7
which python3 # /usr/local/bin/python3
{% endhighlight %}

Pour installer des modules

    sudo python3.6 -m pip install --upgrade pip
    sudo python3.6 -m pip install websockets

