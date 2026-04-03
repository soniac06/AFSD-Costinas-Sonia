import time
import csv
import random

def este_sortata(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

def rezultate_identice(lista1, lista2):
    if len(lista1)!=len(lista2):
        return False
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            return False
    return True

def statistici_noi():
    return {
        "comparatii": 0,
        "mutari": 0,
        "apeluri_recursive": 0
    }

def bubble_sort(lista):
    statistici=statistici_noi()
    n=len(lista)
    schimbat=True
    while schimbat:
        schimbat=False
        for i in range(n-1):
            statistici["comparatii"]+=1
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1]=lista[i+1], lista[i]
                statistici["mutari"]+=3
                schimbat=True
        n-=1
    return lista, statistici

def imparte_lista(lista, stanga, dreapta, statistici):
    pozitie_pivot=random.randint(stanga, dreapta)
    lista[pozitie_pivot], lista[dreapta]=lista[dreapta], lista[pozitie_pivot]
    statistici["mutari"]+=3
    pivot=lista[dreapta]
    i=stanga-1
    for j in range(stanga, dreapta):
        statistici["comparatii"]+=1
        if lista[j]<=pivot:
            i+=1
            if i!=j:
                lista[i], lista[j]=lista[j], lista[i]
                statistici["mutari"]+=3
    if i+1!=dreapta:
        lista[i+1], lista[dreapta]=lista[dreapta], lista[i+1]
        statistici["mutari"]+=3
    return i+1
def quick_sort(lista, stanga=0, dreapta=None, statistici=None):
    if dreapta is None:
        dreapta=len(lista)-1
    if statistici is None:
        statistici=statistici_noi()
    statistici["apeluri_recursive"]+=1
    if stanga<dreapta:
        pozitie_pivot=imparte_lista(lista, stanga, dreapta, statistici)
        quick_sort(lista, stanga, pozitie_pivot-1, statistici)
        quick_sort(lista, pozitie_pivot+1, dreapta, statistici)
    return lista, statistici

def interclasare(stanga, dreapta, statistici):
    rezultat=[]
    i=0
    j=0
    while i<len(stanga) and j<len(dreapta):
        statistici["comparatii"]+=1
        if stanga[i]<=dreapta[j]:
            rezultat.append(stanga[i])
            i+=1
            statistici["mutari"]+=1
        else:
            rezultat.append(dreapta[j])
            j+=1
            statistici["mutari"]+=1
    while i<len(stanga):
        rezultat.append(stanga[i])
        i+=1
        statistici["mutari"]+=1
    while j<len(dreapta):
        rezultat.append(dreapta[j])
        j+=1
        statistici["mutari"]+=1
    return rezultat
def merge_sort(lista, statistici=None):
    if statistici is None:
        statistici=statistici_noi()
    statistici["apeluri_recursive"]+=1
    if len(lista)<=1:
        return lista, statistici
    mijloc=len(lista)//2
    stanga=lista[:mijloc]
    dreapta=lista[mijloc:]
    partea_stanga, statistici=merge_sort(stanga, statistici)
    partea_dreapta, statistici=merge_sort(dreapta, statistici)
    rezultat=interclasare(partea_stanga, partea_dreapta, statistici)
    return rezultat, statistici

