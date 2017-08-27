---
layout: page
title: "Installer GPHOTO2"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2017-08-27T01:00:00+02:00
published: true
author: Nico
redirect_from:
  - http://ouilogique.com/gphoto2/
---

<!--
Ancienne URL
http://ouilogique.com/gphoto2/
-->

La bibliothèque GPHOTO2 est utilisée par des applications pour accéder à une grande variété de modèles d’appareils photo numériques, à l’aide des protocoles standards comme l’USB Mass Storage et PTP, ou à l’aide des protocoles propres aux fabricants.

Dans cet article, je présente l’installation de GPHOTO2 sous MaxOS Sierra et sous Raspbian Stretch.


# Installation de GPHOTO2 sur *MacOS Sierra*

L’installation de GPHOTO2 sur *MacOS Sierra* se fait avec [Homebrew](https://brew.sh/index_fr.html)

{% highlight bash %}
brew update
brew install gphoto2
# Ou pour mettre à jour
brew upgrade gphoto2
gphoto2 -v

# gphoto2 2.5.14
#
# Copyright (c) 2000-2016 Lutz Mueller and others
#
# gphoto2 comes with NO WARRANTY, to the extent permitted by law. You may
# redistribute copies of gphoto2 under the terms of the GNU General Public
# License. For more information about these matters, see the files named COPYING.
#
# This version of gphoto2 is using the following software versions and options:
# gphoto2         2.5.14         clang, popt(m), no exif, no cdk, no aa, jpeg, readline
# libgphoto2      2.5.14         all camlibs, clang, ltdl, no EXIF
# libgphoto2_port 0.12.0         clang, ltdl, USB, serial without locking
{% endhighlight %}


# Installation de GPHOTO2 sur *Raspbian Stretch*

> GPHOTO2 n’est disponible qu’à la version 2.5.4 sur *Raspbian Jessie* avec la commande `sudo apt-get install gphoto2`. Il est donc préférable d’utiliser [*Raspbian Stretch*][1]. Sur *Raspbian Stretch*, la version par défaut est la 2.5.11, mais il est possible d’installer manuellement la version 2.5.14.

{% highlight bash %}
sudo apt-get --assume-yes install gphoto2
gphoto2 -v

# gphoto2 2.5.11
#
# Copyright (c) 2000-2016 Lutz Mueller and others
#
# gphoto2 comes with NO WARRANTY, to the extent permitted by law. You may
# redistribute copies of gphoto2 under the terms of the GNU General Public
# License. For more information about these matters, see the files named COPYING.
#
# This version of gphoto2 is using the following software versions and options:
# gphoto2         2.5.11         gcc, popt(m), exif, cdk, aa, jpeg, readline
# libgphoto2      2.5.12         all camlibs, gcc, ltdl, EXIF
# libgphoto2_port 0.12.0         gcc, ltdl, USB, serial without locking
{% endhighlight %}

> GPHOTO2 entre en conflit avec *gvfs-gphoto2-volume-monitor* et il est donc nécessaire de le désactiver avec les commandes suivantes :

{% highlight bash %}
sudo chmod -x /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
sudo reboot
ssh pi@raspberrypi.local
{% endhighlight %}

> Pour installer la version 2.5.14

{% highlight bash %}
wget http://archive.raspbian.org/raspbian/pool/main/g/gphoto2/gphoto2_2.5.14-1_armhf.deb
wget http://archive.raspbian.org/raspbian/pool/main/libg/libgphoto2/libgphoto2-6_2.5.14-1_armhf.deb
sudo dpkg -i gphoto2_2.5.14-1_armhf.deb libgphoto2-6_2.5.14-1_armhf.deb
rm gphoto2_2.5.14-1_armhf.deb libgphoto2-6_2.5.14-1_armhf.deb
gphoto2 -v

# gphoto2 2.5.14
#
# Copyright (c) 2000-2016 Lutz Mueller and others
#
# gphoto2 comes with NO WARRANTY, to the extent permitted by law. You may
# redistribute copies of gphoto2 under the terms of the GNU General Public
# License. For more information about these matters, see the files named COPYING.
#
# This version of gphoto2 is using the following software versions and options:
# gphoto2         2.5.14         gcc, popt(m), exif, cdk, aa, jpeg, readline
# libgphoto2      2.5.14         all camlibs, gcc, ltdl, EXIF
# libgphoto2_port 0.12.0         gcc, ltdl, USB, serial without locking
{% endhighlight %}


# Quelques commandes utiles

{% highlight bash %}
# Connecter un appareil de photo sur un port USB du Raspberry.
# J’ai testé avec un Nikon D3200 et ça fonctionne
gphoto2 --auto-detect
gphoto2 --abilities
gphoto2 --summary
gphoto2 --list-ports
mkdir gphoto2
cd gphoto2/
gphoto2 --capture-image-and-download --interval 2 --frames 2 --filename=image_%Y-%m-%d_%H-%M-%S.jpg
{% endhighlight %}


# Pour visionner les photos

Un moyen simple de visionner les photos est de créer un mini serveur web sur le Raspberry. Pour démarrer ce serveur, il suffit d’utiliser les commandes suivantes, puis de copier-coller l’URL (par exemple http://192.168.1.135:4000) dans un navigateur.

{% highlight bash %}
# Ces deux commandes peuvent être copié-collées directement dans le terminal ou mises dans le fichier ~/.bash_profile.
# Voir http://ouilogique.com/installer-raspian-stretch/#configuration.
IP=$(hostname -I | awk '{print $1}')
alias pyserver='PORT=4000; echo -e "\nhttp://localhost:$PORT"; echo -e "http://$IP:$PORT\n"; python -m SimpleHTTPServer $PORT'
# Démarre le serveur (ctrl-C pour l’arrêter)
pyserver
{% endhighlight %}

Comme le serveur bloque la ligne de commande, il est préférable de l’utiliser dans un autre shell avec l’utilitaire [`gnu screen`][2].


# Quelques liens

- <http://gphoto.org/>
- <http://lists.alioth.debian.org/pipermail/pkg-phototools-devel/2017-June/010392.html>
- <https://github.com/gphoto/gphoto2>
- <https://github.com/gphoto/gphoto2/issues/72>
- <https://www.raspberrypi.org/forums/viewtopic.php?t=186405>
- <http://archive.raspbian.org/raspbian/pool/main/g/gphoto2/>
- <https://github.com/NicHub/ouilogique.com/commit/d4f594d08b8c9a30e6577072fafda794f4ec93bc>
- <https://packages.debian.org/stretch/gphoto2>

[1]: http://ouilogique.com/installer-raspian-stretch/
[2]: http://ouilogique.com/installer-raspian-stretch/#gnu-screen
