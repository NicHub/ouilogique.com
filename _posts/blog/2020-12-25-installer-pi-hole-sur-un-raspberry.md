---
layout: page
title: "Installer Pi-hole sur un Raspberry"
modified:
categories:
excerpt:
tags: []
image:
     feature:
date: 2020-12-25T13:19:00+01:00
published: true
author: Nico
---

## Introduction

Cette page explique comment installer et configurer Pi-hole sur un Raspberry.

## Ressources

- [Site officiel de Pi-hole](https://pi-hole.net)
- [Documentation de Pi-hole](https://docs.pi-hole.net)
- [Liste des modèles de Raspberry supportés](https://docs.pi-hole.net/ftldns/compatibility/)
- [Télécharger Raspberry Pi OS](https://www.raspberrypi.org/software/)

## Installation de Pi-hole sur le Raspberry

- Flasher Raspberry Pi OS sur une carte SD. ([Voir la procédure détaillée.](./installer-raspian-stretch/))
- Connecter le Raspberry au réseau.
- Ouvrir un terminal sur le Raspberry et installer Pi-hole avec la commande suivante :
```bash
curl -sSL https://install.pi-hole.net | bash
```
- Accepter les options par défaut de l’installateur.
- À la fin de l’installation, relever l’adresse IP locale du Rasperry affichée par l’installateur. On peut aussi l’obtenir avec la commande :
```bash
hostname -I
```
- Relever également le mot de passe de l’interface d’administration de Pi-hole.
- Redémarrer le Raspberry avec la commande
```bash
sudo reboot
```

## Configuration du routeur

> Les explications sont basées sur un modèle de routeur “Sunrise Internet Box”. Les liens proposés ci-dessous fonctionneront donc uniquement sur ce modèle de routeur, mais les principes restent les mêmes pour tous les autres routeurs.
>
> <span style="color:red">L’adresse IP locale de mon RPi est 192.168.1.28. Dans les explications si dessous, il faut remplacer cet IP par celui de votre RPi.</span>

- Se connecter à l’interface d’administration du routeur
  <http://192.168.1.1/>.
- Activer le mode expert en cliquant sur le bouton en haut à droite.

**Définir le Raspberry comme serveur DNS local**

- Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `DNS`
  <http://192.168.1.1/0.2/gui/#/mybox/dns/server>.
- Les valeurs par défaut du routeur sont :
  - `Activer : ON`
  - `Serveur DNS Primaire : 192.168.1.1`
  - `Serveur DNS Secondaire : (vide)`
- Il faut modifier ces valeurs de la façon suivante :
  - `Activer : ON`
  - `Serveur DNS Primaire : 192.168.1.28`
  - `Serveur DNS Secondaire : 192.168.1.28`

**Redirection des requêtes sortant sur le port 53 vers le port 53 du Raspberry**

- Sur la page d’accueil du routeur, cliquer sur `Contrôle d’Accès`, puis sur l’onglet `Redirection de ports`
  <http://192.168.1.1/0.2/gui/#/access-control/port-forwarding/add-rule>.
- Dans la section `Ajouter des règles manuellement` :
  - Cliquer sur la liste déroulante `Services` et sélectionner `DNS`.
  - `Hôte Interne : 192.168.1.28`
  - Laisser les autres valeurs par défaut.
  - Cliquer sur ajouter.

**Désactiver le mode DHCP**

- Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `DHCP`
  <http://192.168.1.1/0.2/gui/#/mybox/DHCP>.
- Dans la section `DHCP`, cliquer sur le bouton `Activer` pour le mettre sur `OFF`.

**Redémarrer le routeur**

- Sur la page d’accueil du routeur, cliquer sur le bouton `Ma Sunrise Internet Box` en haut à gauche, puis sur l’onglet `Maintenance`
  <http://192.168.1.1/0.2/gui/#/mybox/maintenance/reset>.
- Cliquer sur `Redémarrer`.

## Configuration de Pi-hole

**Activer le DHCP**

- Accéder à la page d’accueil de Pi-hole en naviguant à l’adresse
  <http://192.168.1.28/admin/>.
- Dans le menu de gauche, cliquer sur `Settings`, puis sur l’onglet `DHCP`
  <http://192.168.1.28/admin/settings.php?tab=piholedhcp>.
- Activer le DHCP en cliquant sur `DHCP server enabled`.

**Ajout des listes de blocages (Adlists)**

- Dans le menu de gauche, cliquer sur `Group Management`, puis sur `Adlists`
  <http://192.168.1.28/admin/groups-adlists.php>.
- Copier les URL des listes de blocage plus bas sur cette page
  [./#url-des-listes-de-blocage-adlists](./#url-des-listes-de-blocage-adlists).
- Coller ces URL dans le champ `Address`. Les retours à la ligne sont acceptés comme séparateur d’URL.
- Cliquer sur le bouton `Add`.

**Mettre à jour la base de données**

- Dans le menu de gauche, cliquer sur `Tools`, puis sur `Update Gravity`
  <http://192.168.1.28/admin/gravity.php>.
- Cliquer sur le bouton `Update`.

**Ajout des faux positifs (Whitelist)**

- Dans le menu de gauche, cliquer sur `Whitelist`
  <http://192.168.1.28/admin/groups-domains.php?type=white>.
- Copier les URL de la liste des faux positifs plus bas sur cette page
  [./#faux-positifs-whitelist](./#faux-positifs-whitelist).
- Coller ces URL dans le champ `Domain`. Les retours à la ligne sont acceptés comme séparateur d’URL.
- Activer l’option `Add domain as wildcard`.
- Cliquer sur le bouton `Add to Whitelist`.

**Ajout des vrais positifs (Blacklist)**

- Dans le menu de gauche, cliquer sur `Blacklist`
  <http://192.168.1.28/admin/groups-domains.php?type=black>
- Ajouter des URL à votre convenance.

## URL des listes de blocage (Adlists)

http://phishing.mailscanner.info/phishing.bad.sites.conf
http://sysctl.org/cameleon/hosts
https://adaway.org/hosts.txt
https://adblock.mahakala.is
https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt
https://blocklistproject.github.io/Lists/abuse.txt
https://blocklistproject.github.io/Lists/fraud.txt
https://blocklistproject.github.io/Lists/malware.txt
https://blocklistproject.github.io/Lists/phishing.txt
https://blocklistproject.github.io/Lists/piracy.txt
https://blocklistproject.github.io/Lists/ransomware.txt
https://blocklistproject.github.io/Lists/scam.txt
https://blocklistproject.github.io/Lists/tracking.txt
https://blocklistproject.github.io/Lists/youtube.txt
https://dbl.oisd.nl/
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt
https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt
https://hosts.nfz.moe/basic/hosts
https://mirror.cedia.org.ec/malwaredomains/immortal_domains.txt
https://mirror1.malwaredomains.com/files/justdomains
https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt
https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext
https://phishing.army/download/phishing_army_blocklist_extended.txt
https://raw.github.com/notracking/hosts-blocklists/master/hostnames.txt
https://raw.githubusercontent.com/Akamaru/Pi-Hole-Lists/master/cryptomine.txt
https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt
https://raw.githubusercontent.com/anudeepND/youtubeadsblacklist/master/domainlist.txt
https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts
https://raw.githubusercontent.com/CHEF-KOCH/Audio-fingerprint-pages/master/AudioFp.txt
https://raw.githubusercontent.com/CHEF-KOCH/Canvas-fingerprinting-pages/master/Canvas.txt
https://raw.githubusercontent.com/CHEF-KOCH/WebRTC-tracking/master/WebRTC.txt
https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malvertising/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malware/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomainlist.com/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-justdomains/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/ransomwaretracker.abuse.ch/list.txt
https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts
https://raw.githubusercontent.com/kboghdady/youTube_ads_4_pi-hole/master/crowed_list.txt
https://raw.githubusercontent.com/kboghdady/youTube_ads_4_pi-hole/master/youtubelist.txt
https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt
https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/hosts
https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt
https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts_without_controversies.txt
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileAds.txt
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileSpyware.txt
https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/crypto
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/notserious
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriff
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/samsung
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry
https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt
https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
https://raw.githubusercontent.com/vokins/yhosts/master/hosts
https://raw.githubusercontent.com/wlqY8gkVb9w1Ck5MVD4lBre9nWJez8/W10TelemetryBlocklist/master/W10TelemetryBlocklist
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
https://someonewhocares.org/hosts/zero/hosts
https://ssl.bblck.me/blacklists/hosts-file.txt
https://urlhaus.abuse.ch/downloads/hostfile/
https://v.firebog.net/hosts/AdguardDNS.txt
https://v.firebog.net/hosts/Admiral.txt
https://v.firebog.net/hosts/BillStearns.txt
https://v.firebog.net/hosts/Easylist.txt
https://v.firebog.net/hosts/Easyprivacy.txt
https://v.firebog.net/hosts/Prigent-Ads.txt
https://v.firebog.net/hosts/Prigent-Crypto.txt
https://v.firebog.net/hosts/Prigent-Malware.txt
https://v.firebog.net/hosts/Shalla-mal.txt
https://v.firebog.net/hosts/static/w3kbl.txt
https://winhelp2002.mvps.org/hosts.txt
https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
https://www.joewein.net/dl/bl/dom-bl-base.txt
https://www.malwaredomainlist.com/hostslist/hosts.txt
https://www.stopforumspam.com/downloads/toxic_domains_whole.txt
https://www.sunshine.it/blacklist.txt
https://www.technoy.de/lists/blocklist.txt
https://www.technoy.de/lists/fake-streaming.txt
https://www.technoy.de/lists/malware2.txt
https://www.technoy.de/lists/Session-Replay.txt
https://www.technoy.de/lists/Suspicious.txt
https://www.technoy.de/lists/xporn.txt
https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser
https://zerodot1.gitlab.io/CoinBlockerLists/list_browser.txt
https://zerodot1.gitlab.io/CoinBlockerLists/list_optional.txt
https://zerodot1.gitlab.io/CoinBlockerLists/list.txt


## Faux positifs (Whitelist)

0-edge-chat.facebook.com
0.client-channel.google.com
1-edge-chat.facebook.com
1drv.com
2-edge-chat.facebook.com
2.android.pool.ntp.org
3-edge-chat.facebook.com
4-edge-chat.facebook.com
5-edge-chat.facebook.com
6-edge-chat.facebook.com
adf.ly
ae01.alicdn.com
akamaihd.net
akamaitechnologies.com
akamaized.net
amazonaws.com
amzn.com
amzn.to
android.clients.google.com
api-global.netflix.com
api.facebook.com
api.ipify.org
api.rlje.net
app-api.ted.com
appboot.netflix.com
appleid.apple.com
apps.skype.com
appsbackup-pa.clients6.google.com
appsbackup-pa.googleapis.com
appspot-preview.l.google.com
apresolve.spotify.com
apt.sonarr.tv
aspnetcdn.com
attestation.xboxlive.com
audio-ake.spotify.com.edgesuite.net
ax.phobos.apple.com.edgesuite.net
b-api.facebook.com
b-graph.facebook.com
bigzipfiles.facebook.com
bit.ly
brightcove.net
c.s-microsoft.com
captive.apple.com
cdn.cloudflare.net
cdn.embedly.com
cdn.fbsbx.com
cdn.optimizely.com
cdn.vidible.tv
cdn2.optimizely.com
cdn3.optimizely.com
cdnjs.cloudflare.com
cert.mgt.xboxlive.com
client-s.gateway.messenger.live.com
clientconfig.passport.net
clients1.google.com
clients2.google.com
clients3.google.com
clients4.google.com
clients5.google.com
clients6.google.com
cognito-identity.us-east-1.amazonaws.com
connect.facebook.com
connectivitycheck.android.com
connectivitycheck.gstatic.com
continuum.dds.microsoft.com
cpms.spop10.ams.plex.bz
cpms35.spop10.ams.plex.bz
creative.ak.fbcdn.net
cse.google.com
ctldl.windowsupdate.com
cws.conviva.com
d2c8v52l 5s99u.cloudfront.net
d2gatte9o95jao.cloudfront.net
dashboard.plex.tv
dataplicity.com
def-vef.xboxlive.com
delivery.vidible.tv
det-ta-g7g.amazon.com
dev.virtualearth.net
device-messaging-na.amazon.com
device-metrics-us-2.amazon.com
device-metrics-us.amazon.com
device.auth.xboxlive.com
display.ugc.bazaarvoice.com
displaycatalog.mp.microsoft.com
dl.delivery.mp.microsoft.com
dl.dropbox.com
dl.dropboxusercontent.com
dl.google.com
dns.msftncsi.com
download.sonarr.tv
drift.com
driftt.com
drive.google.com
dynupdate.no-ip.com
ecn.dev.virtualearth.net
edge-chat.facebook.com
edge-mqtt.facebook.com
edge.api.brightcove.com
eds.xboxlive.com
events.gfe.nvidia.com
external-lhr0-1.xx.fbcdn.net
external-lhr1-1.xx.fbcdn.net
external-lhr10-1.xx.fbcdn.net
external-lhr2-1.xx.fbcdn.net
external-lhr3-1.xx.fbcdn.net
external-lhr4-1.xx.fbcdn.net
external-lhr5-1.xx.fbcdn.net
external-lhr6-1.xx.fbcdn.net
external-lhr7-1.xx.fbcdn.net
external-lhr8-1.xx.fbcdn.net
external-lhr9-1.xx.fbcdn.net
facebook.com
facebook.net
fb.me
fbcdn-creative-a.akamaihd.net
fbcdn.net
fe3.delivery.dsp.mp.microsoft.com.nsatc.net
firestore.googleapis.com
fonts.gstatic.com
forums.sonarr.tv
g.live.com
geo-prod.do.dsp.mp.microsoft.com
geo3.ggpht.com
gfwsl.geforce.com
giphy.com
github.com
github.io
goo.gl
googleapis.com
googleapis.l.google.com
graph.facebook.com
graph.instagram.com
gravatar.com
gsp1.apple.com
gstatic.com
help.ui.xboxlive.com
hls.ted.com
i.s-microsoft.com
i.ytimg.com
i1.ytimg.com
imagesak.secureserver.net
img.vidible.tv
imgix.net
imgs.xkcd.com
instagram.c10r.facebook.com
instantmessaging-pa.googleapis.com
intercom.io
ipv6.msftncsi.com
jquery.com
jsdelivr.net
keystone.mwbsys.com
l.facebook.com
lastfm-img2.akamaized.net
licensing.xboxlive.com
live.com
livepassdl.conviva.com
login.live.com
login.microsoftonline.com
m.hotmail.com
manifest.googlevideo.com
market.spotify.com
meta-db-worker02.pop.ric.plex.bz
meta.plex.bz
meta.plex.tv
microsoftonline.com
mobile-ap.spotify.com
mqtt-mini.facebook.com
mqtt.c10r.facebook.com
msftncsi.com
my.plexapp.com
nexusrules.officeapps.live.com
nine.plugins.plexapp.com
no-ip.com
node.plexapp.com
notify.xboxlive.com
npr-news.streaming.adswizz.com
ns1.dropbox.com
ns2.dropbox.com
o1.email.plex.tv
o2.sg0.plex.tv
ocsp.apple.com
ocsp.rootg2.amazontrust.com
office.com
office.net
office365.com
officeclient.microsoft.com
om.cbsi.com
onedrive.live.com
ota-downloads.nvidia.com
outlook.live.com
outlook.office365.com
ow.ly
pings.conviva.com
placehold.it
placeholdit.imgix.net
players.brightcove.net
portal.fb.com
pricelist.skype.com
prod.telemetry.ros.rockstargames.com
products.office.com
proxy.plex.bz
proxy.plex.tv
proxy02.pop.ord.plex.bz
pubsub.plex.bz
pubsub.plex.tv
raw.githubusercontent.com
redirector.googlevideo.com
reminders-pa.googleapis.com
res.cloudinary.com
s.gateway.messenger.live.com
s.marketwatch.com
s.shopify.com
s.youtube.com
s.ytimg.com
s1.symcb.com
s1.wp.com
s2.symcb.com
s2.youtube.com
s3-eu-west-1.amazonaws.com
s3.amazonaws.com
s3.symcb.com
s4.symcb.com
s5.symcb.com
sa.symcb.com
scontent-lhr3-1.xx.fbcdn.net
scontent.fgdl5-1.fna.fbcdn.net
scontent.xx.fbcdn.net
script.google.com
secure.avangate.com
secure.brightcove.com
secure.netflix.com
secure.surveymonkey.com
services.sonarr.tv
settings-win.data.microsoft.com
skyhook.sonarr.tv
sls.update.microsoft.com.akadns.net
spclient.wg.spotify.com
ssl.p.jwpcdn.com
stackoverflow.com
staging.plex.tv
star-mini.c10r.facebook.com
star.c10r.facebook.com
status.plex.tv
t.co
t0.ssl.ak.dynamic.tiles.virtualearth.net
t0.ssl.ak.tiles.virtualearth.net
tawk.to
tedcdn.com
themoviedb.com
thetvdb.com
tinyurl.com
title.auth.xboxlive.com
title.mgt.xboxlive.com
todo-ta-g7g.amazon.com
tracking-protection.cdn.mozil a.net
tracking.epicgames.com
traffic.libsyn.com
tvdb2.plex.tv
tvthemes.plexapp.com
twimg.com
twitter.com
ui.skype.com
unagi-na.amazon.com
upgrade.scdn.com
upload.facebook.com
us-east-1.amazonaws.com
v10.events.data.microsoft.com
v10.vortex-win.data.microsoft.com
v20.events.data.microsoft.com
video-stats.l.google.com
videos.vidible.tv
vidtech.cbsinteractive.com
widget-cdn.rpxnow.com
win10.ipv6.microsoft.com
wp.com
ws.audioscrobbler.com
www.adf.ly
www.apple.com
www.appleiphonecel .com
www.bit.ly
www.dataplicity.com
www.googleapis.com
www.msftconnecttest.com
www.msftncsi.com
www.no-ip.com
www.ow.ly
www.worldometers.info
www.xboxlive.com
www.youtube-nocookie.com
xbox.ipv6.microsoft.com
xboxexperiencesprod.experimentation.xboxlive.com
xflight.xboxlive.com
xkms.xboxlive.com
xsts.auth.xboxlive.com
youtu.be
youtube-nocookie.com
yt3.ggpht.com
zee.cws.conviva.com