def genereaza_lista(n, tip):
    if tip=="aleator":
        lista=[]
        for i in range(n):
            lista.append(random.randint(0, 10000))
        return lista
    elif tip=="sortat_crescator":
        lista=[]
        for i in range(n):
            lista.append(i)
        return lista
    elif tip=="sortat_descrescator":
        lista=[]
        for i in range(n, 0, -1):
            lista.append(i)
        return lista
    elif tip=="multe_duplicate":
        lista=[]
        for i in range(n):
            lista.append(random.randint(0, 10))
        return lista
    elif tip=="aproape_sortat":
        lista=[]
        for i in range(n):
            lista.append(i)
        numar_schimbari=max(1, n//20)
        for k in range(numar_schimbari):
            i=random.randint(0, n - 1)
            j=random.randint(0, n - 1)
            lista[i], lista[j]=lista[j], lista[i]
        return lista
    else:
        raise ValueError("Tip de intrare necunoscut.")

def ruleaza_teste():
    random.seed(42)
    dimensiuni=[100, 500, 1000, 2000, 5000]
    tipuri=["aleator", "sortat_crescator", "sortat_descrescator", "multe_duplicate", "aproape_sortat"]
    rulari=3
    algoritmi=[
        ("Bubble Sort", bubble_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort)
    ]
    rezultate=[]
    for n in dimensiuni:
        for tip in tipuri:
            totaluri={}
            for nume_algoritm, _ in algoritmi:
                totaluri[nume_algoritm]={
                    "timp": 0,
                    "comparatii": 0,
                    "mutari": 0,
                    "apeluri": 0
                }
            test_valid=True
            for _ in range(rulari):
                lista_initiala=genereaza_lista(n, tip)
                rezultat_referinta=None
                for nume_algoritm, functie in algoritmi:
                    copie=lista_initiala.copy()
                    start=time.time()
                    rezultat, statistici=functie(copie)
                    end=time.time()
                    if not este_sortata(rezultat):
                        print(f"Eroare: {nume_algoritm} nu sorteaza corect pentru n={n}, tip={tip}")
                        test_valid=False
                        break
                    if rezultat_referinta is None:
                        rezultat_referinta=rezultat.copy()
                    elif not rezultate_identice(rezultat, rezultat_referinta):
                        print(f"Eroare: {nume_algoritm} produce rezultat diferit pentru n={n}, tip={tip}")
                        test_valid=False
                        break
                    totaluri[nume_algoritm]["timp"]+=(end-start)
                    totaluri[nume_algoritm]["comparatii"]+=statistici["comparatii"]
                    totaluri[nume_algoritm]["mutari"]+=statistici["mutari"]
                    totaluri[nume_algoritm]["apeluri"]+=statistici["apeluri_recursive"]
                if not test_valid:
                    break
            if test_valid:
                for nume_algoritm, _ in algoritmi:
                    rezultate.append([
                        nume_algoritm,
                        n,
                        tip,
                        totaluri[nume_algoritm]["timp"] / rulari,
                        totaluri[nume_algoritm]["comparatii"] / rulari,
                        totaluri[nume_algoritm]["mutari"] / rulari,
                        totaluri[nume_algoritm]["apeluri"] / rulari
                    ])
    return rezultate

def afiseaza_rezultate(rezultate):
    print(f"{'Algoritm':<12} {'Dimensiune':<10} {'Intrare':<20} {'Timp mediu':<12} {'Comparatii':<12} {'Mutari':<12} {'Apeluri':<12}")
    print("-"*90)
    for rezultat in rezultate:
        nume_algoritm=rezultat[0]
        dimensiune=rezultat[1]
        tip_intrare=rezultat[2]
        timp_mediu=rezultat[3]
        comparatii=rezultat[4]
        mutari=rezultat[5]
        apeluri=rezultat[6]
        print(f"{nume_algoritm:<12} {dimensiune:<10} {tip_intrare:<20} {timp_mediu:<12.6f} {comparatii:<12.2f} {mutari:<12.2f} {apeluri:<12.2f}")

def salveaza_csv(rezultate, nume_fisier="rezultate_sortare.csv"):
    with open(nume_fisier, "w", newline="") as fisier:
        writer=csv.writer(fisier)
        writer.writerow([
            "Algoritm",
            "Dimensiune",
            "Intrare",
            "Timp mediu",
            "Comparatii",
            "Mutari",
            "Apeluri recursive"
        ])
        writer.writerows(rezultate)

rezultate=ruleaza_teste()
afiseaza_rezultate(rezultate)
salveaza_csv(rezultate)