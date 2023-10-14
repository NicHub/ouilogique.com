---
author: Nico
date: 2018-02-16 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Introduction au langage CSS
---

Ce document fait partie du [cours sur le HTML embarqué][Wiki du cours HTML embarqué] que j’ai donné au [Microclub][Microclub] en janvier et février 2018 à l’EPFL.

## LES DOCUMENTS DU COURS

-   [Introduction au langage HTML][Introduction au langage HTML]
-   [Introduction au langage CSS][Introduction au langage CSS]
-   [Introduction au langage JavaScript][Introduction au langage JavaScript]
-   [Cours complet au format PDF][microclub-atelier-html-embarque.pdf]

## INTRODUCTION

Nous avons vu que le langage HTML permet de définir la structure du contenu d’un document. Nous allons maintenant voir comment mettre en forme l’apparence de ce contenu grâce au langage CSS.

CSS signifie _Cascading Style Sheets_, c’est à dire _Feuilles de style en cascade_. CSS fait appel à des sélecteurs qui permettent d’appliquer les styles aux différents éléments HTML.

### Note

Il n’y a pas que les documents HTML qui peuvent profiter de la mise en forme avec CSS, les documents SVG (_Scalable Vector Graphics_ ou graphique vectoriel adaptable, en français) le peuvent aussi.

### Pour en savoir plus

-   [CSS sur MDN][CSS sur MDN]

## BÉNÉFICES DE LA TECHNOLOGIE CSS

Une des grandes forces de la technologie CSS est d’offrir la possibilité de mettre en forme un document de façons complètement différentes en adaptant uniquement les feuilles de style, mais sans modifier le document HTML source.

Ce cours lui-même est un exemple de cette possibilité offerte par CSS. Il y a plusieurs scénarios de transformation possibles et chacun à son CSS associé :

### Exemple avec ce cours

**Prérequis**

-   Rédaction des documents au format Markdown.

**Scénario 1 : Génération avec GitHub**

-   Lors de la mise en ligne, GitHub convertit automatiquement les fichiers Markdown en HTML et affiche le résultat sur leur site en utilisant leur propre CSS.

**Scénario 2 : Génération avec Pandoc**

-   J’utilise [Pandoc][Pandoc] pour convertir les fichiers Markdown en HTML et j’inclus dans le fichier HTML la feuille de style CSS qui permet de lire [ce fichier][Ce cours au format HTML] dans un navigateur.

**Scénario 3 : Génération avec Prince**

-   J’utilise [Prince][Prince] pour convertir le fichier HTML du scénario 2 en format PDF. La feuille de style est également la même, mais elle contient des instructions qui permettent de différencier le rendu à l’écran et le rendu au format PDF.

**Conclusion**

On voit que les trois scénarios utilisent des CSS différents et qu’un fichier source peut générer différents fichiers cibles.

### EXEMPLE AVEC _CSS ZEN GARDEN_

Un exemple spectaculaire de la puissance de la technologie CSS est le site [_CSS Zen Garden_][CSS Zen Garden]. Le défi proposé par ce site est que tous les participants mettent en forme le même fichier HTML et le résultat visuel doit être aussi original que possible. Je vous laisse juger de l’inventivité des participants ainsi que de la puissance de la technologie CSS.

## POSITION DU CSS

Les instructions CSS peuvent être définies dans 3 endroits différents :

1. Dans un ou plusieurs fichiers externes.
2. À l’intérieur du fichier HTML, dans la balise `<style>` qui doit se trouver elle-même dans la balise `<head>`.
3. Dans l’attribut `style` d’un élément HTML.

### CSS externe au fichier HTML

L’avantage du fichier CSS externe est qu’il permet de réunir toutes les informations de style en un seul fichier qui pourra être utilisé par toutes les pages HTML d’un site, aussi grand soit-il. Ceci permet de minimiser la bande passante et d’accélérer le rendu puisque les agents utilisateurs peuvent garder la feuille de style en cache.

Avec des fichiers CSS externes, il est également plus facile de gérer des scénarios de transformation différents.

Voici un exemple de fichier CSS (style.css) :

<!-- prettier-ignore-start -->
```css
p {
    color: firebrick;
}
```
<!-- prettier-ignore-end -->

