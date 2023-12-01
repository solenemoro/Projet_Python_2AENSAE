import pandas as pd
import requests
import io
import zipfile

file = pd.read_excel('reference_IRIS_geo2023.xlsx')
print(file.columns)

"""
# Results:
Index(['Liste des IRIS au 1er janvier 2023', 'Unnamed: 1', 'Unnamed: 2',
       'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7',
       'Unnamed: 8'],
      dtype='object')

# It's only on line 6 of the excel file that we find the right column names
"""
