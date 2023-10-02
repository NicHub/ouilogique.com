---
author: Nico
date: 2018-02-15 12:00:00+01:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: Introduction au langage HTML
---



Ce document fait partie du [cours sur le HTML embarqué][Wiki du cours HTML embarqué] que j’ai donné au [Microclub][Microclub] en janvier et février 2018 à l’EPFL.



## LES DOCUMENTS DU COURS

- [Introduction au langage HTML][Introduction au langage HTML]
- [Introduction au langage CSS][Introduction au langage CSS]
- [Introduction au langage JavaScript][Introduction au langage JavaScript]
- [Cours complet au format PDF][microclub-atelier-html-embarque.pdf]




## LES AGENTS UTILISATEURS

Dans le cadre de ce cours, un *agent utilisateur*, ou *user agent* en anglais, est un logiciel qui peut traiter des données conformes aux normes HTML, XHTML, CSS, JavaScript et JSON. Cette liste n’est pas exhaustive et différents agents utilisateurs offrent des possibilités plus étendues ou au contraire plus restreintes. Pour la suite, nous nous focaliserons sur la partie du traitement des fichiers HTML, CSS et JavaScript.

Dans la grande majorité des cas, l’agent utilisateur sera un navigateur web, ou *web browser* en anglais, mais il est intéressant de noter que d’autres possibilités existent :

- Les appareils IoT (*Internet of Things* ou Internet des objets).
- Les navigateurs braille pour les personnes malvoyantes.
- Les logiciels de mise en page comme [Prince XML][Prince XML].
- Les logiciels qui ne sont pas des navigateurs mais qui utilisent des données distantes. Par exemple les applications météo ou les horaires de transports publics.
- ...

### Pour en savoir plus

- [Agents utilisateurs (Wikipedia fr)][User agent]



## LA STRUCTURE MINIMALE D’UNE PAGE HTML

Voici la structure minimale pour qu’un document soit considéré comme un document HTML par tous les agents utilisateurs.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset=utf-8 />
        <title>Structure minimale</title>
    </head>
    <body>
    </body>
