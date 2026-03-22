import csv
import json

def citeste_produse_csv(fisier):
    produse={}
    with open(fisier, 'r', newline='') as csvfile:
        reader=csv.reader(csvfile)
        for linie in reader:
            if linie[0]=="id":
                continue
            id_produs=linie[0]
            nume=linie[1]
            pret=float(linie[2])
            stoc=int(linie[3])
            produse[id_produs]={
                "nume": nume,
                "pret": pret,
                "stoc": stoc
            }
    return produse

def citeste_reduceri_json(fisier):
    with open(fisier, "r") as jsonfile:
        reduceri=json.load(jsonfile)
    return reduceri

def afiseaza_meniu(produse):
    print("\n--- MENIU PRODUSE ---")
    for id_produs in produse:
        print(id_produs, produse[id_produs]["nume"], produse[id_produs]["pret"], produse[id_produs]["stoc"])

def adauga_produs(comanda, produse, id_produs, cantitate):
    id_produs=str(id_produs)
    if id_produs not in produse:
        print("Id produs invalid")
        return
    if cantitate<=0:
        print("Cantitate invalida")
        return
    if id_produs in comanda:
        deja_comandat=comanda[id_produs]
    else:
        deja_comandat=0
    stoc_disponibil=produse[id_produs]["stoc"]-deja_comandat
    if cantitate>stoc_disponibil:
        print("Stoc insuficient")
        return
    comanda[id_produs]=cantitate+deja_comandat
    print("Produsul a fost adaugat in comanda")

def scade_produs(comanda, id_produs, cantitate):
    id_produs=str(id_produs)
    if id_produs not in comanda:
        print("Produsul nu se afla in comanda")
        return
    if cantitate<=0:
        print("Cantitate invalida")
        return
    if cantitate>comanda[id_produs]:
        print("Cantitate invalida")
        return
    comanda[id_produs]-=cantitate
    if comanda[id_produs]==0:
        del(comanda[id_produs])
        print("Produsul a fost eliminat din comanda")
    else:
        print("Cantitate actualizata")

def calculeaza_total(comanda, produse):
    total=0
    for id_produs, cantitate in comanda.items():
        total+=cantitate*produse[str(id_produs)]["pret"]
    return total

def calculeaza_reducere(total, tip_reducere, reduceri):
    if tip_reducere=="":
        return 0
    prag=reduceri[tip_reducere]["prag"]
    tip=reduceri[tip_reducere]["tip"]
    valoare=reduceri[tip_reducere]["valoare"]
    if total<prag:
        print("Total insuficient")
        return 0
    if tip=="procent":
        reducere=total*valoare/100
    else:
        reducere=valoare
    if reducere>total:
        reducere=total
    return reducere

def genereaza_bon(comanda, produse, total, reducere):
    text_bon=""
    for id_produs in comanda:
        cantitate=comanda[id_produs]
        pret=produse[id_produs]["pret"]
        nume=produse[id_produs]["nume"]
        subtotal=cantitate*pret
        linie=nume+" x "+str(cantitate)+" = "+str(subtotal)+" lei\n"
        text_bon+=linie
    total_final=total-reducere
    text_bon+="Total : "+str(total)+" lei\n"
    text_bon+="Reducere : "+str(reducere)+" lei\n"
    text_bon+="Total final : "+str(total_final)+" lei\n"
    return text_bon

def scrie_bon_txt(fisier, text_bon):
    with open(fisier, "w") as f:
        f.write(text_bon)
    print(f"Bonul a fost salvat in fisierul {fisier}")

def goleste_comanda(comanda):
    comanda.clear()

if __name__=='__main__':
    produse=citeste_produse_csv("produse.csv")
    reduceri=citeste_reduceri_json("reduceri.json")
    comanda={}
    reducere_curenta=""
    while True:
        print("1 - Afisare meniu produse")
        print("2 - Adaugare produs in comanda")
        print("3 - Scadere/eliminare produs din comanda")
        print("4 - Aplicare reducere")
        print("5 - Finalizare comanda")
        print("6 - Anulare comanda")
        print("0 - Iesire")
        optiune=input("Optiunea aleasa este : ")
        if optiune=="1":
            afisare_meniu(produse)
        elif optiune=="2":
            id_produs=int(input("Index produs : "))
            cant=int(input("Cantitate : "))
            adauga_produs(comanda, produse, id_produs, cant)
        elif optiune=="3":
            id_produs=int(input("Index produs : "))
            cant=int(input("Cantitate : "))
            scade_produs(comanda, id_produs, cant)
        elif optiune=="4":
            total=calculeaza_total(comanda, produse)
            if total==0:
                print("Comanda este goala")
            else:
                print("1 - student")
                print("2 - happy")
                print("3 - cupon")
                print("4 - fara reducere")
                print("0 - inapoi")
                opt=input("Alege reducerea : ")
                if opt=="1":
                    reducere_curenta="student"
                    reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
                    print("Reducere aplicata:", reducere, "lei")
                elif opt=="2":
                    reducere_curenta="happy"
                    reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
                    print("Reducere aplicata:", reducere, "lei")
                elif opt=="3":
                    reducere_curenta="cupon"
                    reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
                    print("Reducere aplicata:", reducere, "lei")
                elif opt=="4":
                    reducere_curenta = ""
                    print("Fara reducere")
                elif opt=="0":
                    print("Revenire la meniul principal")
                else:
                    print("Optiune invalida")
        elif optiune=="5":
            total=calculeaza_total(comanda, produse)
            if total==0:
                print("Comanda este goala")
            else:
                reducere=calculeaza_reducere(total, reducere_curenta, reduceri)
                bon=genereaza_bon(comanda, produse, total, reducere)
                print("\n--- BON ---")
                print(bon)
                scrie_bon_txt("bon.txt", bon)
                for id_produs in comanda:
                    produse[id_produs]["stoc"]-=comanda[id_produs]
                goleste_comanda(comanda)
                reducere_curenta=""
        elif optiune=="6":
            goleste_comanda(comanda)
            reducere_curenta=""
            print("Comanda anulata")
        elif optiune=="0":
            print("Program inchis")
            break
        else:
            print("Optiune invalida")