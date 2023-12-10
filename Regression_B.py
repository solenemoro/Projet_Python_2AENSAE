import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

##### Reading the excel file containing the grades obtained by each arrondissement in varied fields

Notes_arr = pd.read_excel('Notes_arrondissements.xlsx')
notes = pd.Series(Notes_arr['Commerces'])
notes = notes.str.replace(',', '.')
notes = pd.Series.tolist(notes)

Commerces = pd.read_csv('Commerces.csv')

# Splitting the group in 2

# Split the data into training/testing sets
Commerces2 = Commerces.transpose()
X_train = Commerces2[:-10]
print(X_train)
X_test = Commerces2[-10:]

# Split the targets into training/testing sets
y_train = notes[:-10]
print(y_train)
y_test = notes[-10:]

reg = LinearRegression().fit(X_train, y_train)

# Make predictions using the testing set
y_pred = reg.predict(X_test)

# The coefficients
print("Coefficients: \n", reg.coef_)
# The mean squared error
# print("Mean squared error: \n", sklearn.metrics.mean_squared_error(y_test, y_pred))
# Problem: needs numeric
# The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: \n", sklearn.metrics.r2_score(y_test, y_pred))

# disp = sklearn.metrics.PredictionErrorDisplay.from_predictions(y_test, y_pred)
# plt.savefig('Prediction Error for B')
# plt.close()

# Nichts......

"""
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred2, color="blue", linewidth=3)
plt.xlabel('Nombre de commerces alimentaires')
plt.ylabel('Note donnée par les habitants')
plt.title('Une 2ème régression')
plt.savefig('Une 2ème régression')
"""