Pour faire appel à ce fichier, il faut inclure la balise `<link>` dans le document HTML, généralement à l’intérieur de la balise `<head>`, mais la norme HTML 5 permet de positionner cette balise dans l’élément `<body>` également.

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>CSS</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <p>Hello Microclub !</p>
</body>
</html>
```
<!-- prettier-ignore-end -->

### CSS interne au fichier HTML, dans la balise `<style>`

Si on désire ne servir qu’un seul fichier qui contient à la fois les instructions HTML et CSS, comme c’est souvent le cas dans le monde de l’IoT, il est possible de placer les instructions CSS dans une ou plusieurs balises `<style>` qui doivent se trouver dans la balise `<head>` du fichier HTML.

On peut aussi utiliser cette méthode pour créer des exceptions pour une page donnée dans un site web contenant plusieurs pages.

C’est aussi un moyen de forcer les agents utilisateurs à ne pas réutiliser les informations de leur cache.

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>CSS</title>
    <style>
    p {
    color: aqua;
    }
    </style>
</head>
<body>
    <p>Hello Microclub !</p>
</body>
</html>
```
<!-- prettier-ignore-end -->

### CSS interne au fichier HTML, dans l’attribut `style` d’un élément HTML

Cette méthode est analogue à celle que l’on utiliserait dans un logiciel de traitement de texte, c’est-à-dire que l’on applique le style directement à l’élément concerné.

Elle doit être utilisée le moins souvent possible, car elle augmente considérablement la taille des fichiers et diminue la lisibilité. Google pénalise aussi cette pratique lors de l’indexation si on en croit leur outil [PageSpeed Insights][Google Insights].

Elle a également le désavantage d’empêcher la gestion de scénarios de transformation.

Cela dit, c’est un bon moyen de créer une exception pour un élément donné.

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>CSS</title>
</head>
<body>
    <p style="color: blueviolet">Hello Microclub !</p>
</body>
</html>
```
<!-- prettier-ignore-end -->

## LA SYNTAXE

Pour apprendre les bases de la syntaxe CSS, nous allons utiliser l’exemple ci-dessous ([adapté de l’exemple sur MDN][syntaxe CSS MDN]{:rel="nofollow"}).

fichier `syntaxe.css`

<!-- prettier-ignore-start -->
```css
body {
    font: 1em/150% "Helvetica Neue", Arial, monospace;
    padding: 1em;
    margin: 20px auto;
    max-width: 33em;
}

@media (min-width: 768px) {
    body {
    border: 1px solid chocolate;
    }
}

h1 {
    font-size: 1.5em;
}

div p, #id:first-line {
    background-color: antiquewhite;
    color: cadetblue;
}

div p {
    margin: 0;
    padding: 1em;
}

div p + p {
    padding-top: 0;
}
```
<!-- prettier-ignore-end -->

fichier `syntaxe.html`

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Syntaxe CSS</title>
    <link rel="stylesheet" href="syntaxe.css" />
</head>
<body>
    <h1>Un exemple simple</h1>

    <p id="id">Lorem ipsum dolor sit amet, consectetur adipiscing elit.
       Nulla eget sapien volutpat, blandit tortor sit amet, consequat
       sem. Mauris suscipit nunc eu mi lobortis, in porttitor nulla
       tempor. Suspendisse ante erat, eleifend auctor dictum in,
       viverra eu elit.</p>

    <div>
      <p>Nullam sit amet augue consequat, tristique enim non, varius
         orci. Vivamus bibendum elit turpis, sit amet fringilla neque
         mollis sed. Donec semper, nibh molestie maximus pretium, tellus
         nibh molestie leo, vitae vulputate ante turpis a eros.</p>

      <p>Vestibulum pharetra metus id quam dignissim, ac maximus libero
         efficitur. Nullam hendrerit diam nisl. Nullam feugiat semper
         ipsum a pharetra. Ut posuere varius consectetur. Sed purus nunc,
         fringilla laoreet risus vitae, laoreet dapibus diam.</p>
    </div>
</body>
</html>
```
<!-- prettier-ignore-end -->

### Anatomie d’une règle CSS

Une règle CSS se présente sous la forme suivante :

