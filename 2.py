elevi=["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note=[9, 7, 10, 4, 8]

elev_nou="Felix"
nota_elev_nou=6
elev_de_sters="Darius"

interogari_nume=["Ana", "Mara", "Elena", "stop"]

absente=[1, 0, 2, 3, 0]

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()

nota_maxima=max(note)
nota_minima=min(note)
for i in range(len(note)):
    if note[i]==nota_maxima:
        print(f"Nota maxima este {nota_maxima} al elevului {elevi[i]}")
    elif note[i]==nota_minima:
        print(f"Nota minima este {nota_minima} al elevului {elevi[i]}")
print()

media=sum(note)/len(note)
print(f"Media clasei este {media:.2f}")
print()

for i in range(len(note)):
    if note[i]>=5:
        print(elevi[i])
print()

for i in range(len(note)):
    note[i]+=1
print(note)
print()

elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)
print()

pozitie=elevi.index(elev_de_sters)
elevi.pop(pozitie)
print(elevi)
note.pop(pozitie)
print(note)
print()

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()

i=0
while interogari_nume[i]!="stop":
    if interogari_nume[i] in elevi:
        j=elevi.index(interogari_nume[i])
        print(note[j])
    else:
        print("nu exista")
    i+=1
print()

a=0
b=0
for i in range(len(note)):
    if note[i]>=5:
        a+=1
    else:
        b+=1
print(f"Sunt {a} elevi promovati")
print(f"Sunt {b} elevi respinsi")
print()

lista=[]
for i in range(len(note)):
    if note[i]>=5:
        lista.append(note[i])
if len(lista)>0:
    media_lista=sum(lista)/len(lista)
    print(f"Media clasei este {media_lista}")
else:
    print("Nu exista")