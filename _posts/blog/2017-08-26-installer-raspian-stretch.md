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
- Quand Etcher a terminé, créer un fichier vide appelé “ssh” à la racine de la carte SD. N’importe quel éditeur de texte fera l’affaire. On peut aussi utiliser la commande suivante dans le terminal :<br/>`touch /Volumes/boot/ssh`.
- Éjecter la carte SD dans le Finder.
- Insérer la carte SD dans le Raspberry.
- Connecter le câble Ethernet.
- Brancher le câble d’alimentation du Raspberry.
- Après environ 30 secondes, se connecter au Raspberry avec la commande<br/>`ssh pi@raspberrypi.local`. Le mot de passe par défaut est `raspberry`. Si une entrée existe déjà pour `raspberrypi.local` dans le fichier `~/.ssh/known_hosts` de l’ordinateur hôte (pas le RPi), il faut la supprimer.

## Mise à jour de Raspbian

```bash
sudo apt-get --assume-yes update # ~23 s
sudo apt-get --assume-yes dist-upgrade # ~3 min
```

## Configuration

```bash
nano ~/.bash_profile
```

Copier-coller les commandes suivantes dans .bash_profile

```bash
PS1=$'\n\n\xf0\x9f\x98\xBA'"  \t – \[\033[01;32m\]\u@\h\[\033[00m\]:\W > "
alias ll='ls -lGhF'
alias la='ls -a'
alias gs='git status'
alias lsserial='python3 -m serial.tools.list_ports'
IP=$(hostname -I | awk '{print $1}')
alias pyserver='PORT=4000; echo -e "\nhttp://localhost:$PORT"; echo -e "http://$IP:$PORT\n"; /usr/bin/python3 -m http.server $PORT'
```

```bash
source ~/.bash_profile
```

```bash
sudo raspi-config
# Localisation Options
# Interfacing Options / P2 SSH
# Update
# Advanced Options / Expand filesystem
```


## SSH

**Sur l’ordinateur hôte**

```bash
cd ~/.ssh
# Si le fichier ~/.ssh/id_rsa.pub n’existe pas,
# il faut le créer avec `ssh-keygen`.
ssh-keygen # Accepter toutes les valeurs par défaut.
cat ~/.ssh/id_rsa.pub # + Copier le résultat dans le presse-papier.
```

**Sur le RPi**

```bash
mkdir ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys # + Coller la clé de l’hôte à la fin du fichier.
chmod 644 ~/.ssh/authorized_keys
```

## Permissions de fichiers courants

```bash
chmod 700 ~/.ssh
chmod 644 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
chmod 644 ~/.ssh/config
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/github_rsa
chmod 644 ~/.ssh/github_rsa.pub
chmod 600 ~/.ssh/mozilla_rsa
chmod 644 ~/.ssh/mozilla_rsa.pub
```


## VNC

```bash
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
```

```bash
sudo raspi-config
# - Navigate to Interfacing Options.
# - Scroll down and select VNC > Yes.
```


## Enlever les programmes inutiles

Enfin, inutiles pour moi....

```bash
df -h # Pour voir la capacité de la carte SD
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
df -h # Vous venez de libérer 1.1 GB !
```


## Réinstaller un programme qu’on croyait inutile

```bash
sudo apt-get --assume-yes update
sudo apt-get --assume-yes install wolfram-engine
```


## Ajouter quelques programmes utiles

### TMUX

```bash
sudo apt --assume-yes install tmux

tmux # crée et démarre un nouveau shell
mux new -s session_name  # idem mais avec un nom de session
tmux detach # détache du shell en cours

# ctrl-B S # liste les shells tmux
# ctrl-B D # revient au shell principal

tmux ls # liste les shells tmux
tmux a -t 0 # revient au shell tmux 0
tmux a # revient au dernier shell utilisé
exit # quitte et détruit le shell en cours

tmux kill-session -t 0 # détruit une session détachée

# Par défaut, la roulette de la souris fait défiler
# l’historique des commandes. Pour que la roulette
# fasse défiler l’écran, il faut éditer le fichier
~/.tmux.conf
# et ajouter le paramètre
set-option -g mouse on
# Il ne s’appliquera qu’aux nouveaux shells et pas
# aux shells existants, mais on peut le faire dans
# chaque shell individuel avec la commande
tmux set-option -g mouse on

```


### GNU screen

```bash
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
python3 -m serial.tools.list_ports
screen /dev/ttyACM0 115200
# ctrl-A K # pour arrêter la transmission série
```


## Partager un espace disque avec samba

> Source : <https://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/>

### Sur le Raspberry

Installer samba

```bash
sudo apt-get install --assume-yes samba samba-common-bin
```

Éditer la configuration

```bash
sudo nano /etc/samba/smb.conf
```

Au début du fichier, vérifier les informations suivantes :

```conf
workgroup = WORKGROUP
wins support = yes
```

À la fin du fichier, ajouter les informations suivantes :
```conf
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
```

Le flag `public = no` indique que l’accès en temps qu’invité est désactivé. Si on le change en `public = yes`, le disque est partagé en lecture seule.

```bash
sudo smbpasswd -a pi
```

### Monter le disque partagé sur macOS

Dans le Finder :

```bash
⌘ K
smb://raspberrypi.local
```

### Monter le disque partagé sur Windows

Voir <https://support.microsoft.com/fr-ch/help/4026635/windows-map-a-network-drive>

```bash
smb://raspberrypi.local
```

### Installer une autre version de Python 3

> Edit du 16 octobre 2019 : Raspbian Buster intègre la version 3.7.3 de Python.
>
> Avant d’installer une nouvelle version de Python 3, il est prudent de vérifier la version installée sur le Raspberry avec la commande
>
> `python3 --version`

Raspbian Stretch propose la version 3.5 de Python. Comme Python 3.6 apporte de nouvelles fonctionnalités comme les *f-strings* et que le module `asyncio` a été amélioré, je pense que c’est intéressant de l’installer aussi. L’idée est aussi de pouvoir tester le module [quart][quart].

Source : <https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/>
Les versions de Python disponibles sont téléchargeables à : <https://www.python.org/ftp/python/>
Temps d’installation : environ 30 min.
Cette procédure n’écrase pas les versions de Python existantes.

Cette procédure montre comment installer Python 3.6.7.
> J’ai aussi essayé d’installer la version 3.7.1 et l’installation a réussi, mais malheureusement pip ne fonctionnait pas, donc il m’était impossible d’installer de nouveaux modules.

```bash
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
cd ~ && sudo rm -rf temp
```

Créer un lien pour que Python 3.6 soit la version de Python 3 par défaut. Ceci nous permettra d’indiquer le *shebang* `#!/usr/bin/env python3` au début des scripts et de les exécuter avec la commande `python3 <nom_du_script.py>`.

```bash
which python3.6 # /usr/local/bin/python3.6
python3.6 -V # Python 3.6.7
sudo ln -sf /usr/local/bin/python3.6 /usr/local/bin/python3
/usr/bin/env python3 -V # Python 3.6.7
which python3 # /usr/local/bin/python3
```

Pour installer des modules

> Si `pip install <module>` ne fonctionne pas, on peut utiiser les commandes suivantes :

```bash
sudo python3.6 -m pip install --upgrade pip
sudo python3.6 -m pip install quart
```

[quart]: https://gitlab.com/pgjones/quart
