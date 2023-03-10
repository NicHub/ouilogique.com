---
layout: page
title: "Trucs et astuces en Bash"
categories:
excerpt:
tags: []
image:
    feature:
date: 2023-02-17T12:00:00+01:00
published: false
author: Nico
---


# Quelques termes

- terminal
- shell
- ligne de commande
- console


En informatique, quelle est la différence entre une console, un shell, un terminal ?

Les termes "console", "shell" et "terminal" sont souvent utilisés de manière interchangeable, mais il existe en réalité des différences subtiles entre ces concepts en informatique.

    Une console fait référence à une interface utilisateur textuelle qui permet d'accéder à un système informatique, généralement sans interface graphique. Elle peut être située sur un ordinateur local ou être utilisée pour se connecter à distance à un système distant.

    Un shell (ou "interpréteur de commandes") est un programme qui fournit une interface en ligne de commande (CLI) à l'utilisateur pour interagir avec le système d'exploitation. Le shell peut être exécuté à l'intérieur d'une console ou d'un terminal, et il permet d'exécuter des commandes en tapant des instructions textuelles.

    Un terminal est un programme qui fournit une interface graphique à une console, permettant ainsi à l'utilisateur de visualiser et d'interagir avec le système d'exploitation de manière plus conviviale. Le terminal peut également exécuter un shell pour permettre à l'utilisateur d'exécuter des commandes en ligne de commande.

En résumé, une console est une interface utilisateur textuelle brute, un shell est un programme qui permet d'exécuter des commandes en ligne de commande, et un terminal est un programme qui fournit une interface graphique à une console pour permettre une interaction plus conviviale avec le système d'exploitation.


# Utilité de tmux







crontab led
@reboot /usr/bin/python3 /home/pi/Desktop/led_chase_1.py



https://linuxize.com/post/bash-check-if-file-exists/


[ -r /home/pi/.bash_profile ] && . /home/pi/.bash_profile
[ -r /home/pi/.byobu/prompt ] && . /home/pi/.byobu/prompt   #byobu-prompt#





# update

La commande Bash sudo apt-get update sert à mettre à jour la liste des paquets disponibles sur un système Ubuntu ou Debian.

Plus précisément, cette commande va se connecter aux serveurs de packages du système d'exploitation et télécharger les informations les plus récentes sur les paquets disponibles, leurs dépendances et les mises à jour disponibles.

Cela permet de maintenir le système à jour et de s'assurer que les dernières versions des logiciels et des correctifs de sécurité sont disponibles pour l'installation.

Il est important de noter que cette commande ne met pas à jour les paquets eux-mêmes, mais seulement la liste des paquets disponibles. Pour installer les mises à jour disponibles, il faut utiliser la commande sudo apt-get upgrade.


# upgrade

La commande Bash sudo apt-get upgrade sert à mettre à jour les paquets installés sur un système Ubuntu ou Debian.

Plus précisément, cette commande va télécharger et installer les mises à jour disponibles pour les paquets installés sur le système. Cela permet de maintenir le système à jour en installant les dernières versions des logiciels et des correctifs de sécurité.

Il est important de noter que la commande sudo apt-get upgrade ne va pas installer de nouveaux paquets, elle se contente de mettre à jour les paquets existants. Si vous souhaitez installer de nouveaux paquets, vous pouvez utiliser la commande sudo apt-get install suivie du nom du paquet que vous souhaitez installer.

Il est recommandé de régulièrement exécuter la commande sudo apt-get update suivi de la commande sudo apt-get upgrade pour s'assurer que votre système est à jour et sécurisé.

# dist-upgrade

La commande Bash sudo apt-get dist-upgrade sert à effectuer une mise à niveau complète du système d'exploitation Ubuntu ou Debian.

Plus précisément, cette commande va mettre à jour tous les paquets installés sur le système, y compris ceux qui nécessitent des modifications importantes de dépendances ou qui nécessitent la suppression ou l'ajout de nouveaux paquets.

La commande sudo apt-get dist-upgrade peut être utilisée pour effectuer une mise à niveau majeure du système, par exemple lorsqu'une nouvelle version majeure d'Ubuntu ou Debian est disponible.

Il est important de noter que la commande sudo apt-get dist-upgrade est plus puissante que la commande sudo apt-get upgrade et peut entraîner la suppression ou l'ajout de paquets. Il est donc recommandé de bien vérifier les changements proposés avant de procéder à la mise à niveau.

En général, il est recommandé de faire une sauvegarde complète du système avant de procéder à une mise à niveau majeure.

# apt-get vs apt

Les commandes apt-get et apt sont toutes deux des outils de gestion de paquets pour les systèmes Ubuntu et Debian.

La principale différence entre ces deux commandes est que apt est une version simplifiée et plus conviviale de apt-get avec des options plus intuitives et des messages d'erreur plus clairs.

La commande apt offre une expérience utilisateur plus conviviale et plus facile à utiliser, en affichant des informations plus précises et en fournissant une sortie plus conviviale que apt-get.

Cependant, apt-get est toujours largement utilisé et peut être plus flexible dans certains cas d'utilisation, car il offre un contrôle plus fin sur les options et les paramètres.

En général, les deux commandes sont largement interchangeables et peuvent être utilisées selon les préférences personnelles de l'utilisateur.


# Les flux standard de Linux

Source : https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/

Sous Linux, les flux - comme presque tout le reste - sont traités comme des fichiers. Vous pouvez lire du texte à partir d'un fichier et vous pouvez écrire du texte dans un fichier. Ces deux actions impliquent un flux de données. Le concept de traitement d'un flux de données comme un fichier n'est donc pas si compliqué que cela.

Il y a trois flux standard :
- stdin (standard in) est le flux d'entrée standard. Il accepte du texte en entrée.
- stdout (standard out) est le flux de sortie standard.
- stderr (standard error) permet de renvoyer des éventuelles erreurs.

Sous Linux, les flux - comme presque tout le reste - sont traités comme des fichiers. Vous pouvez lire du texte à partir d'un fichier et vous pouvez écrire du texte dans un fichier. Ces deux actions impliquent un flux de données. Le concept de traitement d'un flux de données comme un fichier n'est donc pas si compliqué que cela.

Chaque fichier associé à un processus se voit attribuer un numéro unique pour l'identifier. C'est ce qu'on appelle le descripteur de fichier. Chaque fois qu'une action doit être effectuée sur un fichier, le descripteur de fichier est utilisé pour identifier le fichier.

Ces valeurs sont toujours utilisées pour stdin, stdout et stderr :

    0: stdin
    1: stdout
    2: stderr



# Commandes utiles

grep # tout seul ou en pipe
find
ls
rclone
ps
which
man
kill
git
md5
zip
chmod
alias
sudo
nano
byobu
cd
ping
wget
curl
apt-get
arp -a
echo
printf
