

**128 full-color display type P6-16**
=====================================

16×128 pixels

[Xuan Cai](szxcled.com)



# INFORMATIONS AU DÉMARRAGE

	Colorful LED V39
	System Checks..
	Password OFF
	Baud 9600
	Sim card OK!
	CSQ Checks...
	CSQ: 9

> Le CSQ indique la qualité du signal GPRS. L’idéal serait que le CSQ soit plus grand ou égal à 15, mais ça fonctionne avec un CSQ de 6.


# CARTE SIM

Introduire la carte SIM avec son support en plastique.

Ressortir la carte en pressant le bouton vert à côté de celle-ci.

La carte SIM permet de contrôler l’afficheur à distance via SMS ou *Fetion App* (service chinois de messagerie).



# MOT DE PASSE

Pas de mot passe par défaut.



# COMMANDE PAR SMS

> Les commandes sont sensibles à la casse !<br/>
> Les accents ne sont pas supportés !<br/>
> 140 caractères maximum !

## Protocole

Le message commence obligatoirement par `*` et se termine obligatoirement par `#×` où `×` est le n° du message à afficher, × = 1 .. 59. Si × n’est pas dans l’intervalle 1 .. 59, le message `#1` est modifié. × peut être spécifié avec un `0` non significatif (#1 ou #01).

Les autres sélecteurs (mode de défilement, n° de ligne, couleur) sont optionnels.

|        |                                                                                                           |
| --     | --                                                                                                        |
| `<F×>` | Mode de défilement, × = 1 .. 6                                                                            |
| `<L×>` | N° de ligne, × = 1, 2                                                                                     |
| `<C×>` | Définition de la couleur, × = R (rouge), Y (jaune), G (vert), C (cyan), B (bleu), P (mangenta), W (blanc) |

## Modes de défilement

|        |                           |
| --     | --                        |
| `<F1>` | statique                  |
| `<F2>` | défilement vers le haut   |
| `<F3>` | défilement vers la gauche |
| `<F4>` | défilement vers le bas    |
| `<F5>` | clignote                  |

## Combinaisons de modes de défilements possibles sur deux lignes

|        |      |      |      |      |      |      |      |      |      |      |      |
| --     | --   | --   | --   | --   | --   | --   | --   | --   | --   | --   | --   |
| **L1** | `F1` | `F1` | `F1` | `F1` | `F2` | `F2` | `F2` | `F4` | `F4` | `F5` | `F5` |
| **L2** | `F1` | `F2` | `F3` | `F4` | `F1` | `F2` | `F3` | `F1` | `F4` | `F3` | `F5` |

## Exemples de messages sur une ligne

> Le mode de défilement est optionnel. Si on ne le précise pas, tous les modes de défilement sont utilisés successivement et dans l’ordre chronologique (F1, F2,...). On ne peut pas spécifier plusieurs modes de défilement sur une ligne donnée.<br/>
> Les lignes de commande ci-dessous doivent être envoyées dans des SMS distincts.

	*<F1><CG>A GAGNER A L'EURO MILLIONS : <CR>!! 147 MILLION$ !!#02
	*<F5>!! 147 MILLION$ !!#03

## Exemples de messages sur deux lignes

> En mode deux lignes, les caractères ont une hauteur de 7 px.
> Par défaut, la première lignes est statique et la deuxième défile vers la gauche.<br/>
> On peut changer les modes de défilement des deux lignes. Voir les combinaisons possibles ci-dessus.

	*<L1><F2>KIOSQUE DE MONTCHOISI<L2><F2>JOYEUSES FETES DE FIN D'ANNEE#01
	*<L1><F4>KIOSQUE DE MONTCHOISI<L2><F4>JOYEUSES FETES DE FIN D'ANNEE#04

## Spécifier les textes qui doivent s’afficher

	*RL#01#02#03#04*

## Spécifier la couleur

> Si aucune couleur n’est spécifiée, les caractères s’affichent dans 7 couleurs successivement :
(rouge R, jaune Y, vert G, cyan C, bleu B, mangenta P, blanc W)

	*<CR>ce texte sera rouge <CY>et celui-ci sera jaune#08

## Spécifier la vitesse

> Vitesses de 1 à 6<br/>
> 1 = rapide, 6 = lent<br/>
> Utiliser de préférence les vitesses S1, S2 et S3. Les autres ont tendance à scintiller.<br/>
> La vitesse est définie pour tous les messages. On ne peut pas régler des vitesses individuelles.

	*S1*

## Spécifier la luminosité

> Luminosité de 1 à 6<br/>
> 1 = moins lumineux, 6 = plus lumineux
> La luminosité est définie pour tous les messages. On ne peut pas régler des luminosité individuelles.

	*B1*

## Mise à zéro

> La mise à zéro supprime tous les messages. Si aucun message n’est enregistré, le message “Welcome!” est affiché.

	*DEL*


