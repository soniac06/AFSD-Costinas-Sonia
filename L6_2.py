import random
import matplotlib.pyplot as plt

def genereaza_vector(n):
    return random.sample(range(1, n*10), n) #Alege exact n valori DIFERITE

def cautare_randomizata(vector, valoare_cautata): #caută elementul în ordine aleatoare
    indici=list(range(len(vector))) #Creează lista pozițiilor vectorului
    random.shuffle(indici)
    pasi=0 #Reține câte verificări face algoritmul
    for index in indici:
        pasi+=1
        if vector[index]==valoare_cautata:
            return index, pasi
    return -1, pasi

n=1000
vector=genereaza_vector(n)
valoare_cautata=random.choice(vector) #Alege aleator un element care există sigur în vector
print("Valoare căutată:", valoare_cautata)
numar_rulari=30
lista_pasi=[]
for i in range(numar_rulari):
    pozitie, pasi=cautare_randomizata(vector, valoare_cautata)
    lista_pasi.append(pasi)
    print(f"Rulare {i+1:<2} -> poziție = {pozitie:<4} pași = {pasi}")
minim=min(lista_pasi)
maxim=max(lista_pasi)
medie=sum(lista_pasi)/len(lista_pasi)
print("\nStatistici:")
print("Minim pași:", minim)
print("Maxim pași:", maxim)
print("Media pașilor:", round(medie, 2))
valori_n=[100, 1000, 10000]
medii=[]
for dim in valori_n:
    vector=genereaza_vector(dim)
    valoare=random.choice(vector)
    pasi_total=0
    for _ in range(30):
        _, pasi=cautare_randomizata(vector, valoare)
        pasi_total+=pasi
    medie=pasi_total/30
    medii.append(medie)

# Grafic 1
plt.figure(figsize=(8, 5))
plt.plot(range(1, numar_rulari + 1), lista_pasi, marker='o')
plt.xlabel('Rulare')
plt.ylabel('Număr pași')
plt.title('Pașii necesari pentru căutarea randomizată')
plt.grid(True)
plt.savefig('las_vegas_rulari.png')
plt.show()

# Grafic 2
plt.figure(figsize=(8, 5))
plt.plot(valori_n, medii, marker='o', label='Media pașilor')
plt.xlabel('Dimensiunea vectorului')
plt.ylabel('Număr mediu de pași')
plt.title('Media pașilor pentru dimensiuni diferite')
plt.legend()
plt.grid(True)
plt.savefig('las_vegas_medii.png')
plt.show()