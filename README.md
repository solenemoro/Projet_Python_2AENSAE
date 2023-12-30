# Projet_Python_2AENSAE
## Pourquoi les Parisiens aiment-ils (ou pas) leur quartier ? 


Dans ce projet, nous nous intéressons aux notes que les Parisiens ont attribuées à leur quartier, et essayons de les comprendre en s'intéressant à différentes variables. 
Les données brutes (csv, xlsx...) sont réunies dans le dossier 'data'.

Données utilisées :

-   espaces_verts.geojson est le fichier recensant les espaces verts de paris et leur géolocalisation. Il provient du site Paris Open Data
-   Notes_arrondissements.xlsx est le fichier résultant du code "Webscraping" qui récupère les notes données par les Parisiens à leur quartier sur le site ville-ideale.fr . Il contient les notes attribuées par les habitants à leur arrondissement au niveau global mais aussi selon 9 critères précis. Les notes sont comprises entre 0 et 10 et la note globale est calculée selon la formule (note qualité de vie + moyenne des notes des 8 autres critères) / 2.
-   lieux_culturels.csv provient de data.culture.gouv.fr et recense les lieux culturels.
-   bpeParis.csv est extrait de la base permanente des équipements (BPE) de l'INSEE. Ce fichier ne concerne que la région parisienne et a permis de créer les fichiers Commerces.csv, Education.csv et Transports.csv
-   reference_IRIS_geo2023.xlsx permet d'établir un lien entre les IRIS (qui sont l'unité de base de la BPE) et les arrondissements (qui sont l'unité de base du fichier de notes)


Le code Python est réparti dans différents fichiers Python et notebooks Jupyter. Il est recommandé de suivre l'ordre suivant pour l'éxecution du code :


### Partie 1 : Webscrapping (Ne pas exécuter car l'exécution dure 1h)

1. Webscraping.ipynb
   
   Ce notebook récupère les notes données par les parisiens à leur quartier sur le site ville-ideale.fr . Il crée un fichier "Notes_arrondissements.xlsx" que l'on retrouvera dans le dossier "data". 

### Partie 2 : Cartographie des espaces verts de Paris et correlation avec les notes d'arrondissements

1. espaces_verts.ipynb
   
   Ce notebook récupère grâce au module cartiflette la géolocalisation des arrondissements de paris et utilise la base de données "espaces_verts.geojson" provenant de Paris Open Data.
   Il représente gographiquement les espaces verts de Paris et compare la surface verte aux notes données par les Parisiens au critère "Environnement" et à la note globale pour établir ou non une corrlation.

### Partie 3 : Zoom sur la culture

1. Cartes.ipynb 

Ce notebook utilise la librairie cartiflette pour visualiser les notes concernant la culture et le nombre de lieux culturels dans chaque arrondissement. Ces cartes nous donnent une première vision d'ensemble de la question.

2. analyse_descriptive.ipynb

Nous procédons ici à une analyse descriptive des notes moyennes données à la culture pour chaque arrondissement, et poussons l'analyse de comparaison avec le nombre de lieux culturels plus loin en s'intéressant désormais à la densité de lieux culturels par arrondissement.

### Partie 4 : Corrélation entre les notes et le nombre d'équipements

1. Equipements.ipynb

Nous tentons d'établir des corrélations entre le nombre d'équipements et les notes données dans des thématiques variées : commerce, éducation, infrastructures de santé et moyens de transports. Pour cela, nous utilisons des régressions linéaires en essayant diverses variables explicatives à un niveau plus ou moins agrégé.


## Les limites :
Nos résultats comportent des biais. En effet, les notes données aux arrondissements sont extraites du site ville-ideale.fr et non d'une enquête officielle. De plus, certains arrondissements ont été notés par une vingtaine de personnes seulement donc un très faible nombre pour pouvoir faire des statistiques. Aussi, les personnes qui prennent le temps d'aler noter leur arrondissement sur le site internet sont peut-être celles qui sont les plus satisfaites ou au contraire les moins satisfaites de leur quartier, et ne représentent pas forcémment la population de ce quartier. 
Enfin, l'appréciation de leur quartier par les Parisiens dépend de beaucoup de choses et il faudrait une analyse plus complexe. Nous avons choisi ici de nous concentrer sur quelques variables.

