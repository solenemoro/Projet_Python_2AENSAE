import pandas as pd
import requests
import io
import zipfile

"""
# Type in the terminal
pip install openpyxl
"""

# Lire le fichier excel
pd.read_excel("https://www.insee.fr/fr/statistiques/fichier/3568650/BPE_gammes_2021_internet_v2.xlsx")

##### Reading the Zipfile

# ZipInfo.filename("https://www.insee.fr/fr/statistiques/fichier/3568638/bpe21_ensemble_xy_csv.zip")
"""
doc = zipfile.ZipFile('https://www.insee.fr/fr/statistiques/fichier/3568638/bpe21_ensemble_xy_csv.zip', 'r')

zipfile.ZipFile.open('doc')
"""

# zipfile.extract

url = 'https://www.insee.fr/fr/statistiques/fichier/3568638/bpe21_ensemble_xy_csv.zip'

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

##### Reading the file with information about equipments

dicType = {'BV2012': str, 'DCIRIS': str, 'DEP': str, 'DEPCOM': str, 'DOM': str, 'EPCI': str, 'SDOM': str}
file = pd.read_csv('bpe21_ensemble_xy.csv', sep=";", dtype = dicType)
BPE = file.copy()

##### Reducing the file to keep only Paris

with open('bpeParis.csv','w') as f:
    f = BPE.loc[BPE['DEP'] == '75']
    f.to_csv('bpeParis.csv')

"""
# cf https://gist.github.com/ZeccaLehn/140edc75ff9d2c7cf9f660028763c9f5

# Delete csv files that are too big to push
"""

