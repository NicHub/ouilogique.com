---
layout: page
title: "Les pointeurs en C"
modified:
categories:
excerpt:
tags: []
image:
    feature:
date: 2016-11-01T20:17:00+01:00
published: true
author: Nico
---

Je suis en train de suivre [le très bon cours sur la programmation en C d’Open Classrooms][1] et le deuxième exercice consiste à expliquer les pointeurs à quelqu’un qui n’y connait rien mais qui a des bases en C. Or donc, c’est une bonne occasion de créer une page sur mon blog à ce sujet histoire de faire d’une pierre deux coups, puisque d’après [Mathieu Nebra][2], le prof de ce cours, les programmeurs sont des gros fainéants qui n’aiment pas répéter deux fois les mêmes choses, et... je crois qu’il a raison.

> Les exemples de cet article sont formatés selon la façon traditionnelle des cours sur le langage C. Donc si vous ne connaissez que la présentation Arduino, cela pourrait vous surprendre. Cependant toutes les notions abordées ici sont réutilisables en Arduino C.

Donc commençons par une lapalissade grande comme une maison : la programmation, c’est surtout une affaire de données. Eh oui, rien de très extraordinaire : pour faire avancer le schmilblick les programmes que l’on donne à manger à nos ordinateurs ou nos microcontrôleurs ont besoin de données que l’on va stocker dans des variables. Et c’est bien joli de remplir leurs mémoires avec lesdites données, encore faut-il pouvoir les retrouver et pour cela il y a deux façons de s’y prendre :

1. les transmettre par valeur
2. les transmettre par référence

Voyons ça d’un peu plus près :

## Transmission de variables par valeur

Transmettre le contenu d’une variable par valeur est à peu près une des premières choses que l’on apprend à faire, quel que soit le langage de programmation que l’on étudie. Voici ce que ça donne en C :

```c++
#include <stdio.h>

int main()
{
  // On enregistre la valeur `1` dans la variable `maVariable`
  int maVariable = 1;
  // On affiche "maVariable = 1"
  // `maVariable` est transmise *par valeur* à la fonction `printf`
  printf( "maVariable = %d\n", maVariable );
  return 0;
}
```

L’exemple ci-dessus est des plus basique, mais il faut bien commencer par quelque chose. D’abord on instancie la variable `maVariable` avec le type `int` et on lui assigne la valeur `1` dans la foulée. Ensuite, on affiche le contenu de cette variable. Et pour l’affichage, on utilise la fonction `printf` à laquelle on transmet la _valeur_ de `maVariable`, c’est-à-dire `1` dans cet exemple. Ce qui ne se voit pas par contre, c’est qu’en interne, `maVariable` a été copiée, un peu comme si on avait fait une photocopie et que l’on avait envoyé cette photocopie à la fonction `printf`. Comme `printf` est une fonction de la librairie standard du C ce comportement est difficile à mettre en évidence. Pour cela, nous allons définir une fonction et tout deviendra plus clair.

```c++
#include <stdio.h>

void ex02( int maVariable );

int main()
{
  // On assigne une valeur initiale à `maVariable`
  int maVariable = 1;

  // On appelle la fonction `ex02()` et on lui transmet
  // la valeur de `maVariable`
  // (comme une photocopie de cette variable)
  ex02( maVariable );

  // Maitenant la fonction `ex02()` est terminée. Elle a modifié
  // la valeur de la variable qu’on lui a transmise, mais elle
  // ne l’a fait que sur sa “photocopie”. Donc notre “original”
  // n’est pas modifié. En conséquence, le code suivant affiche
  // "3. maVariable = 1"
  printf( "3. maVariable = %d\n", maVariable );

  return 0;
}

void ex02( int maVariable ) // `maVariable` est transmise par valeur
                            // à la fonction `ex02()`
{
  // Affiche "1. maVariable = 1"
  printf( "1. maVariable = %d\n", maVariable );

  // Modifie la valeur de `maVariable`
  maVariable = 2;

  // Affiche "2. maVariable = 2"
  printf( "2. maVariable = %d\n", maVariable );
}
```

