import pandas as pd

# How to analyze all this stuff

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