<!-- prettier-ignore-start -->
```css
sélecteur1, sélecteur2 {
    propriété1: valeur1;
    propriété2: valeur2;
}
```
<!-- prettier-ignore-end -->

Voici un exemple réel de règle :

<!-- prettier-ignore-start -->
```css
div p, #id:first-line {
    background-color: antiquewhite;
    color: cadetblue;
}
```
<!-- prettier-ignore-end -->

On voit qu’une règle est composée de la manière suivante :

-   Un ou plusieurs **sélecteurs** séparés par des virgules, ici `div p` et `#id:first-line`.
-   Un bloc délimité par des accolades `{}`.
-   Un **bloc** peut être vide ou contenir une ou plusieurs **déclarations**, ici `background-color: antiquewhite;` et `color: cadetblue;`.
-   Les blocs peuvent être imbriqués.
-   Chaque déclaration est constituée de **propriétés** et de **valeurs** séparées du caractère deux points (`:`).
-   Les déclarations sont terminées par un point-virgule.
-   Le point-virgule est optionnel (mais recommandé) pour la dernière déclaration d’un bloc.
-   Les déclarations peuvent être mises sur une ou plusieurs lignes.

> **Les instructions CSS sont sensibles à la casse (majuscule ≠ minuscule).**
> En CSS, il n’est pas possible de définir des variables ou des constantes, ce qui est très problématique pour gérer des projets complexes. Dans ce cas, on utilisera un langage de génération de feuilles de style comme [Sass][Sass].
> Si une règle est invalide, elle est ignorée.

### Commentaires

Il est possible de commenter le code CSS de la manière suivante :

<!-- prettier-ignore-start -->
```css
body {
    font: 1em/150% "Helvetica Neue", Arial, monospace;
    padding: 1em;
    /*
    Ceci est un commentaire.
    Les instructions ci-dessous
    ne seront pas exécutées
    car elles sont commentées.
    */
    /*
    margin: 20px auto;
    max-width: 33em;
    */
}
```
<!-- prettier-ignore-end -->

> CSS ne permet pas de commenter ligne par ligne, comme il est possible de le faire en JavaScript avec les symboles `//`.

> On ne peut pas commenter une portion de code qui contient elle-même des commentaires. Ceci est très contraignant et il convient donc d’être très prudent quand on commente une grande portion de code. Si des commentaires étaient déjà présents, le code ne sera plus valide !

### Validation

Pour s’assurer qu’un code CSS est valide, on peut utiliser [le validateur CSS du W3C][W3C CSS Validator].

### Pour en savoir plus

-   [Les déclarations CSS MDN][Les déclarations CSS MDN]{:rel="nofollow"}
-   [Les blocs CSS MDN][Les blocs CSS MDN]{:rel="nofollow"}
-   [Les règles CSS MDN][Les règles CSS MDN]{:rel="nofollow"}

### Les instructions CSS

[Les instructions CSS MDN][Les instructions CSS MDN]{:rel="nofollow"}

## LES SÉLECTEURS

En CSS, les sélecteurs sont utilisés afin de cibler une partie spécifique d’une page web à mettre en forme. Afin de pouvoir être précis, CSS est très riche en sélecteurs et une grande partie de sa flexibilité dépend de ceux-ci.

-   Les sélecteurs simples
    -   Les sélecteurs de type (type selectors)
    -   Les sélecteurs de classe
    -   Les sélecteurs d’identifiant
    -   Le sélecteur universel
-   Les sélecteurs d’attribut
    -   Définition et valeur des sélecteurs d’attribut
    -   Les sélecteurs d’attribut utilisant un filtre sur les fragments de chaînes
-   Les pseudo-classes
-   Les pseudo-éléments
-   Les combinateurs

Pour découvrir les sélecteurs, rendez-vous sur la page [des sélecteurs de MDN][Les sélecteurs MDN]{:rel="nofollow"}.

## LA CASCADE

Comme son nom l’indique, CSS agit en cascade, ce qui signifie que les définitions de style sont lues les unes après les autres et que si deux règles sont identiques, c’est la dernière qui sera appliquée.

