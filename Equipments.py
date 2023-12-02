import pandas as pd
import requests
import io
import zipfile

########## We must get the IRIS corresponding with each arrondissement

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

########################################################################

##### Reading the file with information about equipments

dicType = {'BV2012': str, 'DCIRIS': str, 'DEP': str, 'DEPCOM': str, 'DOM': str, 'EPCI': str, 'SDOM': str}
file = pd.read_csv('bpe21_ensemble_xy.csv', sep=";", dtype = dicType)

BPE = file.copy()
BPE = BPE.loc[BPE['DEP'] == '75']

##### Number of "commerces alimentaires" (B2) by arrondissement

n1 = 0 # Number initialized
for iris in dicIRIS['Paris 1er Arrondissement']:
    # print(iris)
    col = BPE[(BPE['DCIRIS'] == iris) & (BPE['SDOM'] == 'B2')]
    # print(col)
    n1 += len(col) # number of lines
    # print(n1)

"""
print("Il y a " + str(n1) + " commerces alimentaires dans le 1er arrondissement.")
# We obtain 76
"""

dicB2 = {'1er Arrondissement': n1}

n = 0
for i in range(2,21):
    key_arr = 'Paris ' + str(i) + 'e Arrondissement'
    for iris in dicIRIS[key_arr]:
        col = BPE[(BPE['DCIRIS'] == iris) & (BPE['SDOM'] == 'B2')]
        n += len(col)
    dicB2[str(i) + 'e Arrondissement'] = n
    n = 0

"""
print(dicB2)
# key: number of arrondissement ; value: number of "commerce" alimentaires"
"""

##### Number of "Grandes surfaces" (B1) by arrondissement

n1 = 0 # Number initialized
for iris in dicIRIS['Paris 1er Arrondissement']:
    col = BPE[(BPE['DCIRIS'] == iris) & (BPE['SDOM'] == 'B1')]
    n1 += len(col)

dicB1 = {'1er Arrondissement': n1}

n = 0
for i in range(2,21):
    key_arr = 'Paris ' + str(i) + 'e Arrondissement'
    for iris in dicIRIS[key_arr]:
        col = BPE[(BPE['DCIRIS'] == iris) & (BPE['SDOM'] == 'B1')]
        n += len(col)
    dicB1[str(i) + 'e Arrondissement'] = n
    n = 0

########################################################################

##### Linear regression
Notes_arr = pd.read_excel('Notes_arrondissements.xlsx')

from sklearn.linear_model import LinearRegression
import numpy as np

listB1 = np.array(dicB1.values())
listB2 = np.array(dicB2.values())
B1_B2 = pd.concat([listB1,listB2], axis=1)
notes = pd.Series.tolist(Notes_arr['Commerces'])
reg = LinearRegression().fit(B1_B2, notes)



