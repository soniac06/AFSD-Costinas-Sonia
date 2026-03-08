produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]
reducere_curenta = 0
tip_reducere=None

def afisare_meniu(produse, preturi, stoc):
    for i in range(len(produse)):
        print(i, produse[i], preturi[i], stoc[i])

def adaugare_produs(cant_comanda, stoc, index, cantitate):
    if index<0 or index>=len(cant_comanda):
        print("Index invalid")
        return
    if cantitate<=0:
        print("Cantitate invalida")
        return
    stoc_disponibil=stoc[index]-cant_comanda[index]
    if cantitate>stoc_disponibil:
        print("Stoc insuficient")
        return
    cant_comanda[index]+=cantitate

def scadere_produs(cant_comanda, index, cantitate):
    if index<0 or index>=len(cant_comanda):
        print("Index invalid")
        return
    if cantitate<=0:
        print("Cantitate invalida")
        return
    if cantitate>cant_comanda[index]:
        print("Cantitate invalida")
        return
    cant_comanda[index]-=cantitate

def calcul_total(cant_comanda, preturi):
    total=0
    for i in range(len(cant_comanda)):
        total+=cant_comanda[i]*preturi[i]
    return total

def stabilire_reducere(total, tip_reducere):
    reducere=0
    if tip_reducere=="student":
        if total>=30:
            reducere=total*0.10
        else:
            print("Total insuficient pentru student")
    elif tip_reducere=="happy":
        if total>=50:
            reducere=total*0.15
        else:
            print("Total insuficient pentru happy")
    elif tip_reducere=="cupon":
        if total>=25:
            reducere=7.0
        else:
            print("Total insuficient pentru cupon")
    if reducere>total:
        reducere=total
    return reducere

def afiseaza_bon(produse, preturi, cant_comanda, reducere):
    total=0
    for i in range(len(produse)):
        if cant_comanda[i]>0:
            subtotal=cant_comanda[i]*preturi[i]
            total+=subtotal
            print(produse[i], "x", cant_comanda[i], "=", subtotal, "lei")
    total_final=total-reducere
    print("Total : ", total, "lei")
    print("Reducere : ", reducere, "lei")
    print("Total final : ", total_final, "lei")

def finalizare_comanda(stoc, cant_comanda):
    for i in range(len(stoc)):
        stoc[i]-=cant_comanda[i]
        cant_comanda[i]=0

def anulare_comanda(cant_comanda):
    for i in range(len(cant_comanda)):
        cant_comanda[i]=0

while True:
    print("1. Afisare meniu produse")
    print("2. Adaugare produs")
    print("3. Scadere produs")
    print("4. Aplicare reducere")
    print("5. Finalizare comanda")
    print("6. Anulare comanda")
    print("0. Iesire")
    optiune=input("Optiunea aleasa este : ")
    if optiune=="1":
        afisare_meniu(produse, preturi, stoc)
    elif optiune=="2":
        index=int(input("Index produs : "))
        cant=int(input("Cantitate : "))
        adaugare_produs(cant_comanda, stoc, index, cant)
    elif optiune=="3":
        index=int(input("Index produs : "))
        cant=int(input("Cantitate : "))
        scadere_produs(cant_comanda, index, cant)
    elif optiune=="4":
        total=calcul_total(cant_comanda, preturi)
        if total==0:
            print("Comanda este goala")
        else:
            print("1. Student")
            print("2. Happy")
            print("3. Cupon")
            print("4. Fara reducere")
            print("5. Inapoi")
            opt=input("Alege reducerea : ")
            if opt=="1":
                tip_reducere="student"
                reducere_curenta=stabilire_reducere(total, tip_reducere)
            elif opt=="2":
                tip_reducere="happy"
                reducere_curenta=stabilire_reducere(total, tip_reducere)
            elif opt=="3":
                tip_reducere="cupon"
                reducere_curenta=stabilire_reducere(total, tip_reducere)
            elif opt=="4":
                reducere_curenta=0
                tip_reducere=None
            elif opt=="5":
                print("Revenire la meniul principal")
    elif optiune=="5":
        total=calcul_total(cant_comanda, preturi)
        if total==0:
            print("Comanda este goala")
        else:
            if tip_reducere==None:
                reducere_finala=0
            else:
                reducere_finala=stabilire_reducere(total, tip_reducere)
            afiseaza_bon(produse, preturi, cant_comanda, reducere_finala)
            finalizare_comanda(stoc, cant_comanda)
            reducere_curenta=0
            tip_reducere=None
    elif optiune=="6":
        anulare_comanda(cant_comanda)
        reducere_curenta=0
        tip_reducere=None
        print("Comanda anulata")
    elif optiune=="0":
        print("Program inchis")
        break
    else:
        print("Optiune invalida")