Dans l’exemple ci-dessous, la couleur du texte à l’intérieur des balises `<p>` est définie 3 fois. Pour être exhaustif, il faut aussi mentionner que les agents utilisateurs appliquent eux aussi des styles par défaut et qu’ils peuvent permettre aux utilisateurs de créer leurs propres styles. Donc, l’agent utilisateur lira les 5 sources suivantes et dans cet ordre :

1. Style par défaut de l’agent utilisateur ⇒ _black_
2. Utilisateur de l’agent utilisateur ⇒ _not set_
3. Fichier externe (style.css) ⇒ _firebrick_
4. Balise `<style>` ⇒ _aqua_
5. Attribut `style` de l’élément `<p>` ⇒ _blueviolet_

Les règles de cascade imposent que, si des règles sont en concurrence, ce soit la dernière qui est appliquée. Donc dans l’exemple ci-dessous, la couleur du texte sera _blueviolet_.

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>CSS</title>

    <!-- Lorsque l’agent utilisateur arrive ici,
    il a déjà chargé ses styles par défaut ainsi
    que les styles personnels de l’utilisateur. -->

    <!-- Ici l’agent utilisateur charge le fichier
    style.css -->
    <link rel="stylesheet" href="style.css" />

    <!-- Ici l’agent utilisateur charge les styles
    déclarés dans la balise “style” -->
    <style>
        p {
            color: aqua;
        }
    </style>
</head>
<body>
    <!-- Ici l’agent utilisateur applique le style
    indiqué dans l’attribut “style” -->
    <p style="color: blueviolet">Hello Microclub !</p>
</body>
</html>
```
<!-- prettier-ignore-end -->

## LA PONDÉRATION

Les règles de la cascade s’appliquent pour prioriser les différentes sources. Que se passe-t-il si, pour une même source, plusieurs règles concernent le même élément ? Dans ce cas, pour prioriser les règles, on prendra en compte le poids du sélecteur. Le poids d’un sélecteur est calculé en fonction de sa spécificité :

1. **Niveau 1 (spécificité élevée)** : Sélecteur d’identifiant
2. **Niveau 2 (spécificité moyenne)** : Sélecteur de classe, de pseudo-classe et d’attribut
3. **Niveau 3 (spécificité faible)** : Sélecteur de type et de pseudo-element

Pour déterminer si une règle s’applique plutôt qu’une autre on regarde :

-   Celle qui possède le plus de sélecteurs de niveau 1.
-   Si le nombre de sélecteurs de niveau 1 est le même : celle qui possède le plus de sélecteurs de niveau 2.
-   Si le nombre de sélecteurs de niveau 2 est le même : celle qui possède le plus de sélecteurs de niveau 3.
-   Enfin, si les sélecteurs ont le même poids, ce sera l’ordre des règles dans le fichier source qui importera : la règle la plus basse dans le fichier l’emportera sur une règle déclarée avant.

Prenons ce fragment de HTML par exemple :

<!-- prettier-ignore-start -->
```html
<p id="cookie" class="crispy">Ce cookie est <span>délicieux !</span></p>
```
<!-- prettier-ignore-end -->

Cette feuille de style illustre ce qui se passe lorsqu’un sélecteur de niveau 1 entre en conflit avec d’autres sélecteurs :

<!-- prettier-ignore-start -->
```css
/* Ce sélecteur est composé d’un sélecteur de niveau 1
   Poids : 1 | 0 | 0 */
#cookie {
  color: green;
}
/* Ce sélecteur n’a aucun sélecteur de niveau 1
   et 2 sélecteur de niveau 2
   Poids : 0 | 2 | 0 */
[id=cookie].crispy {
  color: red;
}

/* 1|0|0 > 0|2|0 : La première règle s’applique et le texte
   est vert. Un seul sélecteur de niveau 1 sera toujours
   prioritaire par rapport à X sélecteurs de niveau 2. */
