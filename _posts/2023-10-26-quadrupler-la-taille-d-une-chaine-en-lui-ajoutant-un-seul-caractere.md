---
author: Nico
date: 2024-01-07 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: false
redirect_from: []
tags: []
title: Comment quadrupler la taille d’une chaine en lui ajoutant un seul caractère ?
---

Dans cet article, nous allons découvrir quelques subtilités des chaines de caractères en Python et en UTF-8.

Particulièrement :

-   Qu’il est possible de quadrupler la mémoire nécessaire à une chaine en ne lui ajoutant qu’un seul caractère.
-   Que cela est dû au fait qu’en Python la taille des caractères d’une chaine est fixe, alors qu’UTF-8 utilise une taille de caractères variable.
-   Qu’il est possible de compter super rapidement le nombre de caractères en fonction de leur taille en octet dans une string codée en UTF-8.

> N.B. Dans cet article, quand il est fait mention de Python, il s’agit toujours de Python 3, jamais de Python 2.

Les versions utilisées pour les tests sont :

-   Python 3.11.6
-   Python 3.12.1

L’OS est macOS Sonoma 14.2.1 et les interpréteurs Python ont été installés avec [Homebrew].

[Homebrew]: https://brew.sh/

L’idée m’est venue d’écrire cet article suite à [une question sur Stackoverflow] concernant la comparaison entre la taille d’une chaine de caractères en mémoire avec Python avec sa taille quand elle est enregistrée dans un fichier UTF-8.

[une question sur Stackoverflow]: https://stackoverflow.com/q/77310610/3057377

L’auteur s’étonne que la taille en mémoire soit 4 fois plus grande que celle sur disque.
Mais est-ce si surprenant ?
Voyons cela d’un peu plus près.

## Différences de tailles

Il faut d’abord savoir que Python enregistre les chaines avec des caractères codés sur 1, 2 ou 4 octets, mais tous les caractères d’une même chaine doivent être codés avec le même nombre d’octets.
C’est “l’encodage à taille fixe” ou _“fixed-width encoding”_ en anglais.

En UTF-8, les choses sont un peu différentes, les caractères d’une chaine sont stockés sur 1, 2, 3 ou 4 octets, mais il est possible d’utiliser des caractères codés avec des nombres différents d’octets dans la même chaine.
C’est “l’encodage à taille variable”, ou _“variable-width encoding”_ en anglais.

Cette différence entre taille fixe et taille variable a une conséquence intéressante :
Il est possible de quadrupler la taille d’une chaine en mémoire en lui ajoutant un seul caractère.
Voici comment.

## Cas où la taille est (presque) identique en Python et UTF-8

Tout d’abord, créons une chaine contenant 1000 fois le même caractère codé sur 1 octet, par exemple le caractère `A` (`chr(65)`) et regardons la taille du résultat.

```python
import os
import sys

print("# chaine                         : 1000 * chr(65)")
s1 = 1000 * chr(65)
print(f"taille de la chaine python (RAM) : {sys.getsizeof(s1)} octets")
# 1049 avec Python 3.11
# 1041 avec Python 3.12
```

On voit que cette chaine fait un peu plus que 1000 octets.
Les octets supplémentaires sont utilisés pour enregistrer des métadonnées, mais laissons ça de côté pour l’instant.

Convertissons maintenant cette chaine en sa représentation UTF-8.

```python
s1u = s1.encode("utf-8")
print(f"taille de la chaine utf-8 (RAM)  : {sys.getsizeof(s1u)} octets")
# 1033 Python 3.11 et 3.12
```

On constate que la taille de la chaîne codée en UTF-8 et stockée en mémoire vive est d’environ 1000 octets.
Comme pour la chaine précédente, Python ajoute quelques octets pour les métadonnées.

Convertissons une deuxième fois cette chaîne, enregistrons-la sur le disque.

```python
fname = "s1u.txt"
with open(file=fname, mode="wt", encoding="utf-8") as _f:
    _f.write(s1)
print(f"taille de la chaine utf-8 (HD)   : {os.path.getsize(fname)} octets")
# 1000 Python 3.11 et 3.12
```

On constate que la taille de la chaîne codée en UTF-8 et stockée sur un disque dur est exactement 1000 octets.

