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

-   Un Raspberry Pi modèle 2
-   Une carte SD 32 GB
-   Un ordinateur macOS Sierra
-   Un routeur
-   Un câble Ethernet

> Pas besoin d’écran, de clavier ou de souris pour le Raspberry, nous utiliserons uniquement SSH pour nous connecter au RPi depuis le Mac.

## Préparation (~15 min)

-   Télécharger RASPBIAN STRETCH WITH DESKTOP (1.76 Go)
    <https://www.raspberrypi.org/downloads/raspbian/>.
-   Décompresser l’archive
    `2017-08-16-raspbian-stretch.zip`.
    Elle contient une image disque qui se nomme
    `2017-08-16-raspbian-stretch.img`.
    Sur macOS Sierra, l’utilitaire d’archive par défaut se débrouille très bien pour la décompression.
-   Télécharger et installer Etcher
    <https://etcher.io/>.
-   Ouvrir Etcher et dans les options (icône en forme de roue dentée en haut à droite), décocher l’option “Auto-unmount on success”, puis cliquer sur “Back” pour revenir à l’écran d’accueil.

## Procédure d’installation (~30 min)

-   Dans Etcher, cliquer sur “Select image” et choisir le fichier “2017-08-16-raspbian-stretch.img”.
-   Insérer la carte SD et vérifier qu’Etcher l’a bien détectée.
-   Cliquer sur “Flash”.
    Entrez votre mot de passe lorsque le dialogue le demande.
    L’écriture de l’image disque prend environ 15 min et la vérification (si elle a été sélectionnée dans les préférences) prend aussi 15 min.
    Ces temps peuvent beaucoup varier en fonction de votre matériel.
-   Quand Etcher a terminé, créer un fichier vide appelé “ssh” à la racine de la carte SD.
    N’importe quel éditeur de texte fera l’affaire.
    On peut aussi utiliser la commande suivante dans le terminal :<br/>
    `touch /Volumes/boot/ssh`.
-   Éjecter la carte SD dans le Finder.
-   Insérer la carte SD dans le Raspberry.
-   Connecter le câble Ethernet.
-   Brancher le câble d’alimentation du Raspberry.
-   Après environ 30 secondes, se connecter au Raspberry avec la commande<br/>
    `ssh pi@raspberrypi.local`.
    Le mot de passe par défaut est `raspberry`.
    Si une entrée existe déjà pour `raspberrypi.local` dans le fichier `~/.ssh/known_hosts` de l’ordinateur hôte (pas le RPi), il faut la supprimer.

## Retrouver un appareil sur le réseau local

