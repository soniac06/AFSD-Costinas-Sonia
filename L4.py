import json

def citeste_json(fisier):
    try:
        with open(fisier, "r") as jsonfile:
            lista=json.load(jsonfile)
        return lista
    except FileNotFoundError:
        print("Fisierul nu exista")
        return []

def afisare(lista):
    if len(lista)==0:
        print("Lista este goala")
        return
    print("\n--- LISTA COMPETITORI ---\n")
    for competitor in lista:
        print(f"{competitor['nume']:<20} {competitor['punctaj']:<10} {competitor['timp']:<10}")
    print()

def adaugare(lista):
    nume=input("Nume : ").strip()
    if nume=="":
        print("Nume invalid")
        return
    punctaj=int(input("Punctaj : "))
    timp=int(input("Timp : "))
    competitor={
        "nume": nume,
        "punctaj": punctaj,
        "timp": timp
    }
    lista.append(competitor)
    print("Competitor adaugat")

def actualizare(lista):
    if len(lista)==0:
        print("Lista este goala")
        return
    nume=input("Nume : ").strip()
    gasit=False
    for competitor in lista:
        if competitor["nume"].lower()==nume.lower():
            gasit=True
            competitor["punctaj"]=int(input("Punctaj nou : "))
            competitor["timp"]=int(input("Timp nou : "))
            print("Competitorul a fost actualizat")
            break
    if gasit==False:
        print("Competitor inexistent")

def comparare(x,y):
    if x["punctaj"]>y["punctaj"]:
        return True
    if x["punctaj"]<y["punctaj"]:
        return False
    if x["timp"]<y["timp"]:
        return True
    if x["timp"]>y["timp"]:
        return False
    if x["nume"].lower()<y["nume"].lower():
        return True
    if x["nume"].lower()>y["nume"].lower():
        return False
    return False
def sortare(lista, stanga=0, dreapta=None):
    if dreapta is None:
        dreapta=len(lista)-1
    if stanga<dreapta:
        pivot=lista[dreapta]
        i=stanga-1
        for j in range(stanga,dreapta):
            if comparare(lista[j],pivot):
                i+=1
                lista[i],lista[j]=lista[j],lista[i]
        lista[i+1],lista[dreapta]=lista[dreapta],lista[i+1]
        poz_pivot=i+1
        sortare(lista, stanga, poz_pivot-1)
        sortare(lista, poz_pivot+1, dreapta)

def clasament(lista):
    if len(lista)==0:
        print("Lista este goala")
        return
    sortare(lista,0,len(lista)-1)
    print("\n--- CLASAMENT ---")
    print(f"{'Loc':<5} {'Nume':<20} {'Punctaj':<10} {'Timp':<10}")
    loc=1
    for i in range(len(lista)):
        if i>0:
            if lista[i]["punctaj"]!=lista[i-1]["punctaj"] or lista[i]["timp"]!=lista[i-1]["timp"]:
                loc=i+1
        competitor=lista[i]
        print(f"{loc:<5} {competitor['nume']:<20} {competitor['punctaj']:<10} {competitor['timp']:<10}")
    print()

def statistici(lista):
    if len(lista)==0:
        print("Lista este goala")
        return
    total=len(lista)
    punctaj=[]
    timp=[]
    for competitor in lista:
        punctaj.append(competitor["punctaj"])
        timp.append(competitor["timp"])
    print("\n--- STATISTICI ---")
    print("Numar competitori : ", total)
    print("Punctajul maxim : ", max(punctaj))
    print("Punctajul minim : ", min(punctaj))
    print("Media punctajelor: ", round(sum(punctaj)/total, 2))
    print("Cel mai bun timp : ", min(timp))
    print()

if __name__=="__main__":
    lista=citeste_json("competitori.json")
    while True:
        print("1 - Afisare")
        print("2 - Adaugare")
        print("3 - Actualizare")
        print("4 - Sortare")
        print("5 - Clasament")
        print("6 - Statistici")
        print("0 - Iesire")
        optiune=input("Optiunea aleasa este : ")
        if optiune=="1":
            afisare(lista)
        elif optiune=="2":
            adaugare(lista)
        elif optiune=="3":
            actualizare(lista)
        elif optiune=="4":
            sortare(lista)
            print("Lista a fost sortata")
        elif optiune=="5":
            clasament(lista)
        elif optiune=="6":
            statistici(lista)
        elif optiune=="0":
            print("Program inchis")
            break
        else:
            print("Optiune invalida")