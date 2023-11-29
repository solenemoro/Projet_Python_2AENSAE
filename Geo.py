import pandas
import requests
import io
import zipfile

# We must get the IRIS corresponding with each arrondissement 

# We get the file containing matchings between arrondissements and IRIS

url_1 = 'https://www.insee.fr/fr/statistiques/fichier/2017499/reference_IRIS_geo2023.zip'

r1 = requests.get(url_1)
z1 = zipfile.ZipFile(io.BytesIO(r1.content))
z1.extractall()

import csv

"""
= pd.read_csv('bpe21_ensemble_xy.csv', sep=";")


with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
"""

"""
# Idea
LIBCOM == 'Paris 1er Arrondissement'
then add(CODE_IRIS)

"""

# 'Paris 1er Arrondissement' a traiter a part

liste = []
with open('reference_IRIS_geo2023.xlsx', newline='') as csvfile:
    for i in range(2,21):
            reader = csv.DictReader(csvfile)
            truc = []
            j = str(i)
            right_arr = 'Paris ' + j + 'e Arrondissement'
            for row in reader:
                if LIBCOM == right_arr:
                    truc.append( ['CODE_IRIS'])
            liste.append(truc)
            del(truc)

# Probleme ligne 44