</html>
```

On voit dans cet exemple que le code HTML est composé de balises. Les balises absolument obligatoires pour qu’un document soit considéré comme un document HTML sont :

```html
1. <!DOCTYPE html>
2. <html></html>
3. <head></head>
4. <meta charset=utf-8 />
5. <title></title>
6. <body></body>
```

Nous aurons besoin d’autres balises pour étoffer nos documents HTML, mais les 6 ci-dessus doivent toujours être présentes.

Sans entrer dans les détails, voici à quoi servent ces premiers éléments :

**1. `<!DOCTYPE html>`**
Définit que le document suit la norme HTML 5.

**2. `<html></html>`**
Tout le document (à l’exception du doctype) est entouré des balises `<html>`.

**3. `<head></head>`**
Le contenu de l’élément `<head>` sert à donner des informations aux agents utilisateurs. Ces informations ne sont donc pas visibles directement par l’utilisateur, à l’exception du contenu de l’élément `<title>` et du favicon (pas déclaré dans cet exemple). Il est possible de générer dynamiquement ce contenu avec JavaScript.

**4. `<meta charset=utf-8 />`**
Cet élément `<meta>` indique au navigateur quel est l’encodage du fichier. Sans cette information, les navigateurs font des choix par défaut qui sont souvent différents de l’UTF-8 et donc les caractères ne s’afficheront pas correctement. Pour des raisons de performance, il est conseillé de placer cette balise en premier dans l’élément `<head>`.

**5. `<title></title>`**
Le contenu de l’élément `<title>` sera affiché dans l’onglet de la page dans le navigateur.

**6. `<body></body>`**
Et enfin, le contenu visible par l’utilisateur de la page est placé dans l’élément `<body>`. Il est possible de générer dynamiquement ce contenu avec JavaScript.



## LES ÉLÉMENTS ET LEURS BALISES

### Structure des éléments HTML

Un élément HTML est formé de balises, ou *tag* en anglais. Par exemple :

```html
<p></p>
```

Pour la balise ouvrante, la structure est :

- chevron ouvrant (`<`)
- le nom de la balise (dans l’exemple ci-dessus “`p`”)
- chevron fermant (`>`)

Pour la balise fermante, la structure est :

- chevron ouvrant (`<`)
- barre oblique (`/`)
- le nom de la balise (dans l’exemple ci-dessus “`p`”)
- chevron fermant (`>`)

Entre les balises, on peut inclure :

- rien : `<p></p>`
- du texte sans balises : `<p>du texte</p>`
- d’autres balises : `<p>du <i>texte</i></p>`
- d’autres balises imbriquées (*nested* en anglais) : `<p><b>du <i>texte</i></b></p>`

### Éléments HTML vides

Certains éléments HTML sont toujours vides, c’est-à-dire qu’ils n’ont jamais de contenu entre leur balise ouvrante et leur balise fermante. On les appelle “éléments vides” (*empty elements* ou *void elements* en anglais). Dans ce cas, il est obligatoire d’utiliser une notation compacte avec la barre oblique avant le chevron fermant, que l’on nomme “balise autofermante”.

Donc ceci est valide :

```html
<br /> <!-- Line break = retour à la ligne -->
<img /> <!-- Image -->
<meta /> <!-- Meta-donnée -->
<link /> <!-- lien vers une feuille CSS -->
```

Alors que ceci n’est pas valide :

```html
<br></br> <!-- Line break = retour à la ligne -->
<img></img> <!-- Image -->
<meta></meta> <!-- Meta-donnée -->
<link></link> <!-- lien vers une feuille CSS -->
```

> Dans une balise autofermante, l’espace avant la barre oblique est optionnel.

Voici une liste d’éléments vides : [Éléments vides MDN, fr][Éléments vides MDN, fr]

### Éléments HTML non vides

Si un élément peut avoir un contenu (*non-void HTML element* en anglais), mais que ce contenu est simplement vide dans un contexte donné, il n’est pas valide d’utiliser la notation compacte.

Donc ceci est valide :

```html
<p></p> <!-- Paragraphe -->
<li></li> <!-- Élément de liste -->
<h1></h1> <!-- Titre de niveau 1 -->
```

Alors que ceci n’est pas valide :

```html
<p /> <!-- Paragraphe -->
<li /> <!-- Élément de liste -->
<h1 /> <!-- Titre de niveau 1 -->
```

> La grande majorité des éléments HTML sont non vides.

### Cas particulier de l’élément `<script>`

L’élément `script` est un peu spécial parce qu’il peut être utilisée de deux façons différentes :

- Pour appeler un script externe au fichier HTML.
- Pour définir un script interne au fichier HTML.

Dans le cas de l’appel du script externe, cet élément est toujours vide. Il serait donc légitime de penser qu’on peut utiliser la balise autofermante. Mais comme cet élément peut avoir un contenu dans sa deuxième utilisation, on doit toujours utiliser la notation avec une balise ouvrante et une balise fermante.

```html
<!-- Lien vers un fichier JavaScript (JS) externe. -->
<script src="scripts.js"></script>

<!--
    Définition d’un script JavaScript (JS) interne.
    Comme la balise <script> contient le script dans ce cas là, on ne peut pas l’autofermer lorsqu’on l’utilise pour faire un lien vers un fichier externe (exemple ci-dessus), même si l’élément est vide.
-->
<script>
    console.log("Hello Microclub !")
</script>
```

Notons au passage que les feuilles de style CSS peuvent aussi être internes ou externes au fichier HTML. Mais dans ce cas, les balises utilisées sont différentes :

```html
<!--
    Lien vers une feuille de style CSS externe.
    Comme la balise <link> est toujours vide, elle doit être autofermée.
    -->
<link rel="stylesheet" href="style.css" />

<!-- Définition d’une feuille de style CSS interne. -->
<style rel="stylesheet">
    /* commentaire CSS */
</style>
```

Pour résumer :

CSS externe : `<link />`
CSS interne : `<style></style>`
JS externe : `<script></script>`
JS interne : `<script></script>`

### Imbrication d’éléments

Lorsque les éléments sont imbriqués (*nested* en anglais), il est important de fermer les balises “enfants” avant les balises “parents”.

Ceci est correct :

```html
<p>
    <strong>...</strong>
</p>
```

Ceci ne l’est pas :

```html
<p>
    <strong>...</p>
</strong>
```


### Quelques éléments courants

Voici une liste non exhaustive d’éléments courants :

```html
<p>Ceci est un paragraphe.
Les retours à la ligne doivent y
être explicitement indiqués avec la balise <br />
&lt;br />
La balise “p” est la plus utilisée pour afficher du texte.
</p>

