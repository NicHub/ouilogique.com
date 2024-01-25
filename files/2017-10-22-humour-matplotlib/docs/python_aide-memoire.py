#!/usr/bin/python
# -*- coding: UTF-8 -*-


u"""

Aide mémoire Python

Ceci est un exemple de docstring. Elle commence par la lettre u pour supporter Unicode.

"""

# Version de Python sur osx
# 4 juin 2011 -> Python 2.6.1
# 20 octobre 2018 -> Python 2.7.10


# Ajouter un chemin de recherche de modules (d’import)
import sys
sys.path.append('/mypath')
sys.path.append('/Users/nico/Documents/boulot/2011-04-26_jenova/2011-05-12_solarmax/application/diveintopython/diveintopython-examples-5.4/py/')

# Importer un module
import mymodule

# Obtenir des info sur un module
info(mymodule)

# Imprimer la docstring d’une fonction d’un module
print mymodule.myfunction.__doc__

# Imprimer la docstring d’un script
print globals()['__doc__']

# __name__ est le nom de fichier du module sans le chemin d’accès ni le suffixe

# Permet d’exécuter le module lorsqu’il est appelé manuellement (ie qu’il n’est pas utilisé pour ses fonctions)
if __name__ == "__main__":
    # mettre du code qui doit être exécuté uniquement lors de l’appel manuel




# DÉFINITION D’UN DICTIONNAIRE
# !! Les valeurs ne sont pas dans un ordre définit
# !! Les clés sont sensibles à la casse
# Les valeurs d’un dico peuvent être de n’importe quel type
# Les clés d’un dico peuvent être des strings, des entiers (et quelques autres encore)
d = {"server":"mpilgrim", "database":"master"}     # Assignation
d["server"]                                        # renvoie 'mpilgrim'
d["uid"] = "sa"                                    # Assignation
d                                                  # Renvoie {'database': 'master', 'uid': 'sa', 'server': 'mpilgrim'}
d[42] = "douglas"                                  # Clé numérique
d                                                  # {'retrycount': 3, 42: 'douglas', 'database': 'master', 'uid': 'sa', 'server': 'mpilgrim'}

# Effacer une clé
del d[42]
d                                                  # {'retrycount': 3, 'database': 'master', 'uid': 'sa', 'server': 'mpilgrim'}

# Effacer toutes les clés
d.clear()
d                                                  # Renvoie {}

# Teste la présence d’une clé avec une valeur donnée
"server" in d                                      # Renvoie True

# Ça ne marche pas sur les valeurs
"mpilgrim" in d                                    # Renvoie False


# DÉFINITION D’UNE LISTE

li = ["a", "b", "mpilgrim", "z", "example"]        # Assignation
li                                                 # Renvoie ['a', 'b', 'mpilgrim', 'z', 'example']
li[0]                                              # Renvoie 'a'
li[4]                                              # Renvoie 'example'
li[-1]                                             # Renvoie 'example'

# Découpage d’une liste
li[1:3]                                            # Renvoie ['b', 'mpilgrim']
li[1:-1]                                           # Renvoie ['b', 'mpilgrim', 'z']
li[0:-1]                                           # Renvoie ['a', 'b', 'mpilgrim', 'z']

# Raccourci pour le découpage
li[:3]                                             # Renvoie ['a', 'b', 'mpilgrim']
li[3:]                                             # Renvoie ['z', 'example']
li[:]                                              # Renvoie ['a', 'b', 'mpilgrim', 'z', 'example']

# Attention li ≠ li[:]. li[:] est utilisé pour créer une copie


# Ajout d’éléments à une liste
li.append("new")
li                                                  # Renvoie ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
li.insert(2, "new")
li                                                  # Renvoie ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
li.extend(["two", "elements"])                      # Concaténation de listes
li                                                  # Renvoie ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

# Différence entre extend et append
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
li                                                  # Renvoie ['a', 'b', 'c', 'd', 'e', 'f']

li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
li                                                  # Renvoie ['a', 'b', 'c', ['d', 'e', 'f']]

# Recherche dans une liste
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.index("example")                                 # Renvoie 5