Si on doit retrouver un Raspberry sur le réseau, la première commande à essayer est<br/>
`ping -c1 raspberrypi.local`.
Mais si on ne connait pas le nom du Raspberry, alors il faut balayer toutes les adresses possibles (_network scan_).
Il y a deux commandes utiles pour cela, `arp` et `nmap`. Sur la commande `nmap` doit être installée via Homebrew.
Pour ceux qui préfèrent les GUI, il y a aussi [Zenmap](https://nmap.org/zenmap/).

```bash
arp -a
```

```bash
nmap -sP 192.168.1.0/24
```

## Mise à jour de Raspbian

```bash
sudo apt-get --assume-yes update
sudo apt-get --assume-yes upgrade
sudo apt-get --assume-yes dist-upgrade
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
TIMEFORMAT=$'\nElapsed time: %E'

###
# Create virtual environment for python3 (once)
# cd $HOME && python3 -m venv pyenv
# and activate it (for each terminal)
##
VENVPATH="$HOME/pyenv/bin/activate"
if [[ -f "$VENVPATH" ]]; then source "$VENVPATH"; fi
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

## Selection des interfaces utilisateurs

Par défaut, l’interface graphique est activée et elle consomme beaucoup de ressources.
Donc si on ne l’utilise pas, il est conseillé de la désactiver.

```bash
sudo raspi-config
# 1 System Options
# S5 Boot / Auto Login
# B2 Console Autologin ou B1 Console
```

## VNC

> N. B. Il faut que l’interface graphique soit activée pour que VNC fonctionne (voir § précédent).

```bash
sudo raspi-config
# 3 Interfacing Options / I3 VNC <Yes>.

# Si l’option n’est pas visible, il faut
# installer VNC au préalable avec la commande :
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
```

Télécharger un client VNC pour se connecter au serveur VNC du rPi.
Par exemple RealVNC :
<https://www.realvnc.com/download/viewer/>.

> N. B. Le client VNC installé par défaut sur macOS ne fonctionne pas pour se connecter au serveur VNC du rPI.
> L’erreur retournée est<br />_Le logiciel de l’ordinateur distant semble ne pas être compatible avec cette version de Partage d’écran._<br />`bash /System/Library/CoreServices/Applications/Screen\ Sharing.app`

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
tmux new -s session_name  # idem mais avec un nom de session
tmux detach # pour se détacher du shell en cours

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
# ~/.tmux.conf
nano ~/.tmux.conf
# et ajouter le paramètre
set-option -g mouse on
# Il ne s’appliquera qu’aux nouveaux shells et pas
# aux shells existants, mais on peut le faire dans
# chaque shell individuel avec la commande
tmux set-option -g mouse on
# En mode mouse on, il n'est possible de sélectionner
# du texte. Il faut donc revenir en mode off.
tmux set-option -g mouse off
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
sudo apt-get --assume-yes install samba samba-common-bin
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

Le flag `public = no` indique que l’accès en temps qu’invité est désactivé.
Si on le change en `public = yes`, le disque est partagé en lecture seule.

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

Voir
<https://support.microsoft.com/fr-ch/help/4026635/windows-map-a-network-drive>

On peu aussi entrer le chemin d’accès au Raspberry au [format UNC](https://en.wikipedia.org/wiki/Path_(computing)#Universal_Naming_Convention) directement dans la barre d’adresse de l’explorateur Windows (raccourcis Win+E, Ctrl+L)

```bash
\\raspberrypi.local
```

### Installer une autre version de Python 3

> Les informations de ce chapitre sont passablement obsolètes car les dernières versions de l’OS du rPi intègrent des versions de Python supérieures à 3.6.
> Donc avant d’installer une nouvelle version de Python 3, il est prudent de vérifier la version installée sur le Raspberry avec la commande

```bash
python3 --version
```

> On peut aussi vérifier la version de l’OS avec la commande

```bash
cat /etc/os-release
```
>
> Édit du 16 octobre 2019 : Raspbian Buster intègre la version 3.7.3 de Python.
> Édit du 11 février 2023 : Raspberry Pi OS Bullseye 64 bit intègre la version 3.9.2 de Python.

Raspbian Stretch propose la version 3.5 de Python. Comme Python 3.6 apporte de nouvelles fonctionnalités comme les _f-strings_ et que le module `asyncio` a été amélioré, je pense que c’est intéressant de l’installer aussi. L’idée est aussi de pouvoir tester le module [quart][quart].

Source : <https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/>
Les versions de Python disponibles sont téléchargeables à : <https://www.python.org/ftp/python/>
Temps d’installation : environ 30 min.
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

Créer un lien pour que Python 3.6 soit la version de Python 3 par défaut.
Ceci nous permettra d’indiquer le _shebang_ `#!/usr/bin/env python3` au début des scripts et de les exécuter avec la commande `python3 <nom_du_script.py>`.

```bash
which python3.6 # /usr/local/bin/python3.6
python3.6 -V # Python 3.6.7
sudo ln -sf /usr/local/bin/python3.6 /usr/local/bin/python3
/usr/bin/env python3 -V # Python 3.6.7
which python3 # /usr/local/bin/python3
```

Pour installer des modules

> Si `pip install <module>` ne fonctionne pas, on peut utiliser les commandes suivantes :

```bash
sudo python3.6 -m pip install --upgrade pip
sudo python3.6 -m pip install quart
```

[quart]: https://gitlab.com/pgjones/quart

### picocom

Picocom est un terminal série.

```bash
sudo apt-get --assume-yes install picocom

picocom -b 115200 -p 1 -c /dev/tty
```

Pour pouvoir l’utiliser sans être sudoer, il faut que l’utilisateur courant fasse partie du groupe dialout (et peut-être des groupes plugdev et input, je ne suis plus sûr).
Il faut redémarrer le rPi pour que le changement soit pris en compte.

```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
sudo usermod -a -G input $USER
sudo reboot
```

## Arrêter ou redémarrer un Raspberry

Ce n’est pas une bonne idée de juste tirer la prise quand on veut arrêter ou redémarrer son Raspberry.
En effet, au bout de quelque temps, le système se retrouve avec un grand nombre de fichiers partiels et probablement illisibles.
Si des fichiers importants sont touchés, le Raspberry peut devenir inutilisable.

Donc pour éteindre un Raspberry, on utilisera une des commandes ci-dessous.
La différence entre elles n’est pas aussi évidente qu’il y parait :
<https://unix.stackexchange.com/a/196471/199660>.
Seule la commande `halt` éteint la LED rouge d’alimentation, donc je suppose que c’est celle qu’il faut privilégier.

> N. B. Attention, aucune de ces commandes ne coupe l’alimentation de la carte ou l’alimentation des ports USB.
> Donc ce n’est pas une bonne option pour éjecter un disque externe par exemple.

```bash
sudo halt
sudo poweroff
sudo shutdown -h now --poweroff
```

Et pour redémarrer un Raspberry, on utilisera une des commandes suivantes

```bash
sudo reboot
sudo shutdown -r now
```

## Lire un disque externe

Lorsqu’on connecte un disque externe, il est automatiquement accessible au chemin `/media/pi/nom_du_disque`.
Ce chemin est ausi appelé _point de montage_.
On peut le voir avec la commande `ls` et accéder aux répertoires avec la commande `cd`.
Dans l’exemple ci-dessous, le disque externe s’appelle `LaCie`.
Ce nom changera avec d’autres fabricants ou si plusieurs disques du même fabricant sont utilisés en même temps.
Il faut tenir compte de ce fait lorsqu’on écrit des scripts et des programmes qui utilisent le chemin du point de montage.

```bash
ls -l /media/pi/
cd /media/pi/LaCie
```

## Éjecter un disque externe

> N. B. À proprement parler, seuls les médias comme les CD où les bandes peuvent être éjectés. Mais le terme est aussi utilisé pour les autres médias.

Éjecter un média est un peu plus compliqué que de le connecter et l’utiliser.
En effet, sur un Raspbery ou n’importe quel [système \*nix](https://fr.wikipedia.org/wiki/Type_Unix), il faut comprendre trois notions :

-   Les disques
-   Les partitions
-   Les points de montage

Pour explorer ces concepts, utilisons la commande `lsblk`.

```bash
lsblk --output NAME,PATH,RM,RO,ROTA,TYPE,SIZE,FSAVAIL,MOUNTPOINT
```

```bash
NAME        PATH           RM RO ROTA TYPE  SIZE FSAVAIL MOUNTPOINT
sda         /dev/sda        0  0    1 disk  4.5T
├─sda1      /dev/sda1       0  0    1 part  200M
└─sda2      /dev/sda2       0  0    1 part  4.5T      1T /media/pi/LaCie
mmcblk0     /dev/mmcblk0    0  0    0 disk 29.7G
├─mmcblk0p1 /dev/mmcblk0p1  0  0    0 part  256M  201.8M /boot
└─mmcblk0p2 /dev/mmcblk0p2  0  0    0 part 29.5G     24G /
```

Les résultats affichés par la commande `lsblk`ci-dessus montrent deux disques appelés `sda`et `mmcblk0`.
Ils ont chacun deux partitions `sda1`, `sda2`, `mmcblk0p1` et `mmcblk0p2`.
Et ils ont chacun un ou deux points de montage `/media/pi/LaCie`, `/boot` et `/`.
On peut différencier les disques des partitions dans le dessin de la structure hiérarchique de la première colonne NAME et aussi dans la colonne TYPE.

L’éjection du disque se passe en deux étapes :

1. Démonter ses points de montage.
   Dans le cas présenté, il n’en a qu’un qui est monté à `/media/pi/LaCie`, mais dont la référence se trouve à `/dev/sda2`.
2. Couper l’alimentation du disque.
   La référence du disque lui-même se trouve à `/dev/sda`.

> N. B. Il faut s’assurer que le disque n’est plus utilisé, sinon le système refusera de le démonter avec l’erreur `target is busy`.
> C’est à ça que sert le changement de répertoire ci-dessous.

```bash
cd
udisksctl unmount --block-device /dev/sda2
sudo udisksctl power-off --block-device /dev/sda
```

<!--
Voici quelques explications sur ces informations.

- Les disques durs standards sont nommés avec le préfixe `sd`suivi d’une lettre attribuée dans l’ordre alphabétique. Donc le premier disque aura le nom `sda`, le deuxième `sdb`, etc.
  L’acronyme `sd`signifie *SCSI mass-storage driver*. Ici, c’est le pilote qui est SCSI, même si le disque n’est pas SCSI.
- Les stockages NVMe (Non-Volatile Memory Express) sont nommés avec le préfix `nvm`.
- Les stockages MMC (Multi Media Card) sont nommés avec le préfix `nvm`.
 -->

### Pour aller plus loin

-   [What you need to know about disks and disk partitions in Linux](https://linuxbsdos.com/2021/11/27/what-you-need-to-know-about-disks-and-disk-partitions-in-linux/).
-   [What is NVMe SSD technology?](https://www.kingston.com/en/ssd/what-is-nvme-ssd-technology)
-   [What Is an MMC Card - Full Guide](https://recoverit.wondershare.com/memorycard-recovery/what-is-mmc-card.html)

## À voir aussi

-   <https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/>
