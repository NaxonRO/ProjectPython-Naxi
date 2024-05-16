import pandas as pd
import matplotlib.pyplot as plt

#Luam din fisierul CSV
df = pd.read_csv("train.csv")

#Calculam procentul de supravietuire si nesupravietuitori
surv_procent = (df['Survived'].sum() / len(df)) * 100
nesupravietuitori = 100 - surv_procent

#Calculam procentul de pasageri pentru fiecare clasa
clasa_procent = df['Pclass'].value_counts() / len(df) * 100

#Calculul procentului de barbati si femei
gen_procent = df['Sex'].value_counts() / len(df) * 100

#Creare grafic
plt.figure()

#Procentul pentru pasagerii supravietuitori
plt.subplot(221)
plt.bar(['Supravietuitor', 'Nesupravietuitor'], [surv_procent, nesupravietuitori])
plt.title('Procentul de supravietuire')
plt.ylim(0, 100)

#Procentul pentru fiecare clasa
plt.subplot(222)
clasa_procent.plot(kind='bar')
plt.title('Procent per clasa')
plt.xlabel('Clasă')
plt.ylim(0, 100)

#Procentul sexului
plt.subplot(223)
gen_procent.plot(kind='bar')
plt.title("Procent sex")
plt.xlabel('Sex')
plt.ylim(0, 100)

#Afisare grafic
plt.tight_layout()
plt.show()