# Avant la version 2.2.1, Python n'avait pas de type
#   booléen. Pour compenser cela, Python acceptait
#   pratiquement n'importe quoi dans un contexte
#   requérant un booléen (comme une instruction
#   if), en fonction des règles suivantes :
#
# 0 est faux, tous les autres nombres sont vrai.
#
# Une chaîne vide ("") est faux, toutes les autres
#   chaînes sont vrai.
#
# Une liste vide ([]) est faux, toutes les autres
#   listes sont vrai.
#
# Un tuple vide (()) est faux, tous les autres
#   tuples sont vrai.
#
# Un dictionnaire vide ({}) est faux, tous les
#   autres dictionnaires sont vrai.
#
# Ces règles sont toujours valides en Python 2.3.3
#   et au-delà, mais vous pouvez maintenant
#   utiliser un véritable booléen, qui a pour
#   valeur True ou False. Notez la majuscule, ces
#   valeurs comme tout le reste en Python, sont
#   sensibles à la casse.


# Enlever des éléments d’une liste
# Si la valeur n’existe pas, une erreur est retournée
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove("new")                                 # Enlève la première occurence de "new" et ne renvoie rien
li.pop()                                         # Enlève la dernière valeur de la liste et retourne cette valeur. Dans notre cas 'elements'


# Utilisation des opérateurs de listes
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
li                                                 # Renvoie ['a', 'b', 'mpilgrim', 'example', 'new']


# Teste la présence d’un élément avec une valeur donnée
"b" in li                                          # Renvoie True


# Attention, on peut concaténer avec l’opérateur + ou la fonction extend, mais l’opérateur + crée une nouvelle liste en mémoire
liste = liste + autreliste

# TUPLE
# Un tuple (n-uplet) est une liste non-mutable. Un fois créé, un tuple ne peut en aucune manière être modifié.
# La syntaxe est similaire aux listes. Les crochets droits sont remplacés par des parenthèses.
#Les tuples n’ont pas de méthodes
t = ("a", "b", "mpilgrim", "z", "example")

# Teste la présence d’un élément avec une valeur donnée
"b" in t                                           # Renvoie True


# Conversion de tuple en liste
a=list(t)                                          # Renvoie ['a', 'b', 'mpilgrim', 'z', 'example']
tuple(a)                                           # Renvoie ('a', 'b', 'mpilgrim', 'z', 'example')



# VARIABLES
# Assignation simultanée de plusieurs valeurs
v = ('a', 'b', 'e')
(x, y, z) = v
x                                                  # Renvoie a
y                                                  # Renvoie b
z                                                  # Renvoie e


