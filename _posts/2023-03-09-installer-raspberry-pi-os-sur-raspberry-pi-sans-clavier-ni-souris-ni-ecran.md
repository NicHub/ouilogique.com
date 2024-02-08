---
author: Nico
date: 2023-03-09 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from:
    - /installer-raspian-stretch/
tags: []
title: Installer Raspberry Pi OS sur Raspberry Pi sans clavier, ni souris, ni écran
---

Cet article montre comment configurer un Raspberry de A à Z à l’aide d’un ordinateur standard.
Le Raspberry sera donc en mode _headless_, c’est-à-dire sans clavier, ni souris, ni écran.

> N.B. L’article original, écrit en août 2017, s’intitulait “Installer Raspian Stretch sur Raspberry Pi” et était accessible à cette URL :
> <https://ouilogique.com/installer-raspian-stretch/> qui est maintenant redirigée vers l’URL actuelle.

## Matériel utilisé pour cette procédure

-   Un Raspberry Pi modèle 2 (ou plus)
-   Une carte SD (32 Go recommandés)
-   Un ordinateur standard
-   Un routeur (optionnel, on peut connecter le RPi directement sur le port Ethernet)
-   Un câble Ethernet

## Préparation (~15 min)

> N.B. Ce chapitre a été mis à jour en mars 2023

## Choix de l’OS

Anciennement, l’OS du Raspberry s’appelait _Raspbian_ ce qui était logique puisqu’il est basé sur _Debian_.
On devait le télécharger séparément et l’installer avec un programme qui s’appelait _Etcher_.

Aujourd’hui, les choses sont un peu différentes.
_Etcher_ a été remplacé par _Raspberry Pi Imager_ et on a plus besoin de télécharger l’OS séparément, car c’est le programme qui s’en charge.
Il peut être téléchargé ici :

-   <https://www.raspberrypi.com/software/>

