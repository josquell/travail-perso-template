Fonctionnement d'un processeur
##############################

Les transistors
===============

Définition d'un transistor
__________________________

Un transistor est un composant électronique constitué de matériaux semi-conducteurs utilisé pour redresser, amplifier ou interrompre des oscillations électriques en fonction de la tension qui lui est envoyé. 
Un transistor laisse passer le courant électrique dans un sens, mais pas dans l’autre.

Fonctionnement d'un transistor
______________________________

Un transistor fonctionne avec le binaire. 
Ainsi, une forte tension électrique est assimilée à la valeur 1, alors qu’une faible tension électrique à la valeur 0.

images/transistor.png

Voici un schéma qui présente les deux types de transistors qu’il est possible de construire. 
Le premier transistor est un transistor NPN.

Il est tout d’abord possible de distinguer la zone appelée substrat, qui est composée d’atomes de silicium dopé positivement, d’où la lettre P dans NPN. 
Cela signifie que le silicium a été bombardé d’ions afin de remplacer certains de ses atomes en une autre espèce d’atomes. 
Dans le cas d’un dopage positif, certains atomes de silicium sont remplacés par des atomes de bore qui contiennent un électron de moins que les atomes de silicium. 
Ainsi, le substrat dopé contient moins d’électrons que de protons et cherche constamment à obtenir des électrons, c’est la raison pour laquelle on parle de dopage positif.

Il peut être ensuite observé la source et le drain qui sont deux substrats de silicium dopé négativement. 
Certains des atomes de silicium ont été remplacés par des atomes de phosphore qui contiennent un électron de plus que les atomes de silicium. 
Cette fois-ci, le silicium dopé contient plus d’électrons que de protons et cherche constamment à se débarrasser d’électrons, c’est la raison pour laquelle on parle de dopage négatif. 
Le drain représente l’arrivée des électrons tandis que la source représente la sortie des électrons (pour autant que le courant circule). 
La source et le drain sont aussi appelés émetteur, respectivement collecteur.

Enfin, il est possible de distinguer la grille, également appelée base. 
La grille peut soit envoyer une tension positive, donc demander des électrons, soit envoyer une tension négative, c’est-à-dire apporter des électrons. 
La tension de la grille est toujours plus faible que la tension de la source.

Lorsqu’une zone dopée positivement est mise en contact avec une zone dopée négativement, si le courant électrique est faible, ce dernier ne peut circuler que de la zone négative à la zone positive, et non de la zone positive à la zone négative. 
Le courant électrique pourra néanmoins circuler de la zone positive à la zone négative si celui-ci est assez élevé.

Dans le cas du transistor NPN, si la grille envoie une tension négative, soit le signal 0, elle empêchera le courant électrique de passer du drain à la source. 
À l’inverse, si la grille envoie une tension positive, soit le signal 1, elle permettra au courant électrique de circuler du drain à la source. 
Le courant peut donc circuler dans un sens, mais pas dans l’autre. C’est ainsi que fonctionne le transistor NPN.

En ce qui concerne le transistor PNP, le substrat de silicium est cette fois-ci dopé négativement alors que la source et le drain sont dopés positivement. 
Cela a pour seule conséquence que lorsque la grille envoie une tension négative (signal 0), le courant électrique peut circuler de la source au drain, alors que si la grille envoie une tension positive (signal 1), le courant électrique ne peut pas circuler de la source au drain.

Les portes logiques
===================

Définition d'une porte logique
______________________________

Une porte logique est un composant élémentaire d’un circuit numérique. 
Il existe sept portes logiques de base : AND, OR, XOR, NOT, NAND, NOR et XNOR. 
La majorité des portes logiques disposent de deux entrées et d’une sortie. 
L’objectif d’une porte logique est de renvoyer un signal positif (1) ou négatif (0) à la sortie en fonction des deux valeurs d’entrée.

Fonctionnement d'une porte logique
__________________________________

images/schema_NOT.jpg

