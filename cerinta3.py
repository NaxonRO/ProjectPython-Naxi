import pandas as pd
import matplotlib.pyplot as plt

#Citim din fisierul CSV
df = pd.read_csv("train.csv")

#Selectam coloanele numerice
coloana_numerica = df.select_dtypes(include=['int64', 'float64'])

#Crearea histogramelor pentru fiecare coloana numerica
for col in coloana_numerica.columns:
    plt.figure()
    #bins inseamna numarul de intervale in care sunt grupate
    #datele in histograma
    plt.hist(df[col].dropna(), bins=50)
    plt.title('Histograma pentru ' + col)
    plt.xlabel(col)
    plt.grid(True)
    plt.show()
