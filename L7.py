import json
import os

campuri_obligatorii=["nume", "cost", "profit", "categorie", "risc"]
def incarcare_date(nume_fisier="investitii.json"):
    if not os.path.exists(nume_fisier):
        print("Fisierul nu exista")
        return []
    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            investitii=json.load(f)
    except json.JSONDecodeError:
        print("Fisierul nu este un JSON valid")
        return []
    except Exception as e:
        print("Eroare la citirea fisierului:", e)
        return []
    if not isinstance(investitii, list) or len(investitii)==0:
        print("Fisierul este gol sau nu contine o lista.")
        return []
    investitii_valide=[]
    for inv in investitii:
        if not isinstance(inv, dict):
            print("Element invalid ignorat:", inv)
            continue
        valid=True
        for camp in campuri_obligatorii:
            if camp not in inv:
                print("Lipseste campul", camp, "in", inv)
                valid=False
        if valid:
            if not isinstance(inv["cost"], int) or not isinstance(inv["profit"], int):
                print("Costul si profitul trebuie sa fie numere intregi:", inv)
            elif inv["cost"]<=0 or inv["profit"]<0:
                print("Cost sau profit invalid:", inv)
            else:
                investitii_valide.append(inv)
    return investitii_valide

def afisare_investitii(investitii):
    print("\nInvestiții disponibile:")
    if len(investitii)==0:
        print("Nu exista investitii de afisat")
        return
    for inv in investitii:
        raport=inv["profit"]/inv["cost"]
        print("--------------------------------")
        print("Nume:", inv["nume"])
        print("Cost:", inv["cost"])
        print("Profit:", inv["profit"])
        print("Categorie:", inv["categorie"])
        print("Risc:", inv["risc"])
        print("Raport profit/cost:", round(raport,2))

def analiza_descriptiva(investitii):
    print("\nAnaliza descriptiva:")
    if len(investitii)==0:
        print("Nu exista investitii pentru analiza")
        return
    print("Numar total investitii:", len(investitii))
    cost_min=min(investitii, key=lambda inv: inv["cost"])
    cost_max=max(investitii, key=lambda inv: inv["cost"])
    profit_max=max(investitii, key=lambda inv: inv["profit"])
    print("Investitia cu cost minim:", cost_min["nume"], "-", cost_min["cost"])
    print("Investitia cu cost maxim:", cost_max["nume"], "-", cost_max["cost"])
    print("Investitia cu profit maxim:", profit_max["nume"], "-", profit_max["profit"])
    categorii={}
    riscuri={}
    for inv in investitii:
        categorii[inv["categorie"]]=categorii.get(inv["categorie"], 0)+1
        riscuri[inv["risc"]]=riscuri.get(inv["risc"], 0)+1
    print("\nDistributie pe categorii:")
    for categorie, nr in categorii.items():
        print("-", categorie, ":", nr)
    print("\nDistributie pe niveluri de risc:")
    for risc, nr in riscuri.items():
        print("-", risc, ":", nr)

def filtrare_dupa_categorie(investitii):
    categorie=input("\nIntrodu categoria: ")
    if categorie=="":
        return investitii
    rezultat=[]
    for inv in investitii:
        if inv["categorie"].lower()==categorie.lower():
            rezultat.append(inv)
    return rezultat

def filtrare_dupa_risc(investitii):
    risc=input("Introdu riscul: ")
    if risc=="":
        return investitii
    rezultat=[]
    for inv in investitii:
        if inv["risc"].lower()==risc.lower():
            rezultat.append(inv)
    return rezultat

def ordonare_investitii(investitii):
    print("\nOrdonare:")
    print("1 - dupa cost")
    print("2 - dupa profit")
    print("3 - dupa raport profit/cost")
    print("Enter - fara ordonare")
    optiune=input("Alege optiunea: ")
    rezultat=investitii[:]
    if optiune=="1":
        rezultat.sort(key=lambda inv: inv["cost"])
    elif optiune=="2":
        rezultat.sort(key=lambda inv: inv["profit"], reverse=True)
    elif optiune=="3":
        rezultat.sort(key=lambda inv: inv["profit"]/inv["cost"], reverse=True)
    return rezultat

