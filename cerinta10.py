import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Determinam starea de a fi singur
df['IsAlone'] = (df['SibSp'] + df['Parch'] == 0).astype(int)

#Creeam histograma pentru a vedea sansele de suprav
sns.histplot(data=df, x='IsAlone', hue='Survived', multiple='stack', discrete=True)
plt.title('Sansa suprav in fct de starea de a fi singur')
plt.xlabel('Este singur')
plt.ylabel('Numar de pasag')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Selectam primele 100 de inreg
df_100 = df.head(100)
sns.catplot(data=df_100, x='Pclass', y='Fare', hue='Survived', kind='swarm', size=3, height=6, aspect=1.5)
plt.title('Rel dintre tarif, clasa si stare surpav')
plt.xlabel('Clasa')
plt.ylabel('Tarif')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
