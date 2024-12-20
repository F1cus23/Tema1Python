import pandas as pd
import matplotlib.pyplot as plt

file_path = "data.csv"
data = pd.read_csv(file_path)

#Primul grafic
plt.figure
plt.plot(data['Durata'], label='Durata')
plt.plot(data['Puls'], label='Puls')
plt.plot(data['Calorii'], label = 'Calorii')
plt.plot(data['MaxPuls'], label = 'MaxPuls')
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend()
plt.show()  

#Al doilea grafic
X = 10
plt.figure
plt.plot(data['Durata'][:X], label='Durata', color = 'yellow')
plt.plot(data['Puls'][:X], label='Puls', color='red')
plt.plot(data['Calorii'][:X], label = 'Calorii', color = 'blue')
plt.plot(data['MaxPuls'][:X], label = 'MaxPuls', color = 'black')
plt.title(f"Primele {X} valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend()
plt.show()  

#Al treilea grafic
Y = 12
plt.figure
plt.plot(data['Durata'][-Y:], label='Durata')       
plt.plot(data['Puls'][-Y:], label='Puls')
plt.title(f"Ultimele {Y} valori pentru Durata și Puls")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend()
plt.show()  
