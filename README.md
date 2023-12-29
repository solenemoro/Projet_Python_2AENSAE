# Projet_Python_2AENSAE
## Pourquoi les Parisiens aiment-ils (ou pas) leur quartier ? 


Dans ce projet, nous nous intéressons aux notes que les Parisiens ont attribuées à leur quartier, et essayons de les comprendre en s'intéressant à différentes variables. 
Les données brutes (csv, xlsx...) sont réunies dans le dossier 'data'.

Données utilisées :
-   
-   Notes_arrondissements.xlsx contient les notes attribuées par les habitants à leur arrondissement au niveau global mais aussi selon des catégories plus précises. Les notes sont comprises entre 0 et 10
-   lieux_culturels.csv provient de data.culture.gouv.fr
-   bpeParis.csv est extrait de la base permanente des équipements (BPE), ce fichier ne concerne que la région parisienne et a permis de créer les fichiers Commerces.csv, Education.csv et Transports.csv
-   reference_IRIS_geo2023.xlsx permet d'établir un lien entre les IRIS (qui sont l'unité de base de la BPE)   e ns arrondissements (qui sont l'unité de base du fichier de notes)


Le code Python est réparti dans différents fichiers Python et notebooks Jupyter. Il est recommandé de suivre l'ordre suivant pour l'éxecution du code :


### Partie 1 : Webscrapping et (...) 

1. ...
2. ...
3. ...


### Partie 2 : Zoom sur la culture

1. Cartes.ipynb 

Ce notebook utilise la librairie cartiflette pour visualiser les notes concernant la culture et le nombre de lieux culturels dans chaque arrondissement. Ces cartes nous donnent une première vision d'ensemble de la question.

2. analyse_descriptive.ipynb

Nous procédons ici à une analyse descriptive des notes moyennes données à la culture pour chaque arrondissement, et poussons l'analyse de comparaison avec le nombre de lieux culturels plus loin en s'intéressant désormais à la densité de lieux culturels par arrondissement. 



### Partie 3 : Corrélation entre les notes et le nombre d'équipements

1. Equipements.ipynb

Nous tentons d'établir des corrélations entre le nombre d'équipements et les notes données dans des thématiques variées : commerce, éducation, infrastructures de santé et moyens de transports. Pour cela, nous utilisons des régressions linéaires en essayant diverses variables explicatives à un niveau plus ou moins agrégé.
