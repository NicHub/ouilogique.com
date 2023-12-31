---
author: Nico
date: 2023-10-26 12:00:00+01:00
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

> N.B.
> Dans cet article, quand il est fait mention de Python, il s’agit toujours de Python 3, jamais de Python 2.

Les versions utilisées pour les tests sont :

-   Python 3.11.6
-   Python 3.12.1

L’OS est macOS Sonoma 14.2.1 et les interpréteurs Python ont été installés avec [Homebrew].

[Homebrew]: https://brew.sh/

## Calculer la taille d’une chaine en mémoire

## Calculer la taille d’une chaine codée en UTF-8

## Conséquences des différences d’encodage

## ...

L’idée m’est venue d’écrire cet article suite à [une question sur Stackoverflow] concernant la comparaison entre la taille d’une chaine de caractères en mémoire avec Python avec sa taille quand elle est enregistrée dans un fichier UTF-8.

[une question sur Stackoverflow]: https://stackoverflow.com/q/77310610/3057377

L’auteur s’étonne que la taille en mémoire soit 4 fois plus grande que celle sur disque.
Mais est-ce si surprenant ?
Voyons cela d’un peu plus près.

Il faut d’abord savoir que Python enregistre les chaines avec des caractères codés sur 1, 2 ou 4 octets, mais tous les caractères d’une même chaine doivent être codés avec le même nombre d’octets.
C’est “l’encodage à taille fixe” ou _“fixed-width encoding”_ en anglais.

En UTF-8, les choses sont un peu différentes, les chaines sont stockées sur 1, 2, 3 ou 4 octets, mais il est possible d’utiliser des caractères codés avec des nombres différents d’octets dans la même chaine.
C’est “l’encodage à taille variable”, ou _“variable-width encoding”_ en anglais.

Cette différence entre taille fixe et taille variable a une conséquence intéressante.
Il est possible de quadrupler la taille d’une chaine en mémoire en lui ajoutant un seul caractère.
Voici comment.

Tout d’abord, créons une chaine contenant 1000 fois le même caractère codé sur 1 octet, par exemple le caractère `A` et regardons la taille du résultat.

```python
import sys
s1 = "A" * 1000
print(sys.getsizeof(s1))
# 1049 avec Python version == 3.11
# 1041 avec Python version == 3.12
```

On voit que cette chaine fait un peu plus que 1000 octets.
Les octets supplémentaires sont utilisés pour enregistrer des métadonnées, mais laissons ça de côté pour l’instant.

Maintenant convertissons cette chaine en sa représentation UTF-8.

```python
s1u = s1.encode("utf-8")
print(sys.getsizeof(s1u))
# 1033 Pour toutes les versions de Python
```

On constate que sa taille est d’environ 1000 octets.
Comme pour la chaine précédente, Python ajoute quelques octets pour les métadonnées.

Convertissons une deuxième fois cette chaîne, mais cette fois-ci en l’enregistrant sur le disque.

```python
import os
fname = "s1u.txt"
with open(file=fname, mode="wt", encoding="utf-8") as _f:
    _f.write(s1)
os.path.getsize(fname)
# 1000 Pour toutes les versions de Python
```

On constate que sur le disque, la taille de cette chaîne au format UTF-8 est d’exactement 1000 octets.

C’est maintenant que les choses deviennent intéressantes.
Ajoutons un caractère codé sur 4 octets à notre chaine initiale et regardons quelle est la taille du résultat.

```python
s2 = s1 + "😈"
print(sys.getsizeof(s2))
# 4080 avec Python version == 3.11
# 4064 avec Python version == 3.12
```

On constate que sa taille est maintenant de 4000 octets, plus quelques octets pour les métadonnées.
Sa taille en mémoire a donc quadruplé en ajoutant un seul caractère !
Bingo, c’est l’effet de l’encodage à largeur fixe !
Si un caractère de la chaine est codé sur 4 octets, alors tous les autres le seront aussi.
On constate aussi que la taille des métadonnées a légèrement augmenté car les caractères seuls prennent 1001 × 4 = 4004 octets.

