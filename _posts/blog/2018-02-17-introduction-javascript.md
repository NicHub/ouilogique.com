---
lang: fr
layout: page
title: "Introduction au langage JavaScript"
tags: []
image:
    feature:
date: 2018-02-17T12:00:00+01:00
published: true
author: Nico
---



Ce document fait partie du [cours sur le HTML embarqué][Wiki du cours HTML embarqué] que j’ai donné au [Microclub][Microclub] en janvier et février 2018 à l’EPFL.



## LES DOCUMENTS DU COURS

- [Introduction au langage HTML][Introduction au langage HTML]
- [Introduction au langage CSS][Introduction au langage CSS]
- [Introduction au langage JavaScript][Introduction au langage JavaScript]
- [Cours complet au format PDF][microclub-atelier-html-embarque.pdf]




## INTRODUCTION

Nous avons vu que le langage HTML permet de définir la structure du contenu d’un document et que le langage CSS permet de mettre en forme ce contenu. Nous allons maintenant voir comment utiliser le langage JavaScript pour rendre ce contenu interactif.



## L’ORIGINE DU NOM JAVASCRIPT

JavaScript aurait dû s’appeler LiveScript, mais a été renommé par une décision marketing dans le but de capitaliser sur la popularité du langage Java de Sun Microsystems, malgré le fait qu’ils n’aient que très peu en commun. Cela a toujours été une grande source de confusion.

JavaScript est normalisé par l’Ecma International (curieusement en Europe) sous la norme ECMA-262 et sous le nom de langage ECMAScript. Les noms ECMAScript et JavaScript sont donc souvent considérés comme interchangeables. Cependant, il faut noter que d’autres langages suivent aussi la norme ECMA-262, comme Flash 5 ActionScript d’Adobe ou JScript de Microsoft.

### Pour en savoir plus

- [Differences from ECMA-262 and JavaScript][Differences from ECMA-262 and JavaScript]



## UTILISATION DE JAVASCRIPT

JavaScript est principalement utilisé dans les navigateurs web, mais on le trouve aussi dans d’autres environnements tels que Node.js, Apache CouchDB voire Adobe Acrobat.

JavaScript permet d’automatiser certaines tâches qui rendront les pages web interactives. Dans le contexte de ce cours, l’utilisation de JavaScript sera limitée aux applications dans des navigateurs web utilisés par des humains.

Exemples d’utilisation :

- Effets visuels animés.
- Vérification des données entrées par un utilisateur.
- Communication automatique avec des appareils IoT.
- ...

### Pour en savoir plus

- [JavaScript sur MDN][JavaScript sur MDN]
- [Une réintroduction à JavaScript sur MDN][Une réintroduction à JavaScript sur MDN]



## VERSIONS

Curieusement, il est difficile de déterminer la version JavaScript utilisée par les navigateurs web. Chose incroyable, le langage n’offre pas de moyen d’obtenir cette information par programmation. On trouve des *hacks* sur internet, mais aucune solution officielle.

En utilisant [un de ces *hacks*][jsfiddle JS version], j’ai trouvé les résultats suivants (6 janvier 2018) :

| JS   | Navigateur                       | OS    |
| :--- | :---                             | :---  |
| 1.3  | Internet Explorer 11.125.16299.0 | Win10 |
| 1.5  | Microsoft Edge 41.16299.15.0     | Win10 |
| 1.5  | Firefox 57.0.4 (64 bits)         | Win10 |
| 1.5  | Firefox 57.0.4 (64 bits)         | macOS |
| 1.7  | Chrome 63.0.3239.132 (64 bits)   | Win10 |
| 1.7  | Chrome 63.0.3239.132 (64 bits)   | macOS |
| 1.7  | Opera 50.0.2762.45               | macOS |
| 1.7  | Opera Neon 1.0.2531.0 (64-bit)   | macOS |
| 1.7  | Safari 11.0.2                    | macOS |

