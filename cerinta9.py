import pandas as pd
import matplotlib.pyplot as plt

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Extragem toate titlurile din coloana "Name"
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

#Definim dictionarul pentru map
titlu_map = {
    'Mr': 'male', 'Master': 'male', 'Don': 'male', 'Rev': 'male', 'Dr': 'male', 'Major': 'male',
    'Sir': 'male', 'Col': 'male', 'Capt': 'male', 'Jonkheer': 'male',
    'Mrs': 'female', 'Miss': 'female', 'Mme': 'female', 'Ms': 'female', 'Lady': 'female',
    'Mlle': 'female', 'Countess': 'female', 'Dona': 'female'
}

#Verificam corectitudinea titlurilor
df['Title_Correct'] = df.apply(lambda row: titlu_map.get(row['Title']) == row['Sex'], axis=1)

#Numaram cate persoane corespund fiecarui titlu
nr_tit = df['Title'].value_counts()

#Verificam cate titluri sunt corecte si cate gresite
tit_corect = df['Title_Correct'].value_counts()
print(tit_corect)

#Afisam pers cu tit incor
tit_incor = df[~df['Title_Correct']]
print(tit_incor[['Name', 'Title', 'Sex']])

#Cream graficul cu numarul de pers pt fiec tit
nr_tit.plot(kind='bar')
plt.title("Numar pers per tit")
plt.xlabel('Titlu')
plt.ylabel('Numar pers')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
