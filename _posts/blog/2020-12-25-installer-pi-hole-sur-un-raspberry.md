---
author: Nico
date: 2020-12-25 13:19:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Installer Pi-hole sur un Raspberry
---

## Source

La version originale de ce document a été écrite par Johannes du [Microclub](https://microclub.ch). Il m’a aimablement autorisé à la retranscrire à ma sauce dans cet article.

## Introduction

Pi-hole est un système de blocage d’accès aux contenus Internet adventices, c’est-à-dire non sollicités directement par l’utilisateur et qu’il préfèrerait ne pas télécharger s’il en avait le choix et la possibilité.

Cet article explique comment installer et configurer Pi-hole sur un Raspberry avec Raspberry Pi OS Buster. À noter que Pi-hole peut aussi être déployé sur d’autres OS ainsi que dans une image Docker.

_Note :_ Si vous voulez juste tester le système avec un Pi-hole existant, vous pouvez utiliser celui de Digitec à l’adresse IP `40.114.239.83`.
Ils ont aussi écrit un article sur leur solution : [Article Pi-hole Digitec](https://www.digitec.ch/fr/page/le-pi-hole-de-digitec-ou-comment-en-finir-avec-les-publicites-18923).
Bien évidemment, il faut être à l’aise avec le fait que Digitec aura connaissance de toutes les URL que votre ordinateur interroge.

## Ressources

-   [Site officiel de Pi-hole](https://pi-hole.net)
-   [Documentation de Pi-hole](https://docs.pi-hole.net)
-   [Liste des modèles de Raspberry compatibles](https://docs.pi-hole.net/ftldns/compatibility/)
-   [Liste des OS compatibles](https://docs.pi-hole.net/main/prerequisites/#supported-operating-systems)

## Installation de Pi-hole sur le Raspberry

-   Flasher Raspberry Pi OS sur une carte SD. ([Voir la procédure détaillée.](../installer-raspian-stretch/))
-   Connecter le Raspberry au réseau.
-   Ouvrir un terminal sur le Raspberry et installer Pi-hole avec la commande suivante :

```bash
curl -sSL https://install.pi-hole.net | bash
```

-   Accepter les options par défaut de l’installateur.
-   À la fin de l’installation, relever l’adresse IP locale du Rasperry affichée par l’installateur. On peut aussi l’obtenir avec la commande :

```bash
hostname -I
```

-   Relever également le mot de passe de l’interface d’administration de Pi-hole.
-   Redémarrer le Raspberry avec la commande

```bash
sudo reboot
```

## Configuration du routeur

> Les explications sont basées sur un modèle de routeur “Sunrise Internet Box”. Les liens proposés ci-dessous fonctionneront donc uniquement sur ce modèle de routeur, mais les principes restent les mêmes pour tous les autres routeurs.
>
> <span style="color:red">L’adresse IP locale de mon RPi est 192.168.1.28. Dans les explications si dessous, il faut remplacer cette IP par celle de votre RPi.</span>

-   Se connecter à l’interface d’administration du routeur
    <http://192.168.1.1/>.
-   Activer le mode expert en cliquant sur le bouton en haut à droite.

**Définir le Raspberry comme serveur DNS local**

-   Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `DNS`
    <http://192.168.1.1/0.2/gui/#/mybox/dns/server>.
-   Les valeurs par défaut du routeur sont :
    -   `Activer : ON`
    -   `Serveur DNS Primaire : 192.168.1.1`
    -   `Serveur DNS Secondaire : (vide)`
-   Il faut modifier ces valeurs de la façon suivante :
    -   `Activer : ON`
    -   `Serveur DNS Primaire : 192.168.1.28`
    -   `Serveur DNS Secondaire : 192.168.1.28`

**Redirection des requêtes sortant sur le port 53 vers le port 53 du Raspberry**

-   Sur la page d’accueil du routeur, cliquer sur `Contrôle d’Accès`, puis sur l’onglet `Redirection de ports`
    <http://192.168.1.1/0.2/gui/#/access-control/port-forwarding/add-rule>.
-   Dans la section `Ajouter des règles manuellement` :
    -   Cliquer sur la liste déroulante `Services` et sélectionner `DNS`.
    -   `Hôte Interne : 192.168.1.28`
    -   Laisser les autres valeurs par défaut.
    -   Cliquer sur ajouter.

**Désactiver le mode DHCP**

-   Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `DHCP`
    <http://192.168.1.1/0.2/gui/#/mybox/DHCP>.
-   Dans la section `DHCP`, cliquer sur le bouton `Activer` pour le mettre sur `OFF`.

**Redémarrer le routeur**

-   Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `Maintenance`
    <http://192.168.1.1/0.2/gui/#/mybox/maintenance/reset>.
-   Cliquer sur `Redémarrer`.

## Configuration de Pi-hole

**Activer le DHCP**

-   Accéder à la page d’accueil de Pi-hole en naviguant à l’adresse
    <http://192.168.1.28/admin/>.
-   Dans le menu de gauche, cliquer sur `Settings`, puis sur l’onglet `DHCP`
    <http://192.168.1.28/admin/settings.php?tab=piholedhcp>.
-   Activer le DHCP en cliquant sur `DHCP server enabled`.

**Ajout des listes de blocages (Adlists)**

-   Dans le menu de gauche, cliquer sur `Group Management`, puis sur `Adlists`
    <http://192.168.1.28/admin/groups-adlists.php>.
-   Copier les [URL des listes de blocage (Adlists)](../../files/2020-12-25-installer-pi-hole-sur-un-raspberry/pi-hole-adlists.txt).
-   Coller ces URL dans le champ `Address`. Les retours à la ligne sont acceptés comme séparateur d’URL.
-   Cliquer sur le bouton `Add`.

**Mettre à jour la base de données**

-   Dans le menu de gauche, cliquer sur `Tools`, puis sur `Update Gravity`
    <http://192.168.1.28/admin/gravity.php>.
-   Cliquer sur le bouton `Update`.

**Ajout des faux positifs (Whitelist)**

-   Dans le menu de gauche, cliquer sur `Whitelist`
    <http://192.168.1.28/admin/groups-domains.php?type=white>.
-   Copier les [URL des faux positifs (Whitelist)](../../files/2020-12-25-installer-pi-hole-sur-un-raspberry/pi-hole-whitelist.txt).
-   Coller ces URL dans le champ `Domain`. Les retours à la ligne sont acceptés comme séparateur d’URL.
-   Activer l’option `Add domain as wildcard`.
-   Cliquer sur le bouton `Add to Whitelist`.

**Ajout des vrais positifs (Blacklist)**

-   Dans le menu de gauche, cliquer sur `Blacklist`
    <http://192.168.1.28/admin/groups-domains.php?type=black>
-   Ajouter des URL à votre convenance.

Voilà, Pi-hole est installé et fonctionnel. Nous allons voir maintenant comment récupérer quelques informations.

---

## Récupération des URL indiquées dans les Adlists

Les Adlists sont stockées dans des fichiers textes qu’il est possible de télécharger sur un autre ordinateur. Ces fichiers ont une extension `.domains` et contiennent beaucoup d’URL redondantes, il est donc utile de les filtrer. Voici les commandes bash qui permettent de récupérer ces URL. À noter qu’il est préférable de les exécuter l’une après l’autre.

```bash
# Télécharge les fichiers *.domains.
scp 'pi@192.168.1.28:/etc/pihole/*.domains' .

# Concatène tous les fichiers,
# classe les URL par ordre alphabétique
# et supprime les doublons.
cat *.domains | sort | uniq -u > pihole_adlist_urls_sorted_unique.txt

# Compte les URL.
N1=$(cat *.domains | wc -l)
N2=$(cat pihole_adlist_urls_sorted_unique.txt | wc -l)
P1=$(python -c "p = $N2 / $N1 * 100; print(p)")
printf "Nombre d’URL total        : %10d\n" $N1
printf "Nombre d’URL uniques      : %10d\n" $N2
printf "Pourcentage d’URL uniques : %8.1f %%\n" $P1

# Cleanup.
rm *.domains
```

Avec ma configuration, les résultats retournés sont :

```bash
Nombre d’URL total        :    5281881
Nombre d’URL uniques      :    1605385
Pourcentage d’URL uniques :     30,4 %
```

## Faire des requêtes directement dans la base de données de Pi-hole

Pi-hole enregistre les informations dans des bases de données SQLite3 :

-   `/etc/pihole/gravity.db`.
-   `/etc/pihole/macvendor.db`.
-   `/etc/pihole/pihole-FTL.db`.

Il est possible de faire des requêtes sur ces bases de données directement depuis Bash. Par exemple, la commande suivante renvoie les 3 domaines les plus demandés depuis l’installation de Pi-hole :

```bash
sqlite3 "/etc/pihole/pihole-FTL.db" "SELECT domain,count(domain) FROM queries WHERE (STATUS == 2 OR STATUS == 3) GROUP BY domain ORDER BY count(domain) DESC LIMIT 3;"
```

On peut aussi entrer les commandes dans un shell SQLite3 :

```bash
sqlite3 /etc/pihole/pihole-FTL.db
SELECT domain,count(domain) FROM queries WHERE (STATUS == 2 OR STATUS == 3) GROUP BY domain ORDER BY count(domain) DESC LIMIT 3;
```

Ou enregistrer les commandes SQL dans un fichier :

```bash
# Créer un fichier de commandes SQL :
echo "SELECT domain,count(domain) FROM queries WHERE (STATUS == 2 OR STATUS == 3) GROUP BY domain ORDER BY count(domain) DESC LIMIT 3;" > ~/get_queried_most.sql

# L’exécuter depuis Bash :
cat ~/get_queried_most.sql | sqlite3 "/etc/pihole/pihole-FTL.db"

# Ou l’exécuter depuis le shell SQLite3 :
sqlite3 "/etc/pihole/pihole-FTL.db"
.read /home/pi/get_queried_most.sql
```

Pour afficher les noms des tables d’une base de données :

```bash
sqlite3 "/etc/pihole/gravity.db" ".schema"
```

Pour afficher les noms des champs d’une table :

```bash
sqlite3 "/etc/pihole/gravity.db" ".schema domainlist"
```

Pour compter le nombre d’entrées d’une table :

```bash
sqlite3 "/etc/pihole/gravity.db" "SELECT COUNT(*) FROM gravity" # Le résultat est 5251857 pour mon Pi-hole
```

Pour limiter le nombre de résultats affichés :

```bash
sqlite3 "/etc/pihole/gravity.db" "SELECT * FROM gravity LIMIT 3"
```

Pour afficher les URL des Adlists :

```bash
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist"
```

Pour afficher les URL de la whitelist :

```bash
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM vw_regex_whitelist;"
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM vw_whitelist;"
```

Pour afficher les URL de la blacklist :

```bash
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM vw_regex_blacklist;"
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM vw_blacklist;"
```
