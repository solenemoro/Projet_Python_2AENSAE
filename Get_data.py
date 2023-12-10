# !pip install openpyxl
import pandas as pd
import requests
import io
import zipfile

# Reading the excel file containing a list of equipments and associated codes used by the Insee
pd.read_excel("https://www.insee.fr/fr/statistiques/fichier/3568650/BPE_gammes_2021_internet_v2.xlsx")

##### Reading the Zipfile with information about equipments in 2021

url = 'https://www.insee.fr/fr/statistiques/fichier/3568638/bpe21_ensemble_xy_csv.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
# We obtain two files

##### Reading the file with information about equipments

dicType = {'BV2012': str, 'DCIRIS': str, 'DEP': str, 'DEPCOM': str, 'DOM': str, 'EPCI': str, 'SDOM': str}
file = pd.read_csv('bpe21_ensemble_xy.csv', sep=";", dtype = dicType)
BPE = file.copy()

##### Reducing the file to keep only Paris

with open('bpeParis.csv','w') as f:
    f = BPE.loc[BPE['DEP'] == '75']
    f.to_csv('bpeParis.csv')

# Please delete csv files that are too big to push
# i.e. bpe21_ensemble_xy.csv and Varmod_bpe21_ensemble_xy.csv
