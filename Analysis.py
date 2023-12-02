import pandas as pd

# How to analyze all these stuff

file = pd.read_csv('bpe21_ensemble_xy.csv', sep=";")

# print(BPE)

BPE = file.copy()

BPE = BPE.loc[BPE['DEP'] == 75]


# print(sortedBPE)

##### Number of "commerces alimentaires" (B2) by arrondissement

n = 0 # Number initialized
for iris in dicIRIS['Paris 1er Arrondissement']:
    col = BPE[(BPE['DCIRIS'] == iris) & (BPE[SDOM] == 'B2')]
    n += len(col) # number of lines
    






"""
import csv
with open('bpe21_ensemble_xy.csv', mode='+') as f:
    reader = csv.reader(f, delimiter=';') # , quoting=csv.QUOTE_NONE
    for row in reader:
        print(row)
"""



""""""""""""""" Problème résolu : les points-virgules

# print(sortedBPE.columns)

# We should have sth like that:
Index(['INSEE commune', 'Commune', 'Agriculture', 'Autres transports',
       'Autres transports international', 'CO2 biomasse hors-total', 'Déchets',
       'Energie', 'Industrie hors-énergie', 'Résidentiel', 'Routier',
       'Tertiaire'],
      dtype='object')
# But we have instead:
Index(['AAV2020;AN;BV2012;DEP;DEPCOM;DOM;EPCI;DCIRIS;LAMBERT_X;LAMBERT_Y;QP;QUALI_IRIS;QUALI_QP;QUALI_QVA;QUALI_ZFU;QUALI_ZUS;QUALITE_XY;QVA;REG;SDOM;TYPEQU;UU2020;ZFU;ZUS'], dtype='object')

# Only one column !


# print('DEP' in sortedBPE.columns) # False !

# Column = 'AAV2020;AN;BV2012;DEP;DEPCOM;DOM;EPCI;DCIRIS;LAMBERT_X;LAMBERT_Y;QP;QUALI_IRIS;QUALI_QP;QUALI_QVA;QUALI_ZFU;QUALI_ZUS;QUALITE_XY;QVA;REG;SDOM;TYPEQU;UU2020;ZFU;ZUS'
# Columns = Column.split(';')
# print(Columns)

# s = pd.Series(sortedBPE) # NO
# print(sortedBPE[Column])
# sortedBPE[Columns] = sortedBPE.str.split(';') # NO

# sortedBPE[Columns] = sortedBPE[Column].str.extract((';')) # NO


essai = sortedBPE[Column][1].split(';') # YES
print(essai)
"""


