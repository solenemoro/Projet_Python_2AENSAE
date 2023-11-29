import pandas
import requests
import io
import zipfile

"""
# Type in the terminal
pip install openpyxl
"""

# Lire le fichier excel
pandas.read_excel("https://www.insee.fr/fr/statistiques/fichier/3568650/BPE_gammes_2021_internet_v2.xlsx")

# Zipfile

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


"""
# cf https://gist.github.com/ZeccaLehn/140edc75ff9d2c7cf9f660028763c9f5

# Delete both csv file which are too big to push
"""

