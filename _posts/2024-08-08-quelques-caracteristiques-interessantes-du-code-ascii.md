---
author: Nico
date: 2024-08-08 08:00:00+02:00
image:
    feature: null
lang: fr
layout: page
published: false
redirect_from: []
tags: []
title: Quelques caractéristiques intéressantes du code ASCII <small>(La dernière va vous perforer 🤪)</small>
---

<style>
    table {
        font-family: monospace
    }
    table strong {
        color: #CCC;
    }
</style>

Voici quelques caractéristiques intéressantes du code ASCII tirés de cette vidéo :<br>
[From NUL to DEL: Why 7 Bit ASCII IS Actually Really Clever](https://www.youtube.com/watch?v=9rJO3vptblU)

<iframe width="560" height="315" src="https://www.youtube.com/embed/9rJO3vptblU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Je n’ai reporté que quelques points, donc regardez la vidéo pour le reste.

J’ai plus ou moins reporté le texte original avec le style “parlé”, mais j’ai élagué un peu.

L’auteur a publié un errata quelques semaines après :

<https://www.youtube.com/watch?v=1MHSGivAJvI>

## Caractère <kbd>BEL</kbd> “Bel”

> On peut faire sonner le terminal avec le caractère <kbd>BEL</kbd> (code ASCII = 0x7) :

-   Sous Windows, ouvrir le terminal CMD et taper `echo ^g` où `^g` est le raccourci clavier <kbd>ctrl</kbd> + <span class="nowrap"><kbd>g</kbd>&#8201;.</span>
-   Sous macOS et Linux, ouvrir l’application Terminal et taper `echo -e "\a"`.
    La séquence d’échappement `\a` signifie <kbd>BEL</kbd>.
    C’est analogue à `\n` qui signifie saut de ligne (newline).
    Sous macOS, vérifiez si le son est activé dans les préférences du Terminal sous <span class="nowrap"><code>Profiles/Advanced/Bell/Audible bell</code>.</span>

## Caractères de fin de ligne

> [10:04] Je suis sûr que la plupart d’entre vous sont douloureusement conscients que les fichiers textes sous Linux et macOS utilisent un seul caractère pour indiquer une nouvelle ligne, mais Windows en utilise deux et la raison de cette différence remonte aux premiers jours de l’ASCII.
> En ce temps-là, il y avait un système d’exploitation appelé c. C’était le prédécesseur d’Unix et c’était l’un des premiers systèmes à intégrer des pilotes de périphériques.
> Il ne communiquait pas avec le clavier ou le télétype directement, mais à travers une couche d’abstraction, ce qui fait qu’avec Multics, il était trivial d’ajouter un retour à la ligne <kbd>CR</kbd> lorsqu’un caractère de saut de ligne <kbd>LF</kbd> était lu.

> Windows, pour sa part, est basé sur MS DOS, lui-même basé sur un ancien système appelé CP/M et qui n’intégrait pas de pilotes de périphériques.
> Il envoyait donc des flux de données bruts aux périphériques et devait donc envoyer deux caractères pour faire une fin de ligne : le caractère <kbd>CR</kbd> pour faire revenir la tête d’impression au début de la ligne et le caractère <kbd>LF</kbd> pour faire avancer la feuille.

> Apple a utilisé le caractère <kbd>CR</kbd> seul jusqu’à l’introduction d’OSX en 2001 qui est basé sur Unix BSD et qui utilise donc uniquement le caractère <kbd>LF</kbd> pour les fins de ligne.
> Mais plus de 20 ans après, il existe encore un programme qui utilise <kbd>CR</kbd> pour les fins de ligne : Adobe After Effects.

[10:04]: https://youtu.be/9rJO3vptblU?t=604

## Guillemets ouvrants et fermants

> [13:42] Le code ASCII n’a pas de guillemets ouvrants et fermants comme <kbd>“</kbd> et <span class="nowrap"><kbd>”</kbd>&#8201;.</span>
> Si ça avait été le cas, on aurait pu imbriquer des chaines de caractères à l’infini très facilement et l’analyse syntaxique (_parsing_) aurait été nettement plus simple.

<style>
    .open {color: tomato;}
    .close {color: blue;}
</style>

<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight">
<code>console.log(<span class="open">“Si JavaScript utilisait<br>des <span class="close">“guillemets ouvrants et fermants”</span>,<br>est-ce qu’il ressemblerait à ça ?”</span>);</code>
</pre>
</div>
</div>

_[Note perso] Je ne suis qu’à moitié d’accord avec Dylan. En effet, avec les caractères déjà disponibles en ASCII on aurait très bien pu créer des syntaxes où les guillemets ouvrants et fermants sont différents en début et en fin de chaine. Donc on a pas besoin de guillemets ouvrants et fermants (même si ça serait plus joli). Par exemple :_

<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight">
<code>console.log(<span class="open">"Si JavaScript utilisait<br>des <span class="close">"guillemets ouvrants et fermants'</span>,<br>est-ce qu’il ressemblerait à ça ?'</span>);</code>
</pre>
</div>
</div>

_Ce concept est largement utilisé dans le langage HTML avec les balises ouvrantes et fermantes._
_On est donc sûr que ça tient la route._

> [13:42]: https://youtu.be/9rJO3vptblU?t=822

## Majuscules et minuscules

> [14:45] En ASCII, la différence entre les majuscules et les minuscules est toujours d’un seul bit. Par conséquent, si vous souhaitez effectuer une comparaison de chaine insensible à la casse, il vous suffit d’ignorer un bit.

> Sur les premiers claviers mécaniques, la touche majuscule était physiquement câblée pour activer et désactiver ce bit.

> En plaçant toutes les lettres de l’alphabet dans des blocs continus, on peut faire des choses assez élégantes : si vous voulez savoir si un caractère est une majuscule, vérifiez simplement qu’il se situe entre A et Z.

[14:45]: https://youtu.be/9rJO3vptblU?t=885

| CARACTÈRE<br>ASCII | CODE ASCII DÉCIMAL | CODE ASCII BINAIRE | CARACTÈRE<br>ASCII | CODE ASCII DÉCIMAL | CODE ASCII BINAIRE |
| -----------------: | -----------------: | -----------------: | -----------------: | -----------------: | -----------------: |
|       <kbd>A</kbd> |                 65 |        1**0**00001 |       <kbd>a</kbd> |                 97 |        1**1**00001 |
|       <kbd>B</kbd> |                 66 |        1**0**00010 |       <kbd>b</kbd> |                 98 |        1**1**00010 |
|       <kbd>C</kbd> |                 67 |        1**0**00011 |       <kbd>c</kbd> |                 99 |        1**1**00011 |
|       <kbd>D</kbd> |                 68 |        1**0**00100 |       <kbd>d</kbd> |                100 |        1**1**00100 |
|       <kbd>E</kbd> |                 69 |        1**0**00101 |       <kbd>e</kbd> |                101 |        1**1**00101 |
|       <kbd>F</kbd> |                 70 |        1**0**00110 |       <kbd>f</kbd> |                102 |        1**1**00110 |
|       <kbd>G</kbd> |                 71 |        1**0**00111 |       <kbd>g</kbd> |                103 |        1**1**00111 |
|       <kbd>H</kbd> |                 72 |        1**0**01000 |       <kbd>h</kbd> |                104 |        1**1**01000 |
|       <kbd>I</kbd> |                 73 |        1**0**01001 |       <kbd>i</kbd> |                105 |        1**1**01001 |
|       <kbd>J</kbd> |                 74 |        1**0**01010 |       <kbd>j</kbd> |                106 |        1**1**01010 |
|       <kbd>K</kbd> |                 75 |        1**0**01011 |       <kbd>k</kbd> |                107 |        1**1**01011 |
|       <kbd>L</kbd> |                 76 |        1**0**01100 |       <kbd>l</kbd> |                108 |        1**1**01100 |
|       <kbd>M</kbd> |                 77 |        1**0**01101 |       <kbd>m</kbd> |                109 |        1**1**01101 |
|       <kbd>N</kbd> |                 78 |        1**0**01110 |       <kbd>n</kbd> |                110 |        1**1**01110 |
|       <kbd>O</kbd> |                 79 |        1**0**01111 |       <kbd>o</kbd> |                111 |        1**1**01111 |
|       <kbd>P</kbd> |                 80 |        1**0**10000 |       <kbd>p</kbd> |                112 |        1**1**10000 |
|       <kbd>Q</kbd> |                 81 |        1**0**10001 |       <kbd>q</kbd> |                113 |        1**1**10001 |
|       <kbd>R</kbd> |                 82 |        1**0**10010 |       <kbd>r</kbd> |                114 |        1**1**10010 |
|       <kbd>S</kbd> |                 83 |        1**0**10011 |       <kbd>s</kbd> |                115 |        1**1**10011 |
|       <kbd>T</kbd> |                 84 |        1**0**10100 |       <kbd>t</kbd> |                116 |        1**1**10100 |
|       <kbd>U</kbd> |                 85 |        1**0**10101 |       <kbd>u</kbd> |                117 |        1**1**10101 |
|       <kbd>V</kbd> |                 86 |        1**0**10110 |       <kbd>v</kbd> |                118 |        1**1**10110 |
|       <kbd>W</kbd> |                 87 |        1**0**10111 |       <kbd>w</kbd> |                119 |        1**1**10111 |
|       <kbd>X</kbd> |                 88 |        1**0**11000 |       <kbd>x</kbd> |                120 |        1**1**11000 |
|       <kbd>Y</kbd> |                 89 |        1**0**11001 |       <kbd>y</kbd> |                121 |        1**1**11001 |
|       <kbd>Z</kbd> |                 90 |        1**0**11010 |       <kbd>z</kbd> |                122 |        1**1**11010 |

## Le caractère <kbd>Dell</kbd>

> [15:27] Pourquoi le caractère <kbd>Dell</kbd> “delete” a-t-il la valeur 127 ?
> Parce qu'en binaire, 127 s’écrit `1111111` et qu'à l'époque, les données étaient stockées en perçant des trous sur des bandes en papier.
> Si vous deviez effacer quelque chose, vous ne pouviez pas remplir les trous existants, tout ce que vous pouviez faire, c'était de percer des trous là où il n’y en avait pas.

[15:27]: https://youtu.be/9rJO3vptblU?t=927

## À voir aussi

-   [Les plus belles tables ASCII](../les-plus-belles-tables-ascii/)
-   [EBCDIC : Extended Binary Coded Decimal Interchange Code](https://fr.wikipedia.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code)