Conclusion : si on néglige la place prise par les métadonnées qui ne dépend pas de la taille de la chaine, on voit qu’une chaine qui ne contient que le caractère `A` à la même taille dans les trois cas : 1. en mémoire au format Python, 2. en mémoire au format UTF-8, 3. sur un disque au format UTF-8.

Voyant maintenant les cas où cette égalité n’est plus vraie.

## Quadruplons la taille de la chaine Python

Ajoutons le caractère `😈` (`chr(128520)`) codé sur 4 octets à notre chaine initiale et regardons quelle est la taille du résultat.

```python
s2 = s1 + chr(128520)
print(f"taille de la chaine python (RAM) : {sys.getsizeof(s2)} octets")
# 4080 avec Python version == 3.11
# 4064 avec Python version == 3.12
```

On constate que sa taille est maintenant de 4000 octets, plus quelques octets pour les métadonnées.
Sa taille en mémoire a donc quadruplé en ajoutant un seul caractère !
Bingo, c’est l’effet de l’encodage à largeur fixe !
Si un caractère de la chaine est codé sur 4 octets, alors tous les autres le seront aussi.
On constate aussi que la taille des métadonnées a légèrement augmenté car les caractères seuls prennent 1001 × 4 = 4004 octets.
À noter également qu’en Python, les chaines sont immuables (_immutables_ en anglais).
Ce n’est donc pas la chaine initiale qui a quadruplé de taille, mais une copie modifiée de celle-ci.

Regardons maintenant ce qui se passe si on convertit notre nouvelle chaine en UTF-8 et qu’on mesure la taille du résultat.

```python
s2u = s2.encode("utf-8")
print(f"taille de la chaine utf-8 (RAM)  : {sys.getsizeof(s2u)} octets")
# 1037 Python 3.11 et 3.12
```

```python
fname = "s2u.txt"
with open(file=fname, mode="wt", encoding="utf-8") as _f:
    _f.write(s2)
print(f"taille de la chaine utf-8 (HD)   : {os.path.getsize(fname)} octets")
# 1004 Python 3.11 et 3.12
```

**Résultat des courses, le rapport de taille entre la chaine Python et la chaine UTF-8 est donc de 4 !**

Si on refaisait l’exercice en utilisant 1000 × `😈` et 1 × `A`, on trouverait un rapport de taille de 1 (en faisant abstraction des métadonnées).

On constate également qu’en UTF-8 la taille de s2 est 4 octets plus grande que celle de s1.
Ceci est dû au fait qu’UTF-8 enregistre les caractères avec leur taille initiale, donc 1000 × 1 octet pour le caractère `A` et 1 × 4 octets pour le caractère `😈`.
Comme précédemment, la chaine en mémoire prend quelques octets supplémentaires pour les métadonnées.

À noter que je ne tiens pas compte des caractères codés sur 2 et 3 octets, mais le même raisonnement peut leur être étendu.

En conclusion, le rapport entre la taille mémoire utilisée par Python et la taille en UTF-8 peut varier d’un facteur allant de 1 à 4.
Ces chiffres ne sont pas valables pour les très petites chaines à cause de la taille des métadonnées.
Par contre dès que les chaines sont plus grandes, ça fonctionne très bien.

J’ai mesuré ce rapport sur une dizaine de fichiers contenant des livres entiers en français et je trouve un rapport moyen de 1.8.

## Les points de code

Pour comprendre, les chapitres suivants, il faut d’abord comprendre ce qu’est un point de code.

Un “point de code” est un chiffre qui est attribué à chaque caractère de façon univoque.
Les points de code sont définis par la norme Unicode et on peut les consulter dans la [table officielle des caractères Unicode]
ou sur le site “[table de caractères Unicode]” (anciennement _unicode-table.com_).

[table officielle des caractères Unicode]: https://www.unicode.org/charts/
[table de caractères Unicode]: https://symbl.cc/fr/unicode/table/

> N.B. L’ancêtre d’unicode est l’ASCII.

## Calculer la taille d’une chaine en Python

Pour calculer la taille totale utilisée par Python pour représenter une chaine, il faut en premier trouver le caractère de la chaine qui a le point de code le plus élevé puis utiliser la table ci-dessous pour déterminer le nombre d’octets que Python utilisera pour stocker les caractères de la chaine.
À noter que dès que l’on trouve un caractère dont le point de code est supérieur à 65’535, on est sûr que Python encodera la chaine sur 4 octets.

