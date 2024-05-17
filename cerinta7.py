import pandas as pd
import matplotlib.pyplot as plt

#Citim di fisierul CSV
df = pd.read_csv("train.csv")

#Facem variabilele care definesc copiii si adultii
copii = df[df['Age'] < 18]
adulti = df[df['Age'] >= 18]

#Calculam la fiecare categorie numarul total de participanti
nr_tot_cop = copii.shape[0]
nr_tot_ad = adulti.shape[0]

#Calculam procentul de copii
proc_cop = (nr_tot_cop / df.shape[0]) * 100

#Calculam rata de supravietuire
r_surv_cop = (copii['Survived'].sum() / nr_tot_cop) * 100
r_surv_ad = (adulti['Survived'].sum() / nr_tot_ad) * 100

#Creearea unui grafic pentru rata de suprav a adultilor si copiilor
lab = ['Copii', 'Adulti']
rate = [r_surv_cop, r_surv_ad]

plt.bar(lab, rate)
plt.title("Rata suprav")
plt.xlabel("Grupa varsta")
plt.ylabel("Rata suprav")
plt.ylim(0,100)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