# Assignation de valeurs consécutives
range(7)                                           # Renvoie [0, 1, 2, 3, 4, 5, 6]
(MONDAY, TUESDAY, WEDNESDAY, \
    THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
MONDAY                                             # Renvoie 0
TUESDAY                                            # Renvoie 1
WEDNESDAY                                          # Renvoie 2


# Afficher la doc d'une fonction
print range.__doc__


# FORMATAGE DE CHAÎNES
uid = "sa"
pwd = "secret"
print pwd + " is not a good password for " + uid   # Renvoie secret is not a good password for sa
print "%s is not a good\
 password for %s" % (pwd, uid)                     # Idem

userCount = 6
print "Users connected: %d" % (userCount, )        # Renvoie Users connected: 6. !! (userCount, ) est un tuple alors que (userCount) est une valeur simple
print "Users connected: " + userCount              # Erreur de conversion

# Formatage de nombres
print "Today’s stock price: %f" % 50.4625          # Renvoie 50.462500
print "Today’s stock price: %.2f" % 50.4625        # Renvoie 50.46
print "Change since yesterday: %+.2f" % 1.5        # Renvoie +1.50



# MUTATION DE LISTES
# list comprehension (création fonctionnelle de listes)
li = [1, 9, 8, 4]
[elem*2 for elem in li]                            # Renvoie [2, 18, 16, 8], ne modifie pas li


# Mutation dans un dico
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params.keys()                                      # Renvoie les clés du dictionnaire -> ['pwd', 'database', 'uid', 'server']
params.values()                                    # Renvoie les valeurs du dictionnaire -> ['secret', 'master', 'sa', 'mpilgrim']
params.items()                                     # Renvoie la liste des tuples du dictionnaire -> [('pwd', 'secret'), ('database', 'master'), ('uid', 'sa'), ('server', 'mpilgrim')]
[k for k, v in params.items()]                     # Renvoie ['pwd', 'database', 'uid', 'server']
[v for k, v in params.items()]                     # Renvoie ['secret', 'master', 'sa', 'mpilgrim']
["%s=%s" % (k, v) for k, v in params.items()]      # Renvoie ['pwd=secret', 'database=master', 'uid=sa', 'server=mpilgrim']
";".join(["%s=%s" % (k, v) \
    for k, v in params.items()])                   # Renvoie 'pwd=secret;database=master;uid=sa;server=mpilgrim'


# Concaténation et découpage de chaînes
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
s                                                  # Renvoie 'server=mpilgrim;uid=sa;database=master;pwd=secret'
s.split(";")                                       # Renvoie ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s.split(";", 1)                                    # Renvoie ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
s.split(";", 2)                                    # Renvoie ['server=mpilgrim', 'uid=sa', 'database=master;pwd=secret']



# CHAPITRE 4. LE POUVOIR DE L’INTROSPECTION
# -----------------------------------------


# 4.2. Arguments optionnels et nommés
def info(object, spacing=10, collapse=1):         # spacing et collapse sont optionnels car ils ont des valeurs par défaut. Par contre object est obligatoire
info(odbchelper)
info(odbchelper, 12)
info(odbchelper, collapse=0)
info(spacing=15, object=odbchelper)


# Obtenir le type d’une donnée
type(1)                                            # Renvoie <type 'int'>
type([])                                           # Renvoie <type 'list'>
type(())                                           # Renvoie <type 'tuple'>
type({})                                           # Renvoie <type 'dict'>

import types
type(1) == types.IntType                           # Renvoie True
type([]) == types.ListType                         # Renvoie True
type(()) == types.TupleType                        # Renvoie True
type({}) == types.DictType                         # Renvoie True
import odbchelper
type(odbchelper)                                   # Renvoie <type 'module'>
import types
type(odbchelper) == types.ModuleType               # Renvoie True


# Convertir une donnée en chaîne
str(1)                                             # Renvoie '1'
horsemen = ['war', 'pestilence', 'famine']
horsemen                                           # Renvoie ['war', 'pestilence', 'famine']
str(horsemen)                                      # Renvoie "['war', 'pestilence', 'famine']"
str(odbchelper)                                    # Renvoie "<module 'odbchelper' from '/Users/nico/Documents/boulot/2011-04-26_jenova/2011-05-12_solarmax/application/diveintopython/diveintopython-examples-5.4/py/odbchelper.pyc'>"
str(None)                                          # Renvoie 'None'

# Obtenir les méthodes d'un objet
dir(1)                                            # Renvoie ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
dir([])                                           # Renvoie ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(())                                           # Renvoie ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
dir({})                                           # Renvoie ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dir(odbchelper)                                   # Renvoie ['__author__', '__builtins__', '__copyright__', '__date__', '__doc__', '__file__', '__license__', '__name__', '__package__', '__version__', 'buildConnectionString']


# Test si une méthode peux être invoquée

import string
dir( string )                                      # Renvoie ['Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_float', '_idmap', '_idmapL', '_int', '_long', '_multimap', '_re', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'atof', 'atof_error', 'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count', 'digits', 'expandtabs', 'find', 'hexdigits', 'index', 'index_error', 'join', 'joinfields', 'letters', 'ljust', 'lower', 'lowercase', 'lstrip', 'maketrans', 'octdigits', 'printable', 'punctuation', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate', 'upper', 'uppercase', 'whitespace', 'zfill']
callable( string.join )                            # Renvoie True
callable( string.punctuation )                     # Renvoie False


# getattr


# Exemple 4.14. Présentation du filtrage de liste
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]             # Renvoie ['mpilgrim', 'foo']
[elem for elem in li if elem != "b"]               # Renvoie tous ce qui est différent de "b" -> ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
[elem for elem in li if li.count(elem) == 2]       # Renvoie tout les élément avec 2 occurences -> ['b', 'b', 'd', 'd']