On a le choix entre plusieurs moutures de l’OS.
Celle que je préfère est la version “Raspberry Pi OS (64-bit)”.
La raison est que j’ai besoin d’un OS 64 bit pour faire tourner Prince (<https://www.princexml.com/>).
En cas de doute, il vaut mieux choisir l’OS recommandé, c’est-à-dire “Raspberry Pi OS (32-bit)”.

## Choix du terminal

Si vous êtes sur macOS ou n’importe quel système \*nix, le choix est vite fait, il suffit d’utiliser le terminal par défaut.
Ça ne veut pas dire qu’il n’y a qu’une possibilité, mais qu’il y a de fortes chances que vous sachiez déjà quel terminal choisir.

Par contre si vous êtes sur Windows, il y a de fortes chances que vous ne sachiez pas quel terminal choisir.
Donc voici quelques possibilités.

-   Windows PowerShell (intégré à Windows)
-   COMMAND.COM (cmd) (intégré à Windows)
-   [MinGW – Git Bash installé avec Git](https://git-scm.com/)
-   [Cygwin](https://www.cygwin.com/)
-   [PuTTY](https://putty.org/)

## Procédure d’installation (~30 min)

-   Sur un ordinateur standard (pas le Raspberry), [télécharger _Raspberry Pi Imager_](https://www.raspberrypi.com/software/) et l’installer.
-   Dans _Raspberry Pi Imager_, cliquer sur “Système d’exploitation” et [sélectionner l’OS de votre choix](#choix-de-los).
-   Insérer une carte SD, cliquer sur “Choisir le stockage” et choisir la carte SD.
-   **Important :** Cliquer sur la roue dentée et s’assurer que l’option “Activer SSH” est activée.

    > Anciennement, l’activation de SSH se faisait en créant un fichier vide appelé `ssh`dans le répertoire `boot`, par exemple avec la commande `touch /Volumes/boot/ssh`.
    > Ce n’est plus nécessaire aujourd’hui.

-   Cliquer sur <kbd>ÉCRIRE</kbd>.
    Entrez votre mot de passe lorsque le dialogue le demande.
    L’écriture de l’image disque prend environ 10 min avec la vérification (si elle a été sélectionnée dans les préférences).
    Ces temps peuvent beaucoup varier en fonction de votre matériel.
-   Éjecter la carte SD.
-   Insérer la carte SD dans le Raspberry éteint.
-   Connecter le câble Ethernet.
-   Brancher le câble d’alimentation du Raspberry.
-   Après environ 30 secondes, ouvrir un terminal et se connecter au Raspberry avec la commande `ssh pi@raspberrypi.local`.
    Le mot de passe par défaut est `raspberry`.
    Si SSH renvoie l’erreur `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`,<br>
    c’est parce qu’une entrée existe déjà pour `raspberrypi.local` dans le fichier `~/.ssh/known_hosts` (ou sur Windows `%HOMEPATH%\.ssh\known_hosts`) de l’ordinateur hôte (pas le RPi).
    Donc pour aller plus loin, il faut supprimer les lignes qui commencent par `raspberrypi.local` dans le fichier `known_hosts`.

## Retrouver un appareil sur le réseau local

Si on doit retrouver un Raspberry sur le réseau, la première commande à essayer est<br>
`ping -c1 raspberrypi.local`.
Mais si on ne connait pas le nom du Raspberry, alors il faut balayer toutes les adresses possibles (_network scan_).
Il y a deux commandes utiles pour cela, `arp` et `nmap`.
Sur la commande `nmap` doit être installée via Homebrew.
Pour ceux qui préfèrent les GUI, il y a aussi [Zenmap](https://nmap.org/zenmap/).

```bash
arp -a
```

```bash
nmap -sP 192.168.1.0/24
```

## Mise à jour de Raspbian

```bash
sudo apt-get -y update       # Télécharge les informations des paquets à partir des sources configurées.
sudo apt-get -y upgrade      # Mets à jour les paquets installés sans en supprimer.
sudo apt-get -y dist-upgrade # Installe les versions candidates des paquets installés en installant ou en supprimant d’autres paquets si nécessaire.
sudo apt-get -y autoremove   # Supprime les dépendances qui ne sont plus utilisées.
```

À voir aussi :

-   <https://www.lecoindunet.com/difference-apt-update-upgrade-full-upgrade>
-   <https://askubuntu.com/a/527421/949794>

## Configuration

```bash
nano ~/.bash_profile
```

Copier-coller les commandes suivantes dans .bash_profile :

```bash
PS1=$'\n\n\xf0\x9f\x98\xBA'"  \t – \[\033[01;32m\]\u@\h\[\033[00m\]:\W > "
alias ll='ls -lGhF'
alias la='ll -a'
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

# If Byobu is installed, launch it at startup.
[[ -f /usr/bin/byobu-launch ]] && _byobu_sourced=1 . /usr/bin/byobu-launch 2>/dev/null || true

```

```bash
source ~/.bash_profile
```

```bash
sudo raspi-config
# Update
# Advanced Options / Expand filesystem
```

## SSH

**Sur l’ordinateur hôte**

```bash
# Si le fichier ~/.ssh/id_rsa.pub n’existe pas,
# il faut le créer avec `ssh-keygen`.
ssh-keygen # Accepter toutes les valeurs par défaut.
cat ~/.ssh/id_rsa.pub # + Copier le résultat dans le presse-papier.
```

**Sur le RPi**

```bash
mkdir -p ~/.ssh
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

## Sélection des interfaces utilisateurs

Par défaut, l’interface graphique est activée et elle consomme beaucoup de ressources.
Donc si on ne l’utilise pas, il est conseillé de la désactiver.
Malheureusement, lorsqu’elle est désactivée, les disques ne sont pas montés automatiquement lorsqu’on les connecte au RPi.

```bash
sudo raspi-config
# 1 System Options
# S5 Boot / Auto Login
# B2 Console Autologin ou B1 Console
```

## VNC

> N.B. Il faut que l’interface graphique soit activée pour que VNC fonctionne (voir § précédent).

```bash
sudo raspi-config
# 3 Interfacing Options / I3 VNC <Yes>.

# Si l’option n’est pas visible, il faut
# installer VNC au préalable avec la commande :
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
```

Télécharger un client VNC pour se connecter au serveur VNC du RPi.
Par exemple RealVNC :

-   <https://www.realvnc.com/en/connect/download/viewer/>.

> N.B. Le client VNC installé par défaut sur macOS ne fonctionne pas pour se connecter au serveur VNC du RPi.
> L’erreur retournée est<br>
> _Le logiciel de l’ordinateur distant semble ne pas être compatible avec cette version de Partage d’écran._<br>
> `bash /System/Library/CoreServices/Applications/Screen\ Sharing.app`

## Enlever les programmes inutiles

Enfin, inutiles pour moi...

```bash
df -h # Pour voir la capacité de la carte SD
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
df -h # Vous venez de libérer 1.1 Go !
```

## Réinstaller un programme qu’on croyait inutile

```bash
sudo apt-get --assume-yes update
sudo apt-get --assume-yes install wolfram-engine
```

## Ajouter quelques programmes utiles

### Byobu

Byobu (<https://www.byobu.org/>) est un gestionnaire de fenêtres et un multiplexeur de terminal en mode texte sous licence GPLv3.
Il a été conçu à l’origine pour apporter des améliorations élégantes au gestionnaire de fenêtres GNU Screen, par ailleurs fonctionnel, simple et pratique, pour la distribution serveur Ubuntu.
Byobu comprend maintenant des profils améliorés, des raccourcis clavier pratiques, des utilitaires de configuration et des notifications d’état du système commutables pour le gestionnaire de fenêtres GNU Screen et le multiplexeur de terminal plus moderne Tmux, et fonctionne sur la plupart des distributions Linux, BSD et Mac.
Le code source se trouve sur GitHub : <https://github.com/dustinkirkland/byobu>

Dans la terminologie de Byobu, une session est une instance de Byobu en cours d’exécution.
Une session se compose d’une collection de fenêtres (_windows_), qui sont essentiellement des sessions _shell_, et de volets (_panes_), qui sont des sous-sections de fenêtre.

```bash
sudo apt-get install byobu --assume-yes
byobu

# Configurer les options de base en pressant sur F1

# Configurer le raccourci de “l’escape sequence”.
# Conseil: utiliser la lettre “B”.
Change escape sequence
# Configurer le démarrage automatique de Byobu.
Byobu currently does not launch at login (toggle on)
```

<!--
#### .bash_profile

Pour charger `.bash_profile`, ajouter la commande suivante dans `~/.bashrc` :

```bash
_bash_profile_sourced=1 . ~/.bash_profile 2>/dev/null || true
```
-->

#### Raccourcis clavier

Les raccourcis clavier sont définis dans le fichier
`f-keys.tmux` ([source](https://github.com/dustinkirkland/byobu/blob/master/usr/share/byobu/keybindings/f-keys.tmux)).

```bash
/usr/share/byobu/keybindings/f-keys.tmux
```

Sur macOS, la majorité des raccourcis n’est utilisable qu’à travers la touche `F12`.
Donc quand l’aide indique la combinaison `C-a`, il faut la remplacer par `F12`.

Par exemple,

-   `F12 %` scinde le volet actuel en deux volets verticaux.
-   `F12 |` scinde le volet actuel en deux volets horizontaux.

La liste de toutes les fonctions `F12` est disponible avec la commande `F12 ?`.

Ci-dessous, la liste des raccourcis autres que `F12`.

<!--
| Label | Key     |
| ----- | ------- |
| C     | Control |
| S     | Shift   |
| M     | Meta    |
-->

| Key    | Action                                |
| ------ | ------------------------------------- |
| F1     | configuration menu                    |
| F2     | new window                            |
| F3     | previous window                       |
| F4     | next window                           |
| F5     | refresh menu bar status notifications |
| F6     | detach                                |
| F7     | —                                     |
| F8     | rename window                         |
| F9     | configuration menu                    |
| F10    | —                                     |
| F11    | —                                     |
| F12    | —                                     |
| ctrl-D | kill window                           |

#### À lire

-   <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-byobu-for-terminal-management-on-ubuntu-16-04>
-   <https://superuser.com/a/818753/508141>

### iPython

```bash
python3 -m pip install ipython
```

### Tmux

> N.B. Ce chapitre est ici pour référence.
> Je n’utilise plus Tmux directement, mais à travers [Byobu](#byobu).

```bash
sudo apt --assume-yes install tmux

tmux # crée et démarre un nouveau _shell_
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
# Il ne s’appliquera qu’aux nouveaux shells et pas
# aux shells existants, mais on peut le faire dans
# chaque shell individuel avec la commande
tmux set-option -g mouse on
# En mode mouse on, il n’est possible de sélectionner
# du texte. Il faut donc revenir en mode off.
tmux set-option -g mouse off
```


```bash
# https://ostechnix.com/install-tmux-plugin-manager/
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# tmux source ~/.tmux.conf

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'


``````


À voir aussi :

- <https://tmuxcheatsheet.com/>
- [Tmux has forever changed the way I write code.]
- [Tutorial Install And Use Tmux on MacOS]

[Tmux has forever changed the way I write code.]: https://youtu.be/DzNmUNvnB04
[Tutorial Install And Use Tmux on MacOS]: https://blog.eldernode.com/install-and-use-tmux-on-macos/


### GNU screen

> Je préfère ne pas utiliser GNU screen, mais parfois... on a pas le choix.

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

Vérifier la présence des informations suivantes :

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
sudo smbpasswd -a pi # Pour changer le mot de passe.
```

### Monter le disque partagé sur macOS

Dans le Finder :

```bash
⌘ K
smb://pi@raspberrypi.local
```

### Monter le disque partagé sur Windows

Voir

-   <https://support.microsoft.com/fr-fr/windows/mapper-un-lecteur-r%C3%A9seau-dans-windows-29ce55d1-34e3-a7e2-4801-131475f9557d>

On peut aussi entrer le chemin d’accès au Raspberry au [format UNC](<https://en.wikipedia.org/wiki/Path_(computing)#Universal_Naming_Convention>) directement dans la barre d’adresse de l’explorateur Windows (raccourcis Win+E, Ctrl+L).

```bash
\\raspberrypi.local
```

Si la résolution du nom d’hôte ne fonctionne pas, on peut aussi utiliser l’adresse IP :

```bash
\\192.168.1.240
```

### Installer une autre version de Python 3

> Les informations de ce chapitre sont passablement obsolètes car les dernières versions de l’OS du RPi intègrent des versions de Python supérieures à 3.6.
> Donc avant d’installer une nouvelle version de Python 3, il est prudent de vérifier la version installée sur le Raspberry avec la commande

```bash
python3 --version
```

> On peut aussi vérifier la version de l’OS avec la commande

```bash
cat /etc/os-release
```

> Édit du 16 octobre 2019 : Raspbian Buster intègre la version 3.7.3 de Python.
>
> Édit du 11 février 2023 : Raspberry Pi OS Bullseye 64 bit intègre la version 3.9.2 de Python.

Raspbian Stretch propose la version 3.5 de Python.
Comme Python 3.6 apporte de nouvelles fonctionnalités comme les _f-strings_ et que le module `asyncio` a été amélioré, je pense que c’est intéressant de l’installer aussi.
L’idée est aussi de pouvoir tester le module [quart][quart].

Source : <https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/>
Les versions de Python disponibles sont téléchargeables à : <https://www.python.org/ftp/python/>
Temps d’installation : environ 30 min.
Cette procédure n’écrase pas les versions de Python existantes.

Cette procédure montre comment installer Python 3.6.7.

> J’ai aussi essayé d’installer la version 3.7.1 et l’installation a réussi, mais malheureusement `pip` ne fonctionnait pas, donc il m’était impossible d’installer de nouveaux modules.

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
Il faut redémarrer le RPi pour que le changement soit pris en compte.

```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
sudo usermod -a -G input $USER
sudo reboot
```

### torsocks

Torsocks permet d’utiliser le réseau Tor en ligne de commande, autrement dit, il permet de “torifier” la ligne de commande.

```bash
sudo apt-get install torsocks --assume-yes
ANS=$(torsocks wget -qO- https://check.torproject.org/api/ip)
echo $ANS
# {"IsTor":true,"IP":"××.××.××.××"}
```

## YouTube-DL

```bash
python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
```

## Arrêter ou redémarrer un Raspberry

Ce n’est pas une bonne idée de juste tirer la prise quand on veut arrêter ou redémarrer son Raspberry.
En effet, au bout de quelque temps, le système se retrouve avec un grand nombre de fichiers partiels et probablement illisibles.
Si des fichiers importants sont touchés, le Raspberry peut devenir inutilisable.

Donc pour éteindre un Raspberry, on utilisera une des commandes ci-dessous.
La différence entre elles n’est pas aussi évidente qu’il y parait (voir <https://unix.stackexchange.com/a/196471/199660>).
Seule la commande `halt` éteint la LED rouge d’alimentation, donc je suppose que c’est celle qu’il faut privilégier.

> N.B. Attention, aucune de ces commandes ne coupe l’alimentation de la carte ou l’alimentation des ports USB.
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
Ce chemin est aussi appelé _point de montage_.
On peut le voir avec la commande `ls` et accéder aux répertoires avec la commande `cd`.
Dans l’exemple ci-dessous, le disque externe s’appelle `LaCie`.
Ce nom changera avec d’autres fabricants ou si plusieurs disques du même fabricant sont utilisés en même temps.
Il faut tenir compte de ce fait lorsqu’on écrit des scripts et des programmes qui utilisent le chemin du point de montage.

```bash
ls -l /media/pi/
cd /media/pi/LaCie
```

## Éjecter un disque externe

> N.B. À proprement parler, seuls les médias comme les CD ou les bandes peuvent être éjectés.
> Mais le terme est aussi utilisé pour les autres médias.

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

> N.B. Il faut s’assurer que le disque n’est plus utilisé, sinon le système refusera de le démonter avec l’erreur `target is busy`.
> C’est à ça que sert le changement de répertoire ci-dessous.

```bash
cd
udisksctl unmount --block-device /dev/sda2
sudo udisksctl power-off --block-device /dev/sda
```

<!--
### Monter un disque externe

Si le Raspberry est configuré pour démarrer en mode _Desktop Autologin_ (`sudo raspi-config # options 1 + S5 + B4`), les disques externes sont automatiquement montés par le système et il n’y a donc pas besoin de s’en occuper.
Ceci est valable même si on ne se con
Par contre s’il est configuré pour démarrer en mode _Text console_ (`sudo raspi-config # options 1 + S5 + B1 ou B2`), les points de montages sont créés

https://raspberrypi.stackexchange.com/questions/141161/automatically-mount-usb-storage-on-raspberry-os-bullseye-lite-as-desktop-versio

Voici quelques explications sur ces informations.

- Les disques durs standards sont nommés avec le préfixe `sd`suivi d’une lettre attribuée dans l’ordre alphabétique.
  Donc le premier disque aura le nom `sda`, le deuxième `sdb`, etc.
  L’acronyme `sd`signifie *SCSI mass-storage driver*.
  Ici, c’est le pilote qui est SCSI, même si le disque n’est pas SCSI.
- Les stockages NVMe (Non-Volatile Memory Express) sont nommés avec le préfixe `nvm`.
- Les stockages MMC (Multi Media Card) sont nommés avec le préfixe `nvm`.
 -->

### Pour aller plus loin

-   [What you need to know about disks and disk partitions in Linux](https://linuxbsdos.com/2021/11/27/what-you-need-to-know-about-disks-and-disk-partitions-in-linux/).
-   [What is NVMe SSD technology?](https://www.kingston.com/en/ssd/what-is-nvme-ssd-technology)
-   [What Is an MMC Card - Full Guide](https://recoverit.wondershare.com/memorycard-recovery/what-is-mmc-card.html)

## À voir aussi

-   <https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/>
-   <https://learnxinyminutes.com/docs/bash/>
-   <https://devhints.io/bash>
-   <https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html>

<!-- Liens transmis par Johannes -->

-   <https://funprojects.blog/2021/04/26/control-usb-powered-devices/>
-   <https://raspberrypi.stackexchange.com/questions/118656/raspberry-pi4-uhubctl-bash-script-wont-run>
-   <https://github.com/codazoda/hub-ctrl.c/issues/17>

## Quelques commandes utiles

-   Déterminer le modèle de Raspberry

```bash
cat /sys/firmware/devicetree/base/model
# Raspberry Pi 4 Model B Rev 1.1
```

-   Déterminer la version de l’OS

```bash
cat /etc/os_release
```
