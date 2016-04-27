# Pi-Kart
Projet Tuteuré de mini-voiture autonome 

## Besoins :
 - un circuit ! (DIY)
 - une base de données avec les panneaux


## Fonctionnement essentiel
Etape 1 :
	Récupérer une image de l'environnement devant la voiture
Etape 2 :
	Analyser les formes de l'image pour en sortir les possibles panneaux (triangle, triangle inversé, disque, carré (useless))
Etape 3 :
	Comparer les différentes formes trouvée avec les panneaux connus
Etape 4 : 
	Agir sur les paramètres de la voiture par rapport à la situation détéctée (vitesse, clignotant, direction, etc...)

## Fonctionnement facultatif:
	- Reconnaitre les priorités et réagir
	- Reconnaitre les obstacles (un vieux sur la route)