On voit dans la table ci-dessus que la majorité des navigateurs modernes utilisent la version 1.7 de JavaScript. Firefox et Edge utilisent la version 1.5 et Internet Explorer est à la traîne avec la version 1.3. Ces résultats sont surprenants, parce que si on en croit [la table de correspondance du site W3Schools (au bas de la page)][JavaScript Versions sur W3Schools], ces versions sont très vieilles (informatiquement parlant) :

| JS    | ECMA  | Année |
| :---: | :---: | :---: |
| 1.3   | 1     | 1998  |
| 1.5   | 3     | 2000  |
| 1.7   | 3     | 2006  |



## POSITION DES SCRIPTS

À l’instar des feuilles de style CSS, le code JavaScript peut être défini dans 3 endroits différents :

1. Dans un ou plusieurs fichiers externes.
2. Dans une ou plusieurs balises `<script>` qui peuvent se trouver dans la balise `<head>` ou dans la balise `<body>`.
3. Dans certains attributs de certains éléments HTML, comme `<body onload>` ou `<img onerror>`.

### JS externe au fichier HTML

Les avantages de placer le code JS dans un ou plusieurs fichiers externes sont les mêmes que pour les fichiers CSS, c’est-à-dire que les informations ne seront téléchargées qu’une fois et mises en cache par les agents utilisateurs. De plus, plusieurs fichiers peuvent être regroupés en un seul pour minimiser le nombre de requêtes HTTP.

Voici un exemple de fichier JS :

```js
"use strict";
function main(source)
{
    var now = new Date();
    console.log("Début du script " + now.getTime() +
                "\nsource = " + source);
}
main("index.js");
```

Pour faire appel à ce script, il faut inclure la balise `<script>` ci-dessous dans le fichier HTML :

```html
<script src="index.js"></script>
```

Le plus souvent, on l’inclura juste avant la fermeture de la balise `</body>` car ceci a l’avantage de nous assurer que l’agent utilisateur a connaissance de toute la structure du fichier avant d’exécuter le script. Cependant, il est possible d’intégrer la balise `<script>` presque n’importe où dans le fichier et on la trouve souvent dans la balise `<head>`.

### JS interne au fichier HTML, dans la balise `<script>`

Les avantages de placer le code JS dans un fichier qui contient les instructions JS et HTML sont les mêmes que pour le CSS ([s’y référer pour plus de détails][css-interne]).

Voici un exemple de balises `<script>` intégrées au fichier HTML. On peut observer que ces balises peuvent être placées indifféremment dans la section `head` ou `body` et que la variable `now` et la fonction `main` définies dans le premier script sont globales et peuvent donc être réutilisées dans les scripts suivants.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset=utf-8 />
        <title>JS dans balise script</title>
        <script>
            "use strict";
            var now = new Date();
            function main(source)
            {
                console.log("fonction main " + now.getTime() +
                "\nsource = " + source);
            }
            main("head script");
        </script>
    </head>
    <body>
        <script>
            "use strict";
            main("body script");
        </script>
    </body>
</html>
```

De la même manière si une fonction ou une variable sont définies dans un fichier externe, on peut y accéder dans un script de la page HTML.

> On remarque également que c’est la même balise `<script>` qui est utilisée que le code JS soit externe ou interne à la page HTML. Par contraste, CSS utilise la balise `<style>` pour le code interne et la balise `<link>` pour le code externe.

### JS interne au fichier HTML, dans les attributs d’un élément HTML

Certains éléments HTML possèdent des attributs qui acceptent du code JavaScript. Par exemple, dans le code ci-dessous, on voit que les éléments `<html>` et `<body>` ont respectivement leurs attributs `onclick` et `onload` qui contiennent du code JavaScript.

- `html onclick` ⇒ est exécuté lorsque l’élément `<html>` est cliqué.
- `body onload` ⇒ est exécuté lorsque l’élément `<body>` est chargé.

On voit aussi qu’un script externe est appelé (`<script src="index.js"></script>`) et que la fonction `main()` qui y est définie est utilisée par l’attribut `onload`.

De la même manière, la variable `cpt` définie dans le script à la fin de l’élément `<head>` peut être utilisée par le JS de l’attribut `onclick` car elle est globale. À priori, c’est une mauvaise idée de déclarer une variable globale après qu’elle soit utilisée comme dans cet exemple, mais l’évènement `onclick` ne sera disponible qu’une fois la page complètement chargée, donc dans ce cas, ça n’a pas d’incidence.

> À noter que le préfixe `javascript:` est optionnel, sauf lorsqu’on utilise du JavaScript dans un attribut `href`.

```html
<!DOCTYPE html>
<html onclick="javascript:
               'use strict';
               cpt += 1;
               console.log('html onclick ' + cpt);">