Dans ce deuxième exemple, on se rend tout de suite compte des limitations du passage de variables par valeur :

-   Les valeurs sont copiées et la copie ne revient pas à l’expéditeur (l’expéditeur, c’est la fonction `main()` et le destinataire, c’est la fonction `ex02()`). C’est du vol qualifié et c’est surtout pas pratique si on veut que notre fonction retourne un résultat différent de la donnée de base. Bon, il y a toujours la possibilité d’utiliser un `return`, on en discutera après.
-   Et ces copies prennent de la place en mémoire. Sur un ordi ça ne causera de problèmes que pour des gros programmes, mais sur l’ATmega328p d’un Arduino UNO avec 2 ko de RAM, ça compte.
-   C’est potentiellement lent, puisqu’il faut copier les valeurs avant de les envoyer (sans compter le salaire de la secrétaire qui fait les copies... pff).

Bon ben je crois que le constat est clair, on a besoin d’un autre système pour transmettre nos variables. Et comme j’ai _spoilé_ la réponse au début de cet article, vous savez déjà qu’il s’agit de la...

## Transmission de variables par référence

Si vous ne connaissiez vraiment rien aux pointeurs avant de commencer la lecture de cet article, je suppose que l’inventeur qui sommeille en vous a dû se réveiller et s’écrier “Mais bon sang, pourquoi on ne transmettrait pas l’original plutôt que la copie !” Et bien vous venez de (ré)inventer le passage de variables par référence : BRAVO ! Et le principe est très simple, on ne transmet plus le contenu de nos variables, mais leurs adresses. Et ben oui, c’est un peu “viens chez moi, j’habite chez une copine”. Il suffit de transmettre l’adresse de la variable, histoire que le programme sache où aller passer sa soirée. Donc comme un exemple vaut 1000 mots en voici un :

```c++
#include <stdio.h>

void ex03( int *adresseDeMaVariable );

int main()
{
  // On initialise `maVariable` à 1
  int maVariable = 1;

  // Et on envoie son adresse en mémoire (et pas sa valeur)
  // Pour se faire, il suffit d’ajouter le caractère `&`
  // avant le nom de la variable.
  ex03( &maVariable ); // Suite de l’explication dans la fonction
                       // `ex03()` ci-dessous.

  // Et maintenant que la fonction `ex03()` a été exécutée
  // (elle n’est pas morte, je vous rassure), vérifions que la valeur
  // de `maVariable` a bel et bien été modifiée. Pour ce faire, nous
  // n’avons pas besoin du signe `*`.
  printf( "4. maVariable = %d\n", maVariable );
  // Et YES, ce code affiche
  // 4. maVariable = 2
  // Top cool les pointeurs !

  return 0;
}

void ex03( int *adresseDeMaVariable )
            // Cette fonction reçoit l’adresse de notre variable
            // que l’on stocke dans un pointeur sur cette variable.
            // Pour indiquer que c’est un pointeur, on ajoute
            // le signe `*` avant son nom.
            // En plus du signe `*`, on doit aussi spécifier le type
            // qui doit être identique à celui de la variable pointée
            // (`int` dans ce cas).
{
  // Maintenant on peut afficher cette adresse. Dans la pratique,
  // ça n’a pas d’intérêt, c’est juste pour montrer que c’est possible.
  // À noter que cette adresse sera certainement différente à chaque
  // exécution du programme. Ça ne sert donc à rien de la stocker
  // pour la réutiliser.
  // Notez également le format `%p` pour que `printf` affiche l’adresse
  // du pointeur correctement.
  // Enfin, et c’est le plus important, il n’y a pas de signe `*`
  // avant `adresseDeMaVariable`.
  // Ce code affiche
  // 1. adresseDeMaVariable = 0x7fff54435768
  printf( "1. adresseDeMaVariable = %p\n", adresseDeMaVariable );

  // Plus intéressant maintenant, on va afficher la valeur de notre variable.
  // C’est ce qu’on appelle “le déréférencement du pointeur”.
  // Dans ce cas, le format d’affichage pour `printf` est `%d` car notre
  // variable est de type `int`.
  // Et le plus important, c’est que dans ce cas nous avons besoin du
  // signe `*` avant `adresseDeMaVariable`.
  // Ce code affiche
  // 2. maVariable = 1
  printf( "2. maVariable = %d\n", *adresseDeMaVariable );

  // Encore plus intéressant, on va modifier la valeur pointée par le pointeur.
  // Là encore, nous avons besoin du signe `*`.
  *adresseDeMaVariable = 2;

  // Et si on l’affiche on obtient sans surprise
  // 3. maVariable = 2
  printf( "3. maVariable = %d\n", *adresseDeMaVariable );

  // Et maintenant retournons dans la fonction `main()`
  // et vérifions que la valeur de la variable que nous avons
  // transmise à `ex03()` a bel et bien été modifiée.
  // Suspense...
}
```

