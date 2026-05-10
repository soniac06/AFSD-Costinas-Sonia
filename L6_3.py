import random
import matplotlib.pyplot as plt

candidati=[
    ("Ana", 3000, 90),
    ("Bogdan", 2500, 75),
    ("Maria", 4000, 95),
    ("Dan", 2000, 60),
    ("Elena", 3500, 85),
    ("Ioana", 2800, 70),
    ("George", 3200, 88),
    ("Giulia", 1500, 50),
    ("Filip", 2700, 72),
    ("Rares", 3300, 80)
]
BUGET_MAXIM=15000
print("Lista candidaților:\n")
for nume, cost, scor in candidati:
    print(f"{nume:<10} cost={cost:<5} scor={scor}")
print("\nBuget maxim:", BUGET_MAXIM)
print("-" * 40)
NUMAR_GENE=len(candidati)
POPULATIE=50
GENERATII=100
RATA_MUTATIE=0.05
def cromozom_random():
    return [random.randint(0, 1) for _ in range(NUMAR_GENE)]

def fitness(cromozom):
    cost_total=0
    scor_total=0
    for gena, candidat in zip(cromozom, candidati):
        nume, cost, scor=candidat
        if gena==1:
            cost_total+=cost
            scor_total+=scor
    if cost_total>BUGET_MAXIM:
        return 0
    return scor_total

def selectie(populatie):
    a=random.choice(populatie)
    b=random.choice(populatie)
    if fitness(a)>fitness(b):
        return a
    return b

def crossover(parinte1, parinte2):
    punct=random.randint(1, NUMAR_GENE-1)
    copil=parinte1[:punct]+parinte2[punct:]
    return copil

def mutatie(cromozom):
    for i in range(NUMAR_GENE):
        if random.random()<RATA_MUTATIE:
            cromozom[i]=1-cromozom[i]

populatie=[cromozom_random() for _ in range(POPULATIE)]
best_global=max(populatie, key=fitness)
istoric_best=[]
istoric_medie=[]
for generatie in range(GENERATII):
    fitnessuri=[fitness(c) for c in populatie]
    best=max(fitnessuri)
    medie=sum(fitnessuri)/len(fitnessuri)
    istoric_best.append(best)
    istoric_medie.append(medie)
    generatie_best=max(populatie, key=fitness)
    if fitness(generatie_best)>fitness(best_global):
        best_global=generatie_best[:]
    populatie_noua=[]
    for _ in range(POPULATIE):
        p1=selectie(populatie)
        p2=selectie(populatie)
        copil=crossover(p1, p2)
        mutatie(copil)
        populatie_noua.append(copil)
    populatie=populatie_noua
cea_mai_buna=best_global
print("Cea mai bună echipă găsită:\n")
cost_total=0
scor_total=0
for gena, candidat in zip(cea_mai_buna, candidati):
    nume, cost, scor=candidat
    if gena==1:
        print(f"{nume:<10} cost={cost:<5} scor={scor}")
        cost_total+=cost
        scor_total+=scor
print("\nCost total:", cost_total)
print("Scor total:", scor_total)
print("Buget maxim:", BUGET_MAXIM)
if cost_total<=BUGET_MAXIM:
    print("Buget respectat")
else:
    print("Buget depasit")
plt.figure(figsize=(8, 5))
plt.plot(istoric_best, label='Fitness maxim')
plt.plot(istoric_medie, label='Fitness mediu')
plt.xlabel('Generație')
plt.ylabel('Fitness')
plt.title('Evoluția algoritmului genetic')
plt.legend()
plt.grid(True)
plt.savefig('algoritm_genetic.png')
plt.show()