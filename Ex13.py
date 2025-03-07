from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def parlar(self):
        pass
    
    @abstractmethod
    def moure(self):
        pass

    def quisoc(self):
        return f"Sóc un {self.especie} i tenc {self.edat} anys"
    
class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)
    
    def xerrar(self):
        return "HIIHHHIHI"
    
    def mourem(self):
        return "Galop"

    def quisoc(self):
        return f"Sóc un cavall de {self.edat} anys."


class Dofi(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)
    
    def xerrar(self):
        return "FIIIIII"
    
    def mourem(self):
        return "Nadar"

class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)
    
    def xerrar(self):
        return "BZZZZ BZZZZ"
    
    def mourem(self):
        return "Volar"
    
    def picar(self):
        return "Et picaré!"

class Huma(Animal):
    def __init__(self, edat, nom):
        super().__init__("Huma", edat)
        self.nom = nom
    
    def xerrar(self):
        return "Hola món!"
    
    def mourem(self):
        return "Caminar"
    
    def quisoc(self):
        return f"Sóc {self.nom}, un humà de {self.edat} anys."

class Fiet(Huma):
    def __init__(self, edat, nom, mare, pare):
        super().__init__(edat, nom)
        self.mare = mare
        self.pare = pare
    
    def nompares(self):
        return f"Els meus pares són: {self.pare} i {self.mare}."

class Centaure(Cavall, Huma):
    def __init__(self, edat, nom):
        Huma.__init__(self, edat, nom)
        Cavall.__init__(self, edat)  
    
    def xerrar(self):
        return "Sóc un centaure i puc parlar i relinchar!"
    
    def mourem(self):
        return "Corro com un cavall i camino com un humà"
    
    def quisoc(self):
        return f"Sóc {self.nom}, un centaure de {self.edat} anys."

class Xou(Animal):
    def __init__(self):
        super().__init__("Espectacle", 0)
    
    def xerrar(self):
        return "Benvinguts al xou!"
    
    def mourem(self):
        return "Ballo molt bé!"
    
    def quisoc(self):
        return "És un espectacle únic!"

# Llista d'elements
elements = [Cavall(5), Dofi(8), Abella(1), Huma(30, "Pere"), Fiet(10, "Joanet", "Maria", "Toni"), Centaure(25, "Quiron"), Xou()]

# Iteració sobre elements
for e in elements:
    print(e.quisoc())
    print(e.xerrar())
    print(e.mourem())
    if isinstance(e, Abella):
        print(e.picar())
    if isinstance(e, Fiet):
        print(e.nompares())