Regardons maintenant ce qui se passe si on convertit notre nouvelle chaine en UTF-8 et qu’on mesure la taille du résultat.

```python
s2u = s2.encode("utf-8")
print(sys.getsizeof(s2u))
# 1037
```

On constate qu’en UTF-8 la taille de s2 est 4 octets plus grande que celle de s1.
Ceci est dû au fait qu’UTF-8 enregistre les caractères avec leur taille initiale, donc 1000 × 1 octet pour le caractère `A` et 1 × 4 octets pour le caractère `😈`.

Si on refaisait l’exercice en utilisant 1000 × `😈` et 1 × `A`, on trouverait un rapport de taille proche de 1.

À noter que je ne tiens pas compte des caractères codés sur 2 et 3 octets, mais le même raisonnement peut facilement leur être étendu.

En conclusion, le rapport entre la taille mémoire utilisée par Python et la taille en UTF-8 peut varier d’un facteur allant de 1 à 4.
Ces chiffres ne sont pas valables pour les très petites chaines à cause de la taille des métadonnées.
Par contre dès que les chaines sont plus grandes, ça fonctionne très bien.

J’ai mesuré ce rapport sur une dizaine de fichiers contenant des livres entiers en français et je trouve un rapport moyen de 1.8.

## Calculer la taille d’une chaine en mémoire

<!--

Pour calculer la taille d


 -->

Nous avons vu qu’en Python, la taille d’une chaine en mémoire dépend très fortement des caractères qu’elle contient et pas seulement de leur quantité.

Chaque caractère est défini par un nombre appelé point de code.
On peut les consulter dans la [table officielle des caractères Unicode]
ou sur le site “[table de caractères Unicode]” (anciennement _unicode-table.com_).

[table officielle des caractères Unicode]: https://www.unicode.org/charts/
[table de caractères Unicode]: https://symbl.cc/fr/unicode/table/

Pour calculer la taille totale utilisée par Python pour représenter une chaine, il faut en premier trouver le caractère de la chaine qui a le point de code le plus élevé.
Le nombre d’octets utilisés par Python pour représenter ce point de code sera utilisé pour tous les autres points de code de la chaine.

**Taille en octets en fonction des points de code**

| Points<br>de code  | Nb d’octets par<br>caractère | Encodage |
| :----------------: | :--------------------------: | :------: |
|      0 .. 127      |              1               | Latin-1  |
|     128 .. 255     |              1               | Latin-1  |
|    256 .. 65535    |              2               |  USC-2   |
| 65536 .. 1’114’111 |              4               |  USC-4   |

Ensuite, il faut déterminer la taille des métadonnées.
Elle dépend dépend principalement de la taille en octet du point de code le plus élevé.
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

> N.B. En Python, la valeur du point de code le plus grand possible peut être obtenue avec la constante `sys.maxunicode` et elle vaut `1’114’111 = 2²⁰ + 2¹⁶ - 1`.

## Calculer la taille d’une chaine codée en UTF-8

En UTF-8, le calcul de la taille d’une chaine est différent de celui utilisé pour les chaines Python.
En effet, les caractères sont enregistrés sur 1, 2, 3 ou 4 octets et les plages des points de code ne sont pas exactement les mêmes.

| Points<br>de code  | Nb d’octets<br>par caractère |
| :----------------: | :--------------------------: |
|      0 .. 127      |              1               |
|    128 .. 2047     |              2               |
|   2048 .. 65535    |              3               |
| 65536 .. 1’114’111 |              4               |

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
Python  |____1 o____|____1 o____|________2 o___________|____4 o____|
 UTF-8  |____1 o____|__________2 o_________|____3 o____|____4 o____|
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

<https://symbl.cc/en/unicode/table/>

<https://betterprogramming.pub/an-interviewers-favorite-question-how-are-python-strings-stored-in-internal-memory-ac0eaef9d9c2>

<https://data.statmt.org/cc-100/it.txt.xz>

<https://rushter.com/blog/python-strings-and-memory/>
