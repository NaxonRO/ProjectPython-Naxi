import pandas as pd

# Citim din train.csv
df = pd.read_csv("train.csv")

#Afisam din train.csv cateva linii si coloane de la inceput
print("Primele randuri din fisierul train:")
print(df.head())


#Numaram cate coloane sunt in train
print("\n\n\n")
numar_coloane = len(df.columns)
print("Numarul de coloane din train", numar_coloane)

#Ne uitam sa vedem ce tipuri de elemente sunt pe fiecare coloana din train
print("\n\n\n")
print("Ce tipuri de date se afla pe prima coloana:", df.dtypes)

#Vedem numarul de valori lipsa
print("\n\n\n")
print("Numarul de valori lipsa pentru fiecare coloana:")
print(df.isnull().sum())

#Numaram numarul de linii
print("\n\n\n")
numar_linii = len(df)
print("Numarul de linii:", numar_linii)

#Vedem daca avem duplicate in train.csv
print("\n\n\n")
duplic = df.duplicated().sum()
if duplic > 0:
    print("Numarul de linii duplicate:", duplic)
else:
    print("Nu exista linii duplicate in train")