<head>
    <meta charset="utf-8" />
    <title>JS dans les attributs HTML</title>
    <script src="index.js"></script>
    <script>
        "use strict";
        var cpt = 0;
    </script>
</head>
<body onload="javascript:
              'use strict';
              main('body onload');">
</body>
</html>
```


## LES BASES DU LANGAGE

### Casse

Le langage JavaScript est sensible à la casse, ce qui veut dire que les majuscules et les minuscules ne sont pas équivalentes.

Par exemple :

```js
element = document.getElementById(id); // correct
ELEMENT = DOCUMENT.GETELEMENTBYID(ID); // incorrect
```

### Fin d’instructions

Les instructions sont terminées par le caractère `;`. Les navigateurs sont souvent assez souples et tolèrent son ommission. Attendez-vous à de méchants bugs cependant, donc mieux vaut indiquer systématiquement le caractère `;`.

### La directive `use strict`

```js
"use strict";
```

La directive `"use strict";` se place au début d’un script et indique qu’il doit être exécuté en mode “strict” qui permet au navigateur d’exécuter le script plus rapidement. Avec `"use strict";`, la déclaration des variables est obligatoire comme nous allons le voir ci-dessous.

Pour les détails voir : [le mode scrict (MDN, fr)][le mode scrict (MDN, fr)].

### Déclaration des variables

Lorsqu’on utilise le mode strict, les variables doivent être déclarées et ceci ce fait généralement avec le mot clé `var`.

```js
console.log( a ); // Uncaught ReferenceError: a is not defined
var a;            // Déclaration de la variable a
console.log( a ); // a = Undefined
a = 3.14;
console.log( a ); // a = 3.14
```

On peut aussi déclarer les variables avec `let` et `const`.
La portée de `let` est plus réduite que celle de `var`.
`const` n’est pas supporté par tous les agents utilisateurs, pour l’instant je vous conseille d’éviter de l’utiliser.
La plupart du temps, c’est le mot clé `var` que l’on utilisera.

[Instruction let (MDN, fr)][Instruction let (MDN, fr)]

### Portée d’une variable

```js
var x = 1;        // x est global
console.log( "1. x = " + x ); // x est disponible à l’extérieur de la fonction

function portée() {
    console.log( "3. x = " + x ); // x est disponible à l’intérieur de la fonction
    x = 1111;
    var y = 10;
    console.log( "4. y = " + y );
}

console.log( "2. x = " + x ); // x est disponible à l’intérieur de la fonction
portée();
console.log( "5. x = " + x ); // x est disponible à l’intérieur de la fonction
console.log( "6. y = " + y ); // x est disponible à l’intérieur de la fonction

// Les variables définies dans la fonction ne sont plus accessibles à l’extérieur.
```

### Modification d’une variable avec des opérateurs arithmétiques

```js
var i = 0;
i += 2;
console.log( i ); // 2
i -= 20;
console.log( i ); // -18
i *= 2;
console.log( i ); // -36
i /= 5;
console.log( i ); // -7.2
i %= 5;
console.log( i ); // -2.2
i++
console.log( i ); // -1.2
++i
console.log( i ); // -0.2
i--
console.log( i ); // -1.2
--i
console.log( i ); // -2.2
```

Pour la division entière, voir <http://stackoverflow.com/a/17218003/3057377>

### Test `if-then-else`

```js
/*
La structure “if-then-else” emprunte la syntaxe du C.
Si une condition ne comporte qu’une expression, les accolades sont optionnelles.
*/

