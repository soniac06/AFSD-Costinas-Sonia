def numar_unic(lista: list[int]):
    if not lista:
        return "Lista este goala"
    for x in lista:
        if lista.count(x)==1:
            return f"Numarul unic este: {x}"
    return "Nu exista numar unic in lista"