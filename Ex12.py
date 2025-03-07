import os

def crearfitxer():
    os.mkdir("/home/JordiMelia/AO/Prova")
    os.chdir("/home/JordiMelia/AO/Prova")
    with open("Ex12.txt","w+") as f:
        f.write("David, Toni, Maria... ")
        print(f.read())
    with open("Ex12.txt","r+") as f:
        f.write("David Labiano, Joan, Carlos... ")
        print(f.read())

crearfitxer()