|  Points<br>de code  | Nb d’octets par<br>caractère<br>(Python) | Encodage |
| :-----------------: | :--------------------------------------: | :------: |
|      0 .. 255       |                    1                     | Latin-1  |
|    256 .. 65’535    |                    2                     |  USC-2   |
| 65’536 .. 1’114’111 |                    4                     |  USC-4   |

Ensuite, il faut déterminer la taille des métadonnées.
Elle dépend principalement de l’encodage.
À noter que la taille des métadonnées ne dépend pas du nombre de caractères sauf pour quelques exceptions détaillées dans les tableaux ci-dessous.

**Nombre de caractères dans la chaine == 0**

Lorsqu’une chaîne est vide, le nombre d’octets par caractère n’est pas défini (il est probablement supposé étant égal à 1 octet).
Ces valeurs resteront les mêmes pour les chaines contenant uniquement des points de codes inférieurs à 128.

| Nb d’octets<br>des métadonnées<br>Python == 3.11 | Nb d’octets<br>des métadonnées<br>Python == 3.12 |
| :----------------------------------------------: | :----------------------------------------------: |
|                        49                        |                        41                        |

**Nombre de caractères dans la chaine == 1<br>et nb octet par caractère == 2<br>et Python == 3.12**

Curieusement, en Python 3.12, si la chaine ne contient qu’un caractère codé sur deux octets, la taille de la chaine ne suit pas la relation énoncée après les tableaux.

En plus, une telle chaine prend au total 61 octets alors qu’une chaine avec un caractère de plus (toujours codé sur 2 octets) ne prendra que 59 octets, soit deux octets de moins.

| Points<br>de code | Nb d’octets par<br>caractère | Nb d’octets<br>des métadonnées<br>Python == 3.12 |
| :---------------: | :--------------------------: | :----------------------------------------------: |
|   256 .. 65535    |              2               |                        59                        |

**Tous les autres cas**

| Points<br>de code  | Nb d’octets par<br>caractère | Nb d’octets<br>des métadonnées<br>Python == 3.11 | Nb d’octets<br>des métadonnées<br>Python == 3.12 |
| :----------------: | :--------------------------: | :----------------------------------------------: | :----------------------------------------------: |
|      0 .. 127      |              1               |                        49                        |                        41                        |
|     128 .. 255     |              1               |                        73                        |                        57                        |
|    256 .. 65535    |              2               |                        74                        |                        58                        |
| 65536 .. 1’114’111 |              4               |                        76                        |                        60                        |

Maintenant que nous connaissons la taille en octet de chaque caractère et la taille des métadonnées, nous pouvons calculer la taille en mémoire de la chaine avec la relation suivante :

    T = N × O + M

où

-   T = Taille de la chaine en mémoire
-   N = Nb total de caractères
-   O = Nb d’octets nécessaires pour le caractère ayant le point de code le plus élevé
-   M = Nb d’octets utilisés par les métadonnées

> N.B. En Python, la valeur du point de code le plus grand possible peut être obtenue avec la constante `sys.maxunicode`.
> Pour les versions conventionnelles de Python, elle vaut `1’114’111 = 2²⁰ + 2¹⁶ - 1`.
> Micropython n’implémente pas la

## Calculer la taille d’une chaine codée en UTF-8

En UTF-8, le calcul de la taille d’une chaine est différent de celui utilisé pour les chaines Python.
En effet, les caractères sont enregistrés sur 1, 2, 3 ou 4 octets et les plages des points de code ne sont pas exactement les mêmes.

|  Points<br>de code  | Nb d’octets par<br>caractère<br>(UTF-8) |
| :-----------------: | :-------------------------------------: |
|      0 .. 127       |                    1                    |
|     128 .. 2047     |                    2                    |
|   2048 .. 65’535    |                    3                    |
| 65’536 .. 1’114’111 |                    4                    |

Contrairement à Python, en UTF-8 chaque caractère conserve sa taille en octet, donc la taille de la chaine en mémoire sera la suivante :

    T = Σ Oi

où

-   T = Taille de la chaine en mémoire
-   Oi = Nb d’octets nécessaire pour chaque caractère individuel

