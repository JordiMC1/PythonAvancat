def llegirfitxer():
    nom = input("Diguem el nom del arxiu: ")
    with open(nom,"r") as fitxer:
        b = fitxer.read()
        print(b)
    
try:
    llegirfitxer()
except FileNotFoundError:
    print("El fitxer no existeix.")
    llegirfitxer()