### Petit récapitulatif

-   Si on veut obtenir l’adresse en mémoire d’une variable, il faut utiliser le signe `&`.
-   L’adresse doit être stockée dans une variable de même type que la variable pointée (`int` dans l’exemple) avec en plus le signe `*`. C’est ce qu’on appelle un _pointeur_.
-   Si l’on demande la valeur du pointeur SANS le signe `*` on obtient en fait L’ADRESSE de la variable pointée.
-   Si l’on demande la valeur du pointeur AVEC le signe `*` on obtient en fait LA VALEUR de la variable pointée.

### Notes pratiques

On peut écrire indifféremment `int *adresseDeMaVariable` ou `int* adresseDeMaVariable`

---

La notation d’un pointeur en C se fait en deux parties :

1. Le signe `*`.
2. Le nom de la variable qui contient l’adresse pointée.

Dans mon exemple ci-dessus, cela donne : `*adresseDeMaVariable`.

Donc pour ne pas se mélanger les pinceaux, il vaut mieux éviter d’écrire : ~~`*pointeurVersMaVariable`~~, car le pointeur est composée des deux parties (le signe `*` et l’adresse).

---

! La syntaxe du C n’est pas cohérente, car suivant le contexte, le signe `*` aura une signification différente :

-   quand on spécifie qu’une fonction accepte un pointeur en paramètre, on utilise le signe `*`, alors que ce qui est transmis est l’adresse et pas la valeur.
-   quand on veut obtenir la valeur pointée (et pas l’adresse), on doit aussi utiliser le signe `*`.

<!--
 -->

## Pour la suite

Mon exemple de transmission de variable par référence pourrait ne pas utiliser de pointeur, mais la possibilité de retourner une valeur à la fin de la fonction avec le mot clé `return`. Cependant les `return` sont en général utilisés pour retourner le statut d’exécution de la fonction, autrement dit si elle a réussi à faire ce qu’on lui a demandé ou pas.

Et les `return` ont une limitation particulièrement ennuyeuse qui nous obligera de toute façon à utiliser les pointeurs : ils ne peuvent pas transmettre de tableaux. Et comme les tableaux sont omniprésents en programmation, on va donc également utiliser abondamment les pointeurs. Mais ça fera l’objet d’un autre article.

## Note pour les pros

> Si vous savez utiliser le terminal et que vous avez `gcc` installé sur votre ordi, vous pouvez tester les exemples de cette page avec les commandes :
> `FILENAME=... # Nom du fichier .c sans l’extension` > `gcc $FILENAME.c -o $FILENAME && ./$FILENAME`

## Utilisation des pointeurs pour les tableaux

Quand j’aurai le temps, j’écrirai un article sur ce sujet. Pour l’instant voici quelques exemples que j’ai posté sur StackExchange :

<http://arduino.stackexchange.com/a/31417/13995>

[1]: https://openclassrooms.com/courses/apprenez-a-programmer-en-c
[2]: https://openclassrooms.com/membres/mateo21

<!--
http://exercices.openclassrooms.com/assessment/123?login=6871762&tk=685884fbcf7ec3f75ae6234f11dbce5b&sbd=2016-02-01&sbdtk=2466d6bae51e373d89ac8e3f74213199
-->
