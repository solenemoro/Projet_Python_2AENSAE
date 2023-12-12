import pandas as pd
import requests
import io
import zipfile

##### We must get the IRIS corresponding with each arrondissement 

##### Getting the file containing matchings between arrondissements and IRIS

url_1 = 'https://www.insee.fr/fr/statistiques/fichier/2017499/reference_IRIS_geo2023.zip'

r1 = requests.get(url_1)
z1 = zipfile.ZipFile(io.BytesIO(r1.content))
z1.extractall()

file = pd.read_excel('reference_IRIS_geo2023.xlsx')

##### Changing the names of the columns

"""
print(file.columns)
# Results:
Index(['Liste des IRIS au 1er janvier 2023', 'Unnamed: 1', 'Unnamed: 2',
       'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7',
       'Unnamed: 8'],
      dtype='object')

# It is only on line 6 of the excel file that we find the right column names
"""

wrong_names = pd.Series.tolist(file.columns)
col_names = pd.Series.tolist(file.iloc[4])
dictionary = dict(zip(wrong_names, col_names))

file = file.rename(columns = dictionary)

"""
print(file.columns)
# We obtain the right names of columns
"""

##### Obtaining a list with IRIS in the 1st arrondissement of Paris

Arr1 = file[file['LIBCOM'] == 'Paris 1er Arrondissement']
liste1 = pd.Series.tolist(Arr1['CODE_IRIS'])
print(liste1)

##### The same with all the other arrondissements

dicIRIS = {'Paris 1er Arrondissement': liste1}

for i in range(2,21):
    j = str(i)
    key_arr = 'Paris ' + j + 'e Arrondissement'
    Arr = file[file['LIBCOM'] == key_arr]
    val_arr = pd.Series.tolist(Arr['CODE_IRIS'])
    dicIRIS[key_arr] = val_arr

"""
print(dicIRIS)
# We obtain a dictionary with the name of the arrondissement as a key 
# and a list with the numbers of IRIS corresponding as a value
"""
