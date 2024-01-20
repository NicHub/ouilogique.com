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
title: Comment quadrupler la taille d’une chaine en lui ajoutant un seul caractère ?
---

Dans cet article, nous allons découvrir qu’avec Python, il est possible de quadrupler la mémoire nécessaire à une chaine en ne lui ajoutant qu’un seul caractère.

> N.B. Dans cet article, quand il est fait mention de Python, il s’agit toujours de Python 3, jamais de Python 2.

Les versions utilisées pour les tests sont :

-   Python 3.11.6
-   Python 3.12.1

L’OS est macOS Sonoma 14.2.1 et les interpréteurs Python ont été installés avec [Homebrew].

[Homebrew]: https://brew.sh/

L’idée m’est venue d’écrire cet article à la suite d’[une question sur Stackoverflow] concernant la comparaison entre la taille de deux chaines : une chaine dans un fichier UTF-8 stocké sur un disque et la même chaine dans une variable Python de type `string`.
L’auteur s’étonne que la taille en mémoire soit 4 fois plus grande que celle sur disque.
Mais est-ce si surprenant ?
Voyons cela d’un peu plus près.

[une question sur Stackoverflow]: https://stackoverflow.com/q/77310610/3057377

## Différences de tailles

Il faut d’abord savoir que Python enregistre les chaines avec des caractères codés sur 1, 2 ou 4 octets, mais tous les caractères d’une même chaine doivent être codés avec le même nombre d’octets.
C’est “l’encodage à taille fixe” ou _“fixed-width encoding”_ en anglais.

En UTF-8, les choses sont un peu différentes, les caractères d’une chaine sont stockés sur 1, 2, 3 ou 4 octets, mais il est possible d’utiliser des caractères codés avec des nombres différents d’octets dans la même chaine.
C’est “l’encodage à taille variable”, ou _“variable-width encoding”_ en anglais.

Cette différence entre taille fixe et taille variable a une conséquence intéressante : il est possible de quadrupler la taille d’une chaine en mémoire en lui ajoutant un seul caractère.
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
Les 1000 premiers octets sont utilisés pour les 1000 caractères `A` et les quelques octets restants sont utilisés pour enregistrer des métadonnées.
Mais laissons ça de côté pour l’instant.

Convertissons maintenant cette chaine en sa représentation UTF-8.

```python
s1u = s1.encode("utf-8")
print(f"taille de la chaine utf-8 (RAM)  : {sys.getsizeof(s1u)} octets")
# 1033 Python 3.11 et 3.12
```

On constate que la taille de la chaine codée en UTF-8 et stockée en mémoire vive est d’environ 1000 octets.
Comme pour la chaine précédente, Python ajoute quelques octets pour les métadonnées.

Convertissons une deuxième fois cette chaine, mais cette fois, enregistrons-la sur le disque.

```python
fname = "s1u.txt"
with open(file=fname, mode="wt", encoding="utf-8") as _f:
    _f.write(s1)
print(f"taille de la chaine utf-8 (HD)   : {os.path.getsize(fname)} octets")
# 1000 Python 3.11 et 3.12
```

On constate que la taille de la chaine codée en UTF-8 et stockée sur un disque dur est exactement 1000 octets.

Conclusion : si on fait abstraction de la place prise par les métadonnées qui ne dépend pas de la taille de la chaine, on voit qu’une chaine qui ne contient que le caractère `A` à la même taille dans les trois cas : 1. en mémoire au format Python, 2. en mémoire au format UTF-8, 3. sur un disque au format UTF-8.

Voyons maintenant les cas où cette égalité n’est plus vraie.

## Quadruplons la taille de la chaine Python

Ajoutons le caractère `😈` (`chr(128520)`) codé sur 4 octets à notre chaine initiale et regardons quelle est la taille du résultat.

```python
s2 = s1 + chr(128520)
print(f"taille de la chaine python (RAM) : {sys.getsizeof(s2)} octets")
# 4080 avec Python version == 3.11
# 4064 avec Python version == 3.12
```

On constate que sa taille est maintenant de 4000 octets, plus quelques octets pour les métadonnées.
Sa taille en mémoire a donc quadruplé en ajoutant un seul caractère !
Bingo, c’est l’effet de l’encodage à largeur fixe !
Si un caractère de la chaine est codé sur 4 octets, alors tous les autres le seront aussi.
On constate également que la taille des métadonnées a légèrement augmenté car les caractères seuls prennent 1001 × 4 = 4004 octets.
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

**Résultat des courses, le rapport de taille entre la chaine Python et la chaine UTF-8 est donc de 4 !**

Si on refaisait l’exercice en utilisant 1000 × `😈` et 1 × `A`, on trouverait un rapport de taille de 1 (en faisant abstraction des métadonnées).

On constate également qu’en UTF-8 la taille de s2 est 4 octets plus grande que celle de s1.
Ceci est dû au fait qu’UTF-8 enregistre les caractères avec leur taille initiale, donc 1000 × 1 octet pour le caractère `A` et 1 × 4 octets pour le caractère `😈`.
Comme précédemment, la chaine en mémoire prend quelques octets supplémentaires pour les métadonnées.

À noter que je ne tiens pas compte des caractères codés sur 2 et 3 octets, mais le même raisonnement peut leur être étendu.

En conclusion, le rapport entre la taille mémoire utilisée par Python et la taille en UTF-8 peut varier d’un facteur allant de 1 à 4.
Ces chiffres ne sont pas valables pour les très petites chaines à cause de la taille des métadonnées.
Par contre dès que les chaines sont plus grandes, ça fonctionne très bien.

J’ai mesuré ce rapport sur une dizaine de fichiers contenant des livres entiers en français et je trouve un rapport moyen de 1.8.




```python

````