# Présentation de type
type(1)                                            # Renvoie <type 'int'>
type( li )                                         # Renvoie <type 'list'>
import odbchelper
type(odbchelper)                                   # Renvoie <type 'module'>
import types
type(odbchelper) == types.ModuleType               # Renvoie True



# 4.6. Particularités de and et or
'a' and 'b'                                        # Renvoie 'b'
'b' and 'a'                                        # Renvoie 'a'
'' and 'b'                                         # Renvoie ''
'b' and ''                                         # Renvoie ''
'a' and 'b' and 'c'                                # Renvoie 'c'

# Lorsqu’on utilise and les valeurs sont évaluées
#   dans un contexte booléen de gauche à droite.
#   0, '', [], (), {} et None valent faux dans ce
#   contexte, tout le reste vaut vrai.[1]Si toutes
#   les valeurs valent vrai dans un contexte
#   booléen, and retourne la dernière valeur. Ici
#   and évalue 'a', qui vaut vrai, puis 'b', qui
#   vaut vrai et retourne 'b'.
#
# Si une des valeurs vaut faux and retourne la
#   première valeur fausse. Ici '' est la première
#   valeur fausse.
#
# Toutes les valeurs sont vrai, donc and retourne la
#   dernière valeur, 'c'.


'a' or 'b'                                         # Renvoie 'a'
'b' or 'a'                                         # Renvoie 'b'
'' or 'b'                                          # Renvoie 'b'
'b' or ''                                          # Renvoie 'b'
'a' or 'b' or 'c'                                  # Renvoie 'a'
def sidefx():
    print "in sidefx()"
    return 1
'a' or sidefx()                                    # Renvoie 'a'

# Lorsqu’on utilise or, les valeurs sont évaluées
#   dans un contexte booléen de gauche à droite,
#   comme pour and. Si une des valeurs vaut vrai,
#   or la retourne immédiatement. Dans ce cas 'a'
#   est la première valeur vraie.
#
# or évalue '', qui vaut faux, puis 'b', qui vaut
#   vrai et retourne 'b'.
#
# Si toutes les valeurs valent faux, or retourne la
#   dernière valeur. or évalue '', qui vaut faux,
#   puis [], qui vaut faux, puis {}, qui vaut faux
#   et retourne {}.
#
# Notez que or continue l’évaluation seulement
#   jusqu’à ce qu’il trouve une valeur vraie, le
#   reste est ignoré. C’est important si certaines
#   valeurs peuvent avoir un effet de bord. Ici,
#   la fonction sidefx n’est jamais appelée, car
#   or évalue 'a', qui vaut vrai et retourne 'a'
#   immédiatement.

# 4.7. Utiliser des fonctions lambda

# Fonction ordinaire
def f(x):
    return x*2

f(3)                                               # Renvoie 6

# Fonction lambda
g = lambda x: x*2
g(3)                                               # Renvoie 6
(lambda x: x*2)(3)                                 # Renvoie 6

# 4.8. Assembler les pièces
# 4.9. Résumé


# Divers

# La fonction "pass" est utile pour ne rien faire. C’est une opération nulle.
# par exemple :

def FonctionPasEncoreImplementee():
    pass



# Quitter de force

# http://stackoverflow.com/questions/9591350/what-is-difference-between-sys-exit0-and-os-exit0

import sys
sys.exit( 0 ) # Propre

import os
os._exit( 0 ) # Violent







# Boucles for
# For loops

for i in range( 0, 3 ):
    for j in range( 10, 13 ):
        print "Valeur de i = %d — Valeur de j = %d" % ( i, j )


# Boucles while
# While loops

count = 0
while( count < 9 ):
    print 'The count is:', count
    count = count + 1

print "Good bye!"


# Boucles do-while

i = 0
while( True ):
    print "C’est pas la fin car i = %d" % ( i )
    i = i + 1
    if i > 10:
        break