<p><strong>Texte en gras</strong></p>

<p><em>Texte en italique</em></p>

<p><strong>Texte en gras <em>avec une partie italique</em></strong></p>

<pre>Ceci est un texte préformaté
     dans lequel les passages à la ligne
     et les espaces
     seront respectés</pre>

<p>Le <span>est</span> utilisé pour formater différemment une partie du texte.</p>

<div>Le div sert à regrouper des balises.
    <p>...</p>
    <p>...</p>
    <div></div>
</div>

<img src="https://ouilogique.com/images/site-logo.png" alt="image de démo" />
```

### Liste des balises HTML

La norme HTML définit environ 130 balises différentes que vous pouvez découvrir en suivant les liens ci-dessous.

### Éléments vs balises

Comme nous l’avons vu ci-dessus, un élément HTML est composé de balises et d’un contenu. Dans le langage courant, on utilise souvent indifféremment les termes *éléments* et *balises*, même si à proprement parler il s’agit de deux choses distinctes.

### Pour en savoir plus

- [Les balises HTML et leur rôle (MDN fr)][Les balises HTML et leur rôle]
- [Référence des éléments HTML (MDN fr)][Référence des éléments HTML]
- [HTML Element Reference (W3Schools en)][HTML Element Reference]



## LES ATTRIBUTS

Toutes les balises acceptent des attributs, certains étant obligatoires d’autres optionnels.

Par exemple, la balise `<img>` qui sert à insérer une image a deux attributs obligatoires : `src` et `alt`. À noter que l’attribut `alt` est souvent omis dans les pages web que vous rencontrerez. Il est pourtant fortement conseillé, car il s’agit du texte qui remplacera l’image si celle-ci ne peut pas être affichée. Cet attribut est aussi utilisé par les systèmes de lecture pour les malvoyants.

```html
<img src="https://ouilogique.com/images/site-logo.png" alt="image de démo" />
```

[Voir les attributs possibles de la balise `<img />` sur le site MDN.][img MDN]

Les attributs peuvent être mis à ligne pour faciliter la lecture :

```html
<img
    src="https://ouilogique.com/images/site-logo.png"
    alt="image de démo" />
```

### Les attributs personnalisés

HTML5 permet à l’utilisateur de définir ses propres attributs ce qui peut être fort utile lorsqu’on désire rendre le document interactif avec JavaScript. Ces attributs personnalisés s’appellent “attributs de données” et doivent obligatoirement commencer par le préfix `data-`.

```html
<article
  id="voitureelectrique"
  data-columns="3"
  data-index-number="12314"
  data-parent="voitures">
...
</article>
```

[Voir les attributs de données sur MDN][Les attributs de données sur MDN]



## LE DOCTYPE

Le doctype est une chaine de caractère présente au début du fichier et qui définit explicitement la version de la norme HTML utilisée dans le document. Le mot *doctype* est un mot-valise tiré de la locution anglaise *Document Type Declaration*. Le seul doctype que nous utiliserons dans le cadre de ce cours est le doctype HTML 5 qui se déclare de la manière suivante :

```html
<!DOCTYPE html>
```

Si on ne spécifie pas de doctype, alors les agents utilisateurs utiliseront le *mode quirks*, c’est-à-dire que le moteur de disposition émule le comportement non standard de Netscape Navigator 4 et d’Internet Explorer 5. Ce mode permet de prendre en charge les sites web rédigés avant l’adoption généralisée des standards web.

Si on spécifie un doctype, alors les agents utilisateurs utilisent le mode standard total ou éventuellement le mode quasi standard (qui a priori n’existe plus).

Si vous désirez plus d’informations sur ces différents modes, vous pouvez vous référer aux liens ci-dessous. Je vous conseille de toute façon de ne pas jouer avec le feu et de toujours spécifier le doctype HTML 5 (`<!DOCTYPE html>`).

Pour déterminer si un agent utilisateur est en mode standard ou au contraire en mode quirks, vous pouvez utiliser le JavaScript suivant :

```js
    console.log(document.compatMode === "CSS1Compat" ? "standard" : "quirks");