def aplica_restrictie_suplimentara(investitii):
    print("\nRestrictie suplimentara:")
    print("Se exclud investitiile cu risc ridicat")
    rezultat=[]
    for inv in investitii:
        if inv["risc"].lower()!="ridicat":
            rezultat.append(inv)
    return rezultat

def citire_buget():
    while True:
        try:
            buget=int(input("\nIntrodu bugetul maxim: "))
            if buget<=0:
                print("Bugetul trebuie sa fie pozitiv")
            else:
                return buget
        except:
            print("Introdu o valoare numerica valida")

def optimizare(investitii, buget):
    n=len(investitii)
    dp=[]
    for i in range(n+1):
        linie=[]
        for b in range(buget+1):
            linie.append(0)
        dp.append(linie)
    for i in range(1,n+1):
        cost=investitii[i-1]["cost"]
        profit=investitii[i-1]["profit"]
        for b in range(1,buget+1):
            if cost<=b:
                fara_investitie=dp[i-1][b]
                cu_investitie=dp[i-1][b-cost]+profit
                dp[i][b]=max(fara_investitie, cu_investitie)
            else:
                dp[i][b]=dp[i-1][b]
    b=buget
    investitii_alese=[]
    for i in range(n, 0, -1):
        if dp[i][b]!=dp[i-1][b]:
            investitii_alese.append(investitii[i-1])
            b=b-investitii[i-1]["cost"]
    investitii_alese.reverse()
    return dp[n][buget], investitii_alese, dp

def afisare_tabel_dp(dp, buget):
    print("\nTabel DP partial:")
    limita=buget
    if limita>20:
        limita=20
    for i in range(len(dp)):
        print(dp[i][0:limita+1])

def afisare_rezultat(buget, profit_optim, investitii_alese):
    cost_total=0
    for inv in investitii_alese:
        cost_total+=inv["cost"]
    print("\nRezultat final:")
    print("Buget disponibil:", buget)
    print("Profit optim:", profit_optim)
    print("Cost total utilizat:", cost_total)
    print("Buget ramas:", buget-cost_total)
    print("\nInvestitii selectate:")
    if len(investitii_alese)==0:
        print("Nu a fost selectata nicio investitie")
    else:
        for inv in investitii_alese:
            print("-", inv["nume"],
                  "| Cost:", inv["cost"],
                  "| Profit:", inv["profit"],
                  "| Categorie:", inv["categorie"],
                  "| Risc:", inv["risc"])

if __name__ == "__main__":
    investitii=incarcare_date()
    if len(investitii)==0:
        print("Nu exista investitii valide")
    else:
        afisare_investitii(investitii)
        analiza_descriptiva(investitii)
        investitii_prelucrate = filtrare_dupa_categorie(investitii)
        investitii_prelucrate = filtrare_dupa_risc(investitii_prelucrate)
        investitii_prelucrate = ordonare_investitii(investitii_prelucrate)
        investitii_prelucrate = aplica_restrictie_suplimentara(investitii_prelucrate)
        print("\nInvestitii dupa filtrare si restrictii:")
        afisare_investitii(investitii_prelucrate)
        if len(investitii_prelucrate)==0:
            print("Nu exista investitii disponibile dupa filtrare")
        else:
            while True:
                buget=citire_buget()
                profit_optim, investitii_alese, dp=optimizare(investitii_prelucrate, buget)
                afisare_rezultat(buget, profit_optim, investitii_alese)
                afisare_tabel_dp(dp, buget)
                raspuns=input("\nDoresti analiza pentru alt buget? da/nu: ")
                if raspuns.lower()!="da":
                    break