La porte logique la plus simple est certainement la porte NOT, aussi appelé NON.
La figure 2 Schématise une porte logique NOT. 
Le but de cette porte est d’inverser la valeur d’entrée. 
Il est possible d’observer la tension d’alimentation qui envoie en continu un courant. 
La masse quant à elle attire les électrons lorsqu’il y a un courant. 
Les deux tiges noires juxtaposées d’un point blanc symbolisent un transistor PNP alors que les deux tiges noires situées vers le bas symbolisent un transistor NPN. 
Lorsque la valeur d’entrée est 1, le transistor PNP ne laisse pas passer le courant de l’alimentation à la sortie, alors que le transistor NPN laisse passer le signal issu de la masse qui est nul. 
C’est donc la valeur 0 qui sortira de la porte logique. 
À l’inverse, lorsque le signal d’entrée est 0, le transistor PNP laisse passer le courant de l’alimentation à la sortie, tandis que le transistor NPN ne laisse pas passer le signal nul issu de la masse. 
C’est donc cette fois-ci la valeur 1 qui sortira de la porte logique.

Il est dès lors possible de dresser un tableau récapitulatif qui présente les valeurs de sortie en fonction des valeurs d’entrée d’une porte logique NOT :

images/tableau_NOT.png

Ensuite, la porte logique AND a pour mission de retourner la valeur 1 uniquement lorsque les deux valeurs d’entrée valent 1. 
Voici un schéma simplifié de la porte logique AND.

images/schema_AND.png

Sur la figure 3, T1, T2 et T3 représentent des transistors PNP alors que T4, T5 et T6 représentent des transistors NPN. 
Le chiffre 1 présent tout en haut à droite symbolise l’arrivé du courant issu de l’alimentation. 
Lorsque les deux valeurs d’entrée valent 1, T1 et T2 ne laissent pas passer le courant, ce qui a pour conséquence de laisser ouvert T3 qui laisse alors passer le courant de l’alimentation à la sortie. 
La valeur de sortie est donc 1. 
Lorsque la valeur de l’entrée A est 1 et la valeur de l’entrée B est 0, T2 laisse passer le courant, ce qui a pour conséquence de fermer T3, ce qui empêche le courant de circuler de l’alimentation à la sortie. 
La valeur de sortie est donc 0. 
Lorsque la valeur de l’entrée A est 0 et la valeur de l’entrée B est 1, T1 laisse passer le courant, T3 est donc à nouveau fermé, ce qui empêche le courant de circuler de l’alimentation à la sortie. 
La valeur de sortie est donc 0. 
Enfin, dans le cas où la valeur de l’entrée A et B est 0, T1 et T2 sont ouverts, ce qui a pour conséquence de fermer T3, et d’empêcher le courant de circuler de l’alimentation à la sortie. 
La valeur de sortie est donc 0. Dans les trois derniers cas, T6 laissent passer le signal qui est nul.
Il est dès lors possible de dresser un tableau récapitulatif d’une porte logique AND qui présente les valeurs de sortie en fonction des deux valeurs d’entrée :

images/tableau_NOT

Pour la porte logique NAND, les valeurs de sortie sont simplement l’inverse des valeurs de sortie de la porte logique AND.
Concernant la porte logique OR, la valeur de sorti doit être 0 uniquement lorsque les deux valeurs d’entrée valent 0. 
Dans les trois autres cas, la valeur de sortie doit être 1.
Dans le cas de la porte logique NOR, les valeurs de sortie sont simplement l’inverse des valeurs de sortie de la porte logique OR.
Ensuite la porte XOR retourne 0 si la valeur d’entrée A et la valeur d’entrée B sont identiques et 1 dans les deux autres cas.
À nouveau, pour la porte logique XNOR, les valeurs de sortie sont l’inverse des valeurs de sortie de la porte logique XOR.
Les différentes portes logiques ont dès lors été parcourues. 
Les portes logiques permettent de construire des circuits logiques plus ou moins complexes.