```
<!-- prettier-ignore-end -->

### Pour en savoir plus

-   [Pondération MDN][Pondération MDN]{:rel="nofollow"}

## L’HÉRITAGE

[Héritage MDN][Héritage MDN]{:rel="nofollow"}

## LES _MEDIA QUERIES_

Les _media queries_, ou requêtes media en français, sont des instructions CSS qui permettent d’appliquer des règles CSS différentes en fonction de l’appareil utilisé et ceci sans modification du code HTML. Elles sont à la base de ce qu’on appelle le _responsive design_ ou design adaptatif en français et c’est ce qui permet à un site web de s’afficher lisiblement à la fois sur un écran de bureau 27" et sur l’écran d’un téléphone.

On peut spécifier le média cible à deux endroits différents :

Dans l’attribut `media` de la balise `<link>` qui appelle le code CSS :

<!-- prettier-ignore-start -->
```html
<link rel="stylesheet" media="screen" href="style-screen.css" />
<link rel="stylesheet" media="print" href="style-print.css" />
```
<!-- prettier-ignore-end -->

Ou dans le CSS lui-même :

<!-- prettier-ignore-start -->
```css
body
{
  background-color: lime;
}

@media (min-width: 700px)
{
  body
  {
    background-color: red;
  }
}

@media (min-width: 700px) and (orientation: landscape)
{
  body
  {
    background-color: lime;
  }
}
```
<!-- prettier-ignore-end -->

### Pour en savoir plus

-   [Les medias queries MDN][Les medias queries MDN]

## LES COULEURS

Les couleurs peuvent être définies de plusieurs façons différentes. Tous les exemples ci-dessous définissent la même couleur <span style="color: white; background-color:firebrick">firebrick</span>.

<!-- prettier-ignore-start -->
```css
/* Par nom : */
body { background-color: firebrick; }

