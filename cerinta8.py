import pandas as pd

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Calculam media si modulul
varsta_med = df.groupby(['Pclass', 'Survived'])['Age'].mean()
tarif_med = df.groupby(['Pclass', 'Survived'])['Fare'].mean()
mod_cab = df.groupby(['Pclass', 'Survived'])['Cabin'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else 'U')
mod_imbarc = df.groupby(['Pclass', 'Survived'])['Embarked'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else 'S')

#Functia pentru complet val col num
def umplere(row, col, med):
    if pd.isnull(row[col]):
        return med.loc[row['Pclass'], row['Survived']]
    else:
        return row[col]

#Functia pentru complet val col categ
def umplere_categ(row, col, med):
    if pd.isnull(row[col]):
        return med.loc[row['Pclass'], row['Survived']]
    else:
        return row[col]

#Completam valori lipsa ptr col num
df['Age'] = df.apply(lambda row: umplere(row, 'Age', varsta_med), axis=1)
df['Fare'] = df.apply(lambda row: umplere(row, 'Fare', tarif_med), axis=1)

#Completare val lipsa ptr col categ
df['Cabin'] = df.apply(lambda row: umplere_categ(row, 'Cabin', mod_cab), axis=1)
df['Embarked'] = df.apply(lambda row: umplere_categ(row, 'Embarked', mod_imbarc), axis=1)

#Verificam daca mai sunt valori care lipsesc
print(df.isnull().sum())
