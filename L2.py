import csv
glosar={
  "variabila": {
    "definitie": "nume asociat unei valori",
    "categorie": "fundamente",
    "exemplu": "x = 10"
  },
  "dictionar": {
    "definitie": "structura de date bazata pe perechi cheie-valoare",
    "categorie": "structuri de date",
    "exemplu": "{'a': 1, 'b': 2}"
  }
}

def afisare_meniu():
    print("--- Meniu glosar ---")
    print("Optiuni :")
    print("1. Adauga termen")
    print("2. Cautare exacta termen")
    print("3. Cautare partiala termeni")
    print("4. Actualizare termen")
    print("5. Stergere termen")
    print("6. Afisare glosar")
    print("7. Statistici")
    print("8. Salvare")
    print("9. Incarcare")
    print("0. Iesire")

def afisare_glosar():
    for termen, info in glosar.items():
        print("Termen : ", termen)
        print("Definitie : ", info["definitie"])
        print("Categorie : ", info["categorie"])
        print("Exemplu : ", info["exemplu"])

def adauga_termen():
    termen=input("Introduceti termenul : ")
    definitie=input("Introduceti definitia : ")
    categorie=input("Introduceti categoria : ")
    exemplu=input("Introduceti un exemplu : ")
    if termen in glosar:
        print("Termenul exista deja in glosar.")
        return
    glosar[termen]={
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }
    print("Termenul a fost adaugat.")

def cautare_exacta():
    termen=input("Introduceti termenul : ")
    if termen in glosar:
        info=glosar[termen]
        print("Definitie : ", info["definitie"])
        print("Categorie : ", info["categorie"])
        print("Exemplu : ", info["exemplu"])
    else:
        print("Termenul nu exista in glosar.")

def cautare_partiala():
    fragment=input("Introduceti fragmentul : ")
    gasit=False
    for termen in glosar:
        if fragment.lower() in termen.lower():
            gasit=True
            print(termen, " - ", glosar[termen])
    if gasit==False:
        print("Nu se gasesc termeni de tipul cerut.")

def actualizare():
    termen=input("Introduceti termenul : ")
    print("Campuri disponibile: definitie, categorie, exemplu")
    camp=input("Introduceti campul : ")
    if termen not in glosar:
        print("Termenul nu exista in glosar.")
        return
    if camp not in glosar[termen]:
        print("Camp invalid.")
        return
    valoare=input("Introduceti valoarea : ")
    glosar[termen][camp]=valoare
    print("Actualizare realizata.")

def stergere():
    termen=input("Introduceti termenul : ")
    if termen in glosar:
        del glosar[termen]
        print("Termenul a fost sters din glosar.")
    else:
        print("Termenul nu exista in glosar.")

def statistici():
    total_termeni=len(glosar)
    categorii={}
    for termen in glosar:
        categ=glosar[termen]["categorie"]
        if categ not in categorii:
            categorii[categ]=0
        categorii[categ]+=1
    print("Numarul total de termeni este : ", total_termeni)
    print("Termenii pe categorii sunt : ")
    for categ, num in categorii.items():
        print(categ, " : ", num)

def salvare():
    with open("glosar.csv", "w", newline="", encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["termen", "definitie", "categorie", "exemplu"])
        for termen, info in glosar.items():
            writer.writerow([termen, info["definitie"], info["categorie"], info["exemplu"]])
        print("Glosarul a fost salvat.")

def incarcare():
    try:
        with open("glosar.csv", "r", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            glosar.clear()
            for row in reader:
                glosar[row["termen"]]={
                    "definitie": row["definitie"],
                    "categorie": row["categorie"],
                    "exemplu": row["exemplu"]
                }
        print("Glosarul a fost incarcat.")
    except FileNotFoundError:
        print("Fisierul nu exista.")

if __name__=='__main__':
    while(True):
        afisare_meniu()
        optiune=input("Alege o optiune : ")
        if optiune=='1':
            adauga_termen()
        elif optiune=='2':
            cautare_exacta()
        elif optiune=='3':
            cautare_partiala()
        elif optiune=='4':
            actualizare()
        elif optiune=='5':
            stergere()
        elif optiune=='6':
            afisare_glosar()
        elif optiune=='7':
            statistici()
        elif optiune=='8':
            salvare()
        elif optiune=='9':
            incarcare()
        elif optiune=='0':
            print("Program terminat.")
            break
        else:
            print("Optiune invalida.")