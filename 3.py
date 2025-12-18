def afiseaza(tabla):
    for i in range(3):
        for j in range(3):
            print(tabla[i][j], end=' ')
        print()

def citeste_mutare(tabla, jucator):
    while True:
        linie=int(input("Introduceti linia"))
        coloana=int(input("Introduceti coloana"))
        if linie<0 or coloana<0 or linie>2 or coloana>2:
            print("Coordonate invalide")
            continue
        if tabla[linie][coloana]!='.':
            print("Pozitie ocupata")
            continue
        return linie, coloana

def stare_joc(tabla):
    for i in range(3):
        if tabla[i][0]==tabla[i][1]==tabla[i][2] and tabla[i][0]!='.':
            return tabla[i][0]
    for j in range(3):
        if tabla[0][j]==tabla[1][j]==tabla[2][j] and tabla[0][j]!='.':
            return tabla[0][j]
    if tabla[0][0]==tabla[1][1]==tabla[2][2] and tabla[0][0]!='.':
        return tabla[0][0]
    if tabla[0][2]==tabla[1][1]==tabla[2][0] and tabla[0][2]!='.':
        return tabla[0][2]
    for i in range(3):
        for j in range(3):
            if tabla[i][j]=='.':
                return "CONTINUA"
    return "EGAL"

tabla=[
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
      ]
jucator='X'
while True:
    afiseaza(tabla)
    linie,coloana=citeste_mutare(tabla, jucator)
    tabla[linie][coloana]=jucator
    rezultat=stare_joc(tabla)
    if rezultat!="CONTINUA":
        afiseaza(tabla)
        if rezultat=="EGAL":
            print("Jocul s-a terminat la egalitate!")
            break
        else:
            print(f"A castigat jucatorul {rezultat}!")
            break
    if jucator=="X":
        jucator='O'
    else:
        jucator='X'