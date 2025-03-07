def indexenpal():
    llista = ["Marc","David","Maria","Joan"]
    diccionari = {}
    for i,e in enumerate(llista):
        diccionari[e] = i
    return diccionari

print(indexenpal())