if( true )
    console.log( "C’est vrai" );
else
    console.log( "C’est faux" );

/*
Si une condition comporte plusieurs expressions, les accolades sont obligatoires.
*/
if( false )
    console.log( "C’est vrai" );
else
{
    console.log( "C’est..." );
    console.log( "..faux" );
}
```

### Comparaison faible vs stricte

```js
/*
Comparaison faible vs stricte
== ⇒ Comparaison “faible” ⇒ pas de vérification du type
=== ⇒ Comparaison “stricte” ⇒ avec vérification du type
https://developer.mozilla.org/fr/docs/Web/JavaScript/Les_diff%C3%A9rents_tests_d_%C3%A9galit%C3%A9
*/

var a = 6;
var b = '6';

// la variable “a” contient le nombre 6 sous forme d’un nombre.
// La variable “b” contient le nombre 6 sous forme d’une chaîne de caractères (string).
// avec l’opérateur ==, les deux variables sont égales.
if( a == b )
    console.log( "== OK" );
else
    console.log( "== NOT OK" );

// ===
// avec l’opérateur ===, les deux variables ne sont pas égales car
// elles n’ont pas le même type.
if( a === b )
    console.log( "=== OK" );
else
    console.log( "=== NOT OK" );
```

### Boucle `while`

```js

// La structure “while” emprunte la syntaxe du C.
// Si elle ne comporte qu’une expression, les accolades sont optionnelles.
var compteur = 0;
while( compteur < 10 )
    console.log( "compteur = ", compteur++ );

// Attention, la variable “compteur” est définie en dehors de la boucle,
// donc la boucle suivante ne sera jamais exécutée, car “compteur == 10”
// à cet endroit du code.
while( compteur < 10 )
    console.log( "compteur = ", compteur++ );

// Si on veut isoler la variable compteur, on peut créer un bloc
{
    let compteur = 0;
    while( compteur < 5 )
        console.log( "compteur = ", compteur++ );
};

// Ici “compteur” vaut 10. Les modifications apportées à la variables déclarée
// avec “let” dans le bloc ne sont pas visbles à l’extérieur du bloc.
console.log( "compteur (après bloc) = ", compteur );
```

### Quitter une boucle avec `break`

```js
// On peut quitter une boucle “while” avec un “break”
compteur = 0;
while( compteur < 10 )
{
    console.log( "compteur = ", compteur++ );
    if( compteur > 5 ) break;
}
```

### La boucle `do...while`

```js
compteur = 0;
do
    console.log( "compteur = ", compteur++ );
while( compteur < 10 )
```

### Incrémentation

```js
// POST INCRÉMENTATION “X++”
// Si l’opérateur est utilisé en suffixe (par exemple : x++),
// il renvoie la valeur avant l’incrémentation.
compteur = 0;
while( compteur < 10 )
    console.log( "compteur = ", compteur++ );

// PRÉ INCRÉMENTATION “++X”
// Si l’opérateur est utilisé en préfixe (par exemple : ++x),
// il renvoie la valeur après l’incrémentation.
compteur = 0;
while( compteur < 10 )
    console.log( "compteur = ", ++compteur );

// Ça marche aussi pour la décrémentation “--”
// plus de détails ici :
// https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Op%C3%A9rateurs_arithm%C3%A9tiques
```

### La boucle `for`

```js
// BOUCLE “FOR” AVEC VAR
for( var cpt=1; cpt<=5; cpt++ ) // “++cpt” ou “cpt++” sont équivalents ici.
    console.log( "cpt = ", cpt );

// ATTENTION LA VARIABLE “CPT” EST AUSSI DÉFINIE EN DEHORS DE LA BOUCLE “FOR”
console.log( "cpt = ", cpt );

