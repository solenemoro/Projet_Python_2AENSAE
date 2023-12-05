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

dicType = {'BV2012': str, 'DCIRIS': str, 'DEP': str, 'DEPCOM': str, 'DOM': str, 'EPCI': str, 'SDOM': str}
BPE = pd.read_csv('bpeParis.csv', sep=",", dtype = dicType)

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
# key: number of arrondissement ; value: number of "commerces alimentaires"
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

########## Linear regression

"""
Notes_arr = pd.read_excel('Notes_arrondissements.xlsx')

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

listB1 = pd.DataFrame(dicB1.values())
listB2 = pd.DataFrame(dicB2.values())
B1_B2 = pd.concat([listB1,listB2], axis=1)
notes = pd.Series(Notes_arr['Commerces'])
notes = notes.str.replace(',', '.')
notes = pd.Series.tolist(notes)

##### Only with B2

reg = LinearRegression().fit(listB2, notes)

y_pred = reg.predict(listB2)

plt.scatter(listB2, notes, color="black")
plt.plot(listB2, y_pred, color="blue", linewidth=3)
plt.xlabel('Nombre de commerces alimentaires')
plt.ylabel('Note donnée par les habitants')
plt.title('Une régression')
plt.savefig('Une régression')
plt.close()
"""

"""
plt.show() # Seems useless

# Not very satisfactory since y_pred is surprisingly decreasing
"""

"""
# Splitting the group in 2

# Split the data into training/testing sets
X_train = listB2[:-10]
X_test = listB2[-10:]

# Split the targets into training/testing sets
y_train = notes[:-10]
y_test = notes[-10:]

reg = LinearRegression().fit(X_train, y_train)

# Make predictions using the testing set
y_pred2 = reg.predict(X_test)

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred2, color="blue", linewidth=3)
plt.xlabel('Nombre de commerces alimentaires')
plt.ylabel('Note donnée par les habitants')
plt.title('Une 2ème régression')
plt.savefig('Une 2ème régression')
plt.close()
"""

##### Regression with B1 and B2

"""
# Split the data into training/testing sets
X_train = B1_B2[:-10]
X_test = B1_B2[-10:]

# Split the targets into training/testing sets
y_train = notes[:-10]
y_test = notes[-10:]

reg = LinearRegression().fit(X_train, y_train)

# Make predictions using the testing set
y_pred = reg.predict(X_test)

# Plot outputs
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

"""

##### Idea: industrializing to have all types of equipments concerned by B, i.e. "commerces"

##### Number of each type of commerce by arrondissement

n1 = 0 # Number initialized

"""
listType = []
for j in range(1,4):
    type = B10 + str
"""

listType = ['B101', 'B102', 'B103', 'B201', 'B202', 'B203', 'B204', 'B205', 'B206', 'B301', 'B302', 'B303', 'B304', 'B305', 'B306', 'B307', 'B308', 'B309', 'B310', 'B311', 'B312', 'B313', 'B314', 'B315', 'B316']

list1 = []
for type in listType:
    for iris in dicIRIS['Paris 1er Arrondissement']:
        col = BPE[(BPE['DCIRIS'] == iris) & (BPE['TYPEQU'] == type)]
        n1 += len(col) # number of lines
    list1.append(n1)
    n1 = 0

dicB = {'1er Arrondissement': list1}

n = 0
for arr in range(2,21):
    key_arr = 'Paris ' + str(arr) + 'e Arrondissement'
    listBType = []
    for type in listType:
        for iris in dicIRIS[key_arr]:
            col = BPE[(BPE['DCIRIS'] == iris) & (BPE['TYPEQU'] == type)]
            n += len(col)
        listBType.append(n)
        n = 0
    dicB[str(arr) + 'e Arrondissement'] = listBType


Commerces_precis = pd.DataFrame(dicB)
Commerces_precis.set_axis(listType, axis = 0)
Commerces_precis.to_csv('Commerces.csv', index = False)

"""
print("Il y a " + str(n1) + " commerces alimentaires dans le 1er arrondissement.")
# We obtain 
"""

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

"""
print(dicB2)
# key: number of arrondissement ; value: number of "commerce" alimentaires"
"""