/* Par code hexadecimal RGB : */
body { background-color: #B22222; }

/* Par code decimal RGB : */
body { background-color: rgb(178, 34, 34); }

/* Par code decimal RGB avec gestion de la transparence : */
body { background-color: rgba(178, 34, 34, 0.5); }

/* Par code decimal HSL : */
body { background-color: hsl(0, 68%, 42%); }

/* Par code decimal HSL avec gestion de la transparence : */
body { background-color: hsla(0, 68%, 42%, 0.5); }
```
<!-- prettier-ignore-end -->

### Notation courte

Il existe aussi une notation courte sur 3 chiffres au lieu de 6. Par exemple, `#B22` est équivalent à `#BB2222`, ce qui est très proche de `#B22222` de notre exemple ci-dessus.

<!-- prettier-ignore-start -->
```css
body { background-color: #B22; }
```
<!-- prettier-ignore-end -->

### Nombre de couleurs

La notation standard sur 6 chiffres permet d’afficher 16<sup>6</sup> = 256<sup>3</sup> = 16’777’216 de couleurs, alors que la notation sur 3 chiffres n’en offre que 16<sup>3</sup> = 4’096.

### Pour en savoir plus

-   [HTML Color Picker W3 Schools][HTML Color Picker W3 Schools]
-   [Couleurs CSS MDN][Couleurs CSS MDN]

## FRAMEWORKS

Mettre en forme des pages HTML peut vite devenir une tâche complexe, particulièrement quand on veut l’afficher sur des écrans de tailles très différentes. Pour cela, il est fortement conseillé de ne pas réinventer la roue et d’utiliser un _framework_, c’est-à-dire une collection d’outils prête à l’emploi.

Dans le monde du CSS, le _framework_ [Bootstrap][Bootstrap] est très populaire en ce moment. Il est basé sur un système de grille à 12 colonnes qui sont utilisées pour l’alignement des éléments visuels.

Un désavantage de Bootstrap est que le fichier CSS de base (bootstrap.min.css) pèse 118 ko, ce qui est relativement conséquent quand on veut travailler avec un [ESP8266][ouilogique ESP8266 WeMos]. Mais j’ai essayé et ça fonctionne. Si la topologie du projet le permet, il est de toute façon préférable de charger Bootstrap depuis un CDN et pas depuis le site web ou l’appareil IoT de l’application en utilisant le code suivant :

<!-- prettier-ignore-start -->
```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
```
<!-- prettier-ignore-end -->

Voici un canevas pour bien commencer avec Bootstrap. Il est assez complet, donc dans la plupart des cas, il conviendra d’enlever les éléments inutilisés.

<!-- prettier-ignore-start -->
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <title></title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous" />
  <style type="text/css">
    @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,200i,400');
    body {
      font-family: 'Source Sans Pro', monospace;
      font-size: 14pt;
      margin: 2em;
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-xs-12 col-xs-offset-0">
        <h1>Bootstrap starter template</h1>
        <p></p>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.6.4.slim.min.js" integrity="sha256-a2yjHM4jnF9f54xUQakjZGaqYs/V1CYvWpoqZzC2/Bw=" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
```
<!-- prettier-ignore-end -->

Il existe d’autres _frameworks_, comme [Foundation][Foundation] qui est aussi très populaire.

### Pour en savoir plus

-   [Site officiel de Bootstrap, en][Bootstrap]
-   [Site officiel de Foundation, en][Foundation]

## POUR LA SUITE

Avec cette introduction sur la technologie CSS, vous avez maintenant une base pour comprendre comment mettre en forme une page HTML simple.

Si vous désirez approfondir vos connaissances, vous pouvez lire [l’article “Composer le HTML avec les CSS”][Composer le HTML avec les CSS].

Pour vous aider lors de l’écriture de vos feuilles de style, vous trouverez une liste exhaustive des mots-clés de la syntaxe CSS ici : [Référence CSS MDN][Référence CSS MDN].

Le site du W3C contient lui aussi beaucoup d’informations utiles : [CSS sur le site du W3C][CSS W3C].

[Foundation]: https://foundation.zurb.com/
[Bootstrap]: https://getbootstrap.com/
[CSS W3C]: https://www.w3.org/Style/CSS/Overview.fr.html
[CSS sur MDN]: https://developer.mozilla.org/fr/docs/Web/CSS
[Référence CSS MDN]: https://developer.mozilla.org/fr/docs/Web/CSS/Reference
[Composer le HTML avec les CSS]: https://developer.mozilla.org/fr/Apprendre/CSS
[Google Insights]: https://developers.google.com/speed/pagespeed/insights/?hl=fr
[syntaxe CSS MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_syntaxe
[Les déclarations CSS MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_syntaxe#Les_d%C3%A9clarations_CSS
[Les blocs CSS MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_syntaxe#Les_blocs_CSS
[Les règles CSS MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_syntaxe#Les_r%C3%A8gles_CSS
[Les instructions CSS MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_syntaxe#Les_r%C3%A8gles_CSS
[Sass]: http://sass-lang.com/
[W3C CSS Validator]: https://jigsaw.w3.org/css-validator/#validate_by_input
[Les sélecteurs MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/Les_s%C3%A9lecteurs
[Pondération MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_cascade_et_l_h%C3%A9ritage#Le_poids_des_s%C3%A9lecteurs
[Héritage MDN]: https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_%C3%A0_CSS/La_cascade_et_l_h%C3%A9ritage#L'h%C3%A9ritage
[ouilogique ESP8266 WeMos]: ../NodeMCU_esp8266/
[Wiki du cours HTML embarqué]: https://github.com/NicHub/microclub-atelier-html-embarque/wiki
[Les medias queries MDN]: https://developer.mozilla.org/fr/docs/Web/CSS/Requ%C3%AAtes_m%C3%A9dia/Utiliser_les_Media_queries
[HTML Color Picker W3 Schools]: https://www.w3schools.com/colors/colors_picker.asp?color=00bfff
[Couleurs CSS MDN]: https://developer.mozilla.org/fr/docs/Web/CSS/color
[Pandoc]: https://pandoc.org/
[Ce cours au format HTML]: https://raw.githubusercontent.com/wiki/NicHub/microclub-atelier-html-embarque/md2pdf/microclub-atelier-html-embarque.html
[Ce cours au format PDF]: https://raw.githubusercontent.com/wiki/NicHub/microclub-atelier-html-embarque/md2pdf/microclub-atelier-html-embarque.pdf
[Prince]: https://www.princexml.com/
[CSS Zen Garden]: http://www.csszengarden.com/
[Microclub]: https://microclub.ch/
[microclub-atelier-html-embarque.pdf]: https://raw.githubusercontent.com/wiki/NicHub/microclub-atelier-html-embarque/md2pdf/microclub-atelier-html-embarque.pdf
[Introduction au langage HTML]: ../introduction-html/
[Introduction au langage CSS]: ../introduction-css/
[Introduction au langage JavaScript]: ../introduction-javascript/
