import pandas as pd
import matplotlib.pyplot as plt

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Definim categoriile de varsta
categ_varsta = [(0, 20), (21, 40), (41, 60), (61, df['Age'].max())]
categ = ['[0,20]', '[21,40]', '[41,60]', '[61,max]']

#Calculam barbatii supravietuitori
barb_sup = []
for minim, maxim in categ_varsta:
    nr_sup = df[(df['Age'] >= minim) & (df['Age'] <= maxim) & (df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
    barb_sup.append(nr_sup)

#Calculam barbatii totali
barb_tot = []
for minim, maxim in categ_varsta:
    nr_barb = df[(df['Age'] >= minim) & (df['Age'] <= maxim) & (df['Sex'] == 'male')].shape[0]
    barb_tot.append(nr_barb)

#Calculam procentul supravietuitorilo
proc = [supravietuitori * 100 / total if total != 0 else 0 for supravietuitori, total in zip(barb_sup, barb_tot)]

#Creeam graficul
plt.bar(categ, proc)
plt.title("Procentul de supraviețuire al bărbaților pe categorii de vârstă")
plt.xlabel("Categorie vârstă")
plt.ylabel("Procent supraviețuire")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
