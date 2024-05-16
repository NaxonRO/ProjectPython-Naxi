import pandas as pd

#Citim dim fisierul CSV
df = pd.read_csv("train.csv")

#Vedem care coloane au valori lipsa si determinam numarul acestora
valoare_lipsa = df.isnull().sum()
valoare_lipsa = valoare_lipsa[valoare_lipsa > 0]
prop = (valoare_lipsa / len(df)) * 100

#Printam coloanele cu valori lipsa
print("\n\n\n")
print("Coloanele cu valori lipsa:")
print(valoare_lipsa)

#Printam numarul si proportia valorilor lipsa
print("\n\n\n")
print("Numarul si proportia valorilor lipsa:")
print(prop)

#Dterminam procentul de valori lipsa
surv = df[df['Survived'] == 1].isnull().sum() / len(df[df['Survived'] == 1]) * 100
nesurv = df[df['Survived'] == 0].isnull().sum() / len(df[df['Survived'] == 0]) * 100

#Scoatem coloanele care au 0 la procent
surv = surv[surv > 0]
nesurv = nesurv[nesurv > 0]

#Printam procentul valorilor lipsa pentru clasa surv = 1
print("\n\n\n")
print("Procent valori lipsa surv == 1")
print(surv)

#Printam procentul valorilor lipsa pentru clasa surv = 0
print("\n\n\n")
print("Procent valori lipsa surv == 0")
print(nesurv)
