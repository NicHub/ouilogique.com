---
author: Nico
date: 2024-01-08 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: false
redirect_from: []
tags: []
title: Calculer la taille d’une chaine en Python
---

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
> CircuitPython n’implémente pas la constante `sys.maxunicode`, mais il ne retourne pas d’erreur lorsqu’on exécute la commande `chr(1_114_111)`.
> J’ai testé avec [CircuitPython 8.2.9 sur Lolin S2 Mini] qui utilise Python 3.4.0.

[CircuitPython 8.2.9 sur Lolin S2 Mini]: https://circuitpython.org/board/lolin_s2_mini/

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
> Cependant, il existe une variante qui s’appelle _UTF-8 with BOM_ _(Byte order mask)_ qui ajoute la séquence d’octets `EF BB BF`au début du fichier pour indiquer explicitement que le fichier est au format UTF-8.
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
 UTF-8  |____1 B___|_________2 B__________|____3 B_____|____4 B____|
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