> N.B. Par défaut, UTF-8 n’utilise pas de métadonnées.
> Cepandant, il existe une variante qui s’appelle _UTF-8 with BOM_ _(Byte order mask)_ qui ajoute la séquence d’octet `EF BB BF` au début du fichier pour indiquer explicitement que le fichier est au format UTF-8.
> Ceci peut être utile si on doit être absolument sûr du type de fichier par exemple s’il est nécessaire de faire la distinction entre des fichiers UTF-8 et ASCII.
> En effet, un fichier UTF-8 qui ne contient que des caractères dont les points de code sont inférieurs à 128 ne peut pas être distingué d’un fichier ASCII avec le même contenu.
> Ce sont les mêmes fichiers.
> D’où l’intérêt de spécifier que l’on souhaite que le fichier soit traité comme étant en UTF-8.
> Dans la pratique, le BOM est rarement utilisé et peut apporter plus de problèmes que de solutions.
> Par contre, pour UTF-16 et UTF-32 le BOM est utile, mais ça ne fait pas partie du cadre de cet article.

<!--

UCS

Universal Character Set

UCS2 : C'est un schéma de codage où chaque caractère Unicode est représenté sur 2 octets. Cela signifie qu'il peut représenter des caractères Unicode allant de U+0000 à U+FFFF, soit 65 536 caractères différents.

UCS4 : À l'inverse, UCS4 utilise 4 octets pour représenter chaque caractère Unicode. Cela permet de représenter l'ensemble de l'espace Unicode, allant de U+0000 à U+10FFFF, soit 1 114 112 caractères différents.

-->

## Conséquences des différences d’encodage

On l’a vu, Python et UTF-8 sont passablement différents dans leur manière d’encoder les chaines de caractères.
Voici quelques conséquences de ces différences.

-   On est obligé de lire entièrement une chaine UTF-8 si l’on veut :

    -   Connaître la taille qu’elle prendra en mémoire.
    -   Connaître le nombre de caractères qu’elle contient.
    -   Connaître la position de tous les caractères.

En effet, si une chaine est enregistrée dans un fichier qui prend 1000 octets sur le disque, on ne peut pas savoir à l’avance s’il contient 1000 x 1 octets, 250 × 4 octets ou n’importe quelle autre combinaison avec des caractères codés sur 2 ou 3 octets.

-   L’accès à une position aléatoire dans une chaine UTF-8 est peu performant, puisqu’on ne connait la position d’un caractère qu’en lisant les caractères qui le précède.
    Si cet aspect est important, on préfèrera utiliser UTF-32 qui enregistre tous les caractères sur 4 octets.

-   On ne peut pas calculer la taille en mémoire vive en connaissant le nombre de caractères codés sur 1, 2, 3 ou 4 octets en UTF-8 parce que Python n’utilise pas les mêmes tailles pour les mêmes points de code comme on l’a vu dans les tableaux ci-dessus et sur la figure suivante.

```log
        0         127        255         2047        65535      1’114’111
Python  |_________1 B_________|__________2 B___________|____4 B____|
 UTF-8  |____1 B___|_🤪________2 B__________|____3 B_____|____4 B____|
```

## ...

```python
import numpy as np
fname = "./test_files/it.txt_part_0001.txt"
content = np.memmap(fname, dtype="uint8", mode="r")
byte_counters = {
    "1-B": np.count_nonzero(content >> 7 == 0b0),
    "2-B": np.count_nonzero(content >> 5 == 0b110),
    "3-B": np.count_nonzero(content >> 4 == 0b1110),
    "4-B": np.count_nonzero(content >> 3 == 0b11110),
}
print(byte_counters)
```

it.txt_part_0001_unicode_map.txt

<https://www.swisstransfer.com/d/815a168d-d818-4da3-9c83-462211c2f58d>

<https://data.statmt.org/cc-100/>

<https://data.statmt.org/cc-100/it.txt.xz>

<https://symbl.cc/en/unicode/table/>

<https://betterprogramming.pub/an-interviewers-favorite-question-how-are-python-strings-stored-in-internal-memory-ac0eaef9d9c2>

<https://rushter.com/blog/python-strings-and-memory/>

<!--


import sys

s1 = 1 * chr(181)
s2 = 2 * chr(181)
print(sys.getsizeof(s1), sys.getsizeof(s2))

# Python9  74 75
# Python10 74 75
# Python11 74 75
# Python12 61 59





Note that every string in Python takes additional 49-80 bytes of memory, where it stores supplementary information, such as hash, length, length in bytes, encoding type and string flags. That's why an empty string takes 49 bytes of memory.
 -->
