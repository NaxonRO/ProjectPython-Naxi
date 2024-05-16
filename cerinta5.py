import pandas as pd
import matplotlib.pyplot as plt

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Definim categoriile de varsta
categ_varsta = [(0, 20), (21, 40), (41, 60), (61, df['Age'].max())]
categ = ['[0,20]', '[21,40]', '[41,60]', '[61,max]']

#Adaugam o coloana suplimentara pentru categoria de varsta
df['Categorie_de_varsta'] = ''

#Calculam numar pasageri per categorie
pasag_categ = []
for minim, maxim in categ_varsta:
    numar_pasageri = df[(df['Age'] >= minim) & (df['Age'] <= maxim)].shape[0]
    pasag_categ.append(numar_pasageri)

#Cream graficul
plt.bar(categ, pasag_categ)
plt.title("Număr de pasageri per categorie de vârstă")
plt.xlabel("Categorie vârstă")
plt.ylabel("Nr. pasageri")
plt.grid(axis='y')
plt.tight_layout()
plt.show()