```

Historiquement, de nombreux doctype ont eu cours et il est fort probable que vous en rencontriez d’autres.

Le doctype est un élément à part dans la grammaire HTML dans le sens où sa balise ouvrante ne doit jamais être fermée.

### Pour en savoir plus

- [Recommended list of Doctype declarations (W3C en)][Recommended list of Doctype declarations (W3C en)]
- [Document type declaration (Wikipedia en)][Document type declaration]
- [Doctype (Wikipedia fr)][Doctype]
- [Mode quirks de Mozilla (MDN fr)][Mode quirks de Mozilla]
- [Mode presque standard de Gecko (MDN fr)][Mode presque standard de Gecko]
- [Fix Your Site With the Right DOCTYPE!][Fix Your Site With the Right DOCTYPE!]



## L’ESPACE DE NOM

Certains validateurs comme celui de l’éditeur [*Oxygen XML Editor*][oxygenxml.com] imposent que l’espace de nom soit spécifié et ceci se fait dans l’attribut `xmlns` de la balise `<html>` ouvrante :

```html
<html xmlns="http://www.w3.org/1999/xhtml">
...
</html>
```



## LES ÉDITEURS DE CODE HTML

Voici une liste non exhaustive d’éditeurs de code HTML :

- [Brackets][brackets.io] (que nous allons utiliser pour ce cours)
- [Sublime Text 3][sublimetext.com] (que j’utilise au quotidien)
- [Atom][atom.io]
- [Oxygen XML Editor][oxygenxml.com]
- [Visual Studio Code][code.visualstudio.com]
- [Notepad++][notepad++]
- [BBEdit][bbedit]
- [Gedit][gedit]
- [Nano][nano]
- ...



## LA VALIDATION

À ce stade, nous pouvons commencer à vérifier que ce que nous faisons est valide avec le validateur du World Wide Web Consortium (W3C) [W3C Markup Validation Service][validator input].


## LES ENTITÉS

Les entités servent à référencer les caractères par un code qui peut être textuel, décimal ou hexadécimal. Ceci est particulièrement utile dans les cas suivants :

- Le caractère est aussi utilisé dans la grammaire HTML comme les signes &lt;, &gt; et &amp;.
- Le caractère peut être confondu avec un autre ayant un glyphe visuellement identique, comme l’espace insécable qui est visuellement identique à l’espace simple et que l’on représentera par donc par `&nbsp;` ou le trait d’union insécable, identique au trait d’union normal et que l’on représentera par `&#8209;`.
- Le type d’encodage du fichier texte ne permet pas de représenter le caractère. Par exemple si le fichier est encodé en `windows-1257`, le caractère “ç” ne sera pas utilisable directement, mais pourra quand même être représenté avec l’entité `&ccedil;`.
- Le caractère ne s’affiche pas correctement dans votre éditeur, comme l’émoticône “visage souriant” (`&#9786;` = &#9786;).
- Le caractère est par nature invisible, comme l’espace sans chasse (`&#8203;`).

> Pour tout nouveau projet, il est important de s’assurer que tous vos fichiers sont encodés en `utf-8` qui est une norme quasi universelle aujourd’hui en occident. Le premier avantage est que vos fichiers seront lisibles par la grande majorité des agents utilisateurs et le deuxième avantage est que vous ne serez pas contraint d’utiliser plus d’entités que nécessaire.

### Quelques entités

| Caractère                   | Glyphe  | Entité textuelle | Entité décimale | Entité hexadécimale |
| :---                        | :---:   | :---:            | :---:           | :---:               |
| Signe inférieur à           | &lt;    | `&lt;`           | `&#60;`         | `&#x3C;`            |
| Signe supérieur à           | &gt;    | `&gt;`           | `&#62;`         | `&#x3E;`            |
| Esperluette                 | &amp;   | `&amp;`          | `&#38;`         | `&#x26;`            |
| Espace insécable            | &#160;  | `&nbsp;`         | `&#160;`        | `&#xA0;`            |
| Trait d’union insécable     | &#8209; |                  | `&#8209;`       | `&#x2011;`          |
| Émoticône “visage souriant” | &#9786; |                  | `&#9786;`       | `&#x263A;`          |
| Espace sans chasse          | &#8203; |                  | `&#8203;`       | `&#x200B;`          |


Vous trouverez une liste exhaustive d’entités sur [unicode-table.com][unicode-table.com].



## HTML vs XHTML

La norme HTML 5 autorise deux syntaxes :

- La syntaxe HTML
- La syntaxe XHTML

La différence la plus notable est que la syntaxe HTML autorise que certaines balises ne soient pas fermées :

en HTML, ceci est valide :

```html
<meta charset="utf-8">
<p>...
<ul>
    <li>...
    <li>...
</ul>
```

alors qu’en XHTML, toutes les balises doivent être fermées :

```html
<meta charset="utf-8" />
<p>...</p>
<ul>
    <li>...</li>
    <li>...</li>
</ul>
```

> La syntaxe XHTML a l’immense avantage d’être logique et facile à appliquer lorsque l’on génère le code à la main. De plus elle permet d’utiliser les outils prévus pour les fichiers XML, comme les langages XPath, XSLT et XQuery.
>
> La syntaxe HTML permet quand à elle d’économiser quelques octets puisque le nombre de balises nécessaires est moindre. Certaines personnes, dont je ne fais pas partie, la trouvent aussi plus facile à lire puisque moins verbeuse.
>
> Le validateur du W3C accepte le mélange des deux syntaxes dans un même document et de ce que je peux voir sur le web, la syntaxe HTML a le vent en poupe. Cependant, **mon conseil est de privilégier ~~systématiquement~~ la syntaxe XHTML.** (Je découvre quelques mois plus tard que [Google suggère de privilégier la syntaxe HTML][Google HTML CSS Style Guide Optional Tags].)



### Les différences principales entre HTML et XHTML

#### Structure du document

- Le doctype `<!DOCTYPE html>` est obligatoire.
- L’attribut `xmlns="http://www.w3.org/1999/xhtml"` est obligatoire.
- Les balises `<html>`, `<head>`, `<title>`, et `<body>` sont obligatoires.

#### Balises XHTML

- Les balises doivent être imbriquées correctement.
- Les balises doivent être systématiquement fermées ou autofermées.
- Les balises doivent être écrites en minuscules.
- La balise racine `<html>` doit être unique.

#### Attributs XHTML

- Les attributs doivent être écrits en minuscules.
- Les valeurs des attributs doivent être entourées de guillemets simples (`'`) ou doubles (`"`).
- La minimisation des attributs est interdite.<br /> `FAUX  ⇒ <input checked />`<br />`JUSTE ⇒ <input checked="checked" />`

> Note : Je préfère souvent les guillemets doubles (`"`) aux guillemets simples (`'`), parce que l’apostrophe sur un clavier standard est aussi un guillemet simple et que ça peut rendre les recherches fastidieuses, particulièrement quand on veut appliquer les règles de typographie soignées qui imposent d’utiliser l’apostrophe typographique (`’`) au lieu de l’apostrophe droite (`'`).

### Pour en savoir plus

- [HTML and XHTML (W3Schools en)][HTML and XHTML]
- [Apostrophe et « impostrophe »][Apostrophe et « impostrophe »]
- [Google HTML/CSS Style Guide][Google HTML CSS Style Guide]


## LE TRAITEMENT DES BLANCS

> On appelle “blanc” ou *whitespace* en anglais, un caractère qui n’a pas de représentation graphique. Les blancs les plus usuels sont le retour à la ligne et l’espace ([qui est un mot féminin en typographie][Un espace ou une espace ?]).

En HTML et en CSS, il y a 5 façons possibles de traiter les blancs :

- **normal**
Les séries de blancs sont regroupées, les caractères de saut de ligne sont gérés comme les autres blancs. Les passages à la ligne sont faits naturellement pour remplir les boîtes.

- **nowrap**
Les blancs sont regroupés comme avec normal mais les passages à la ligne automatiques sont supprimés.

- **pre**
Les séries de blancs sont conservées telles quelles. Les sauts de ligne ont uniquement lieu avec les caractères de saut de ligne et avec les éléments `<br />`.

- **pre-wrap**
Les séries de blancs sont conservées telles quelles. Les sauts de ligne ont lieu avec les caractères de saut de ligne, avec `<br />` et on a des passages à la ligne automatiques.

- **pre-line**
Les séries de blancs sont regroupées, les sauts de lignes ont lieu avec les caractères de saut de ligne, les éléments `<br />` et on a des passages à la ligne automatiques.

### Exemple de blanc *normal* avec la balise `<p>`

- Les espaces successives ne comptent que pour une espace.
- Si on veut tout de même afficher plusieurs espaces successives, il faut utiliser l’espace insécable (`&nbsp;`).
- Un ou plusieurs retours à ligne sont traités comme une seule espace.
- Si on veut un retour à ligne, on doit utiliser la balise `<br />` (*line break*).

### Valeurs par défaut

- **normal**
La grande majorité des balises HTML ont leur attribut CSS `white-space` défini par défaut à la valeur `normal`.

- **pre**
`<option>`, `<pre>`, `<select>`

- **pre-wrap**
`<textarea>`

### Modification de la valeur par défaut

On peut modifier la valeur de l’attribut `white-space` par défaut avec l’instruction CSS suivante :

```html
p.pre-line { white-space: pre-line; }
```

### Pour en savoir plus

- [white-space (MDN fr)][white-space (MDN fr)]
- [Un espace ou une espace ?][Un espace ou une espace ?]



## LES COMMENTAIRES

Si l’on veut commenter une portion de code HTML, il faut utiliser la notation suivante :

```html
<!-- Commentaire -->
```

Par contre, il faut utiliser les marques de commentaire natives des langages que l’on intègre :

Exemple avec du code CSS intégré dans le code HTML :

```html
<style rel="stylesheet">
    /* commentaire CSS */
</style>
```

Exemple avec du code JavaScript intégré dans le code HTML :

```html
<script>
    /* commentaire JS */
    // Commentaire JS
</script>
```


[white-space (MDN fr)]: https://developer.mozilla.org/fr/docs/Web/CSS/white-space

[HTML and XHTML]: https://www.w3schools.com/html/html_xhtml.asp

[unicode-table.com]: https://unicode-table.com/fr/

[nano]: https://www.nano-editor.org/

[gedit]: https://doc.ubuntu-fr.org/gedit

[bbedit]: https://www.barebones.com/products/bbedit/

[notepad++]: https://notepad-plus-plus.org/fr/

[code.visualstudio.com]: https://code.visualstudio.com/

[atom.io]: https://atom.io/

[sublimetext.com]: https://www.sublimetext.com/

[brackets.io]: http://brackets.io/

[User agent]: https://fr.wikipedia.org/wiki/User_agent

[Les balises HTML et leur rôle]: https://developer.mozilla.org/fr/Apprendre/HTML/Balises_HTML

[Référence des éléments HTML]: https://developer.mozilla.org/fr/docs/Web/HTML/Element

[HTML Element Reference]: https://www.w3schools.com/tags/

[Doctype]: https://fr.wikipedia.org/wiki/Doctype

[Document type declaration]: https://en.wikipedia.org/wiki/Document_type_declaration

[Mode quirks de Mozilla]: https://developer.mozilla.org/fr/docs/Web/HTML/Quirks_Mode_and_Standards_Mode

[img MDN]: https://developer.mozilla.org/fr/docs/Web/HTML/Element/Img

[Mode presque standard de Gecko]: https://developer.mozilla.org/fr/docs/Mozilla/Mode_presque_standard_de_Gecko

[oxygenxml.com]: https://www.oxygenxml.com/

[validator.w3.org]: https://validator.w3.org/

[validator input]: https://validator.w3.org/#validate_by_input

[Prince XML]: https://www.princexml.com/

[Apostrophe et « impostrophe »]: https://www.druide.com/fr/enquetes/apostrophe-et-impostrophe

[Un espace ou une espace ?]: https://www.druide.com/fr/enquetes/un-espace-ou-une-espace

[Wiki du cours HTML embarqué]: https://github.com/NicHub/microclub-atelier-html-embarque/wiki

[Éléments vides MDN, fr]: https://developer.mozilla.org/fr/docs/Glossaire/Element_vide

[Recommended list of Doctype declarations (W3C en)]: https://www.w3.org/QA/2002/04/valid-dtd-list.html

[Fix Your Site With the Right DOCTYPE!]: http://alistapart.com/article/doctype

[Les attributs de données sur MDN]: https://developer.mozilla.org/fr/Apprendre/HTML/Comment/Utiliser_attributs_donnes

[Microclub]: https://microclub.ch/

[microclub-atelier-html-embarque.pdf]:  ../../files/2018-02-17-html-embarque/microclub-atelier-html-embarque.pdf

[Introduction au langage HTML]: ../introduction-html/

[Introduction au langage CSS]: ../introduction-css/

[Introduction au langage JavaScript]: ../introduction-javascript/

[Google HTML CSS Style Guide]: https://google.github.io/styleguide/htmlcssguide.html

[Google HTML CSS Style Guide Optional Tags]: https://google.github.io/styleguide/htmlcssguide.html#Optional_Tags