// Si on ne veut pas que la varible de compteur soit définie en dehors
// de la boucle “for”, il faut la déclarer avec “let”.
console.log( "\n\n\n# BOUCLE “FOR” AVEC LET" );
for( let cptLet=1; cptLet<=5; cptLet++ )
    console.log( "cptLet = ", cptLet );
// Ici, “cptLet” n’est plus défini.

console.log( "\n\n\n# BOUCLE “FOR” INFINIE" );
for( ;; )
{
    break;
}
```

### Les fonctions

```js
console.log( "\n\n\n# APPEL DE FONCTIONS" );

// On peut appeler une fonction avant qu’elle ne soit définie dans le fichier.
direBonjour();
function direBonjour()
{
    console.log( "Bonjour 1 !" );
}
direBonjour();
```

### Valeur de sortie des fonctions et portée des variables

```js
// Une fonction ne peut retourner qu’une seule valeur
// les variables définies dans les fonctions ne sont pas visibles à l’extérieur
function direBonjour2()
{
    var message = "Bonjour 2 !" // “message” n’est défini que dans la fonction et pas à l’extérieur.
    return message;
}
var resultat = direBonjour2();
console.log( resultat );
console.log( typeof( message ) ); // typeof( message ) = undefined
```

### Paramètres des fonctions

```js
function direBonjour( prenom1, prenom2 )
{
    var message = "Bonjour, " + prenom1 + " et " + prenom2 + " !";
    return message;
}
console.log( direBonjour( "Baptiste" ) );
console.log( direBonjour( "Baptiste", "Sophie" ) );
console.log( direBonjour( "Baptiste", "Sophie", "Toto" ) );
```


### Les chaînes de caractères (*string*)

```js
console.log( "\n\n\n# LES CHAÎNES DE CARACTÈRES (STRING)" );

/*
En Javascript il n’y a pas de différence entre
les guillemets simples et les guillemets doubles
*/
console.log( 'guillemets simples ' );
console.log( "guillemets doubles " );
console.log( '"guillemets" \'simples\' ' );
console.log( "'guillemets' \"doubles\" " );
```


> Attention en JSON, seuls les guillemets doubles sont valables !

> Il existe une nouvelle fonctionnalité appelée “Littéraux de gabarits”
qui utilise le caractère “`” (backticks ou accent grave) comme délimiteur.
Cette fonctionnalité est récente et n’est pas acceptée universellement.


### Concaténation de chaînes de caractères

```js
console.log( "Bonjour " + "à vous !" );
console.log( "Le chiffre vaut " + 7 );
```


## LES LIBRAIRIES

- <https://www.jqwidgets.com/>
- <http://dashing.io/>





[JavaScript sur MDN]: https://developer.mozilla.org/fr/docs/Web/JavaScript

[Une réintroduction à JavaScript sur MDN]: https://developer.mozilla.org/fr/docs/Web/JavaScript/Une_r%C3%A9introduction_%C3%A0_JavaScript

[Differences from ECMA-262 and JavaScript]: https://docstore.mik.ua/orelly/web2/action/appd_01.htm

[JavaScript Versions sur W3Schools]: https://www.w3schools.com/js/js_versions.asp

[jsfiddle JS version]: http://jsfiddle.net/Ac6CT/

[Wiki du cours HTML embarqué]: https://github.com/NicHub/microclub-atelier-html-embarque/wiki

[css-interne]: https://github.com/NicHub/microclub-atelier-html-embarque/wiki/cours-1-css#css-interne-au-fichier-html-dans-la-balise-style

[le mode scrict (MDN, fr)]: https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Strict_mode

[Instruction let (MDN, fr)]: https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/let

[Microclub]: https://microclub.ch/

[microclub-atelier-html-embarque.pdf]:  ../../files/2018-02-17-html-embarque/microclub-atelier-html-embarque.pdf

[Introduction au langage HTML]: ../introduction-html/

[Introduction au langage CSS]: ../introduction-css/

[Introduction au langage JavaScript]: ../introduction-javascript/
