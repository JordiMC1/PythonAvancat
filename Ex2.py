from functools import reduce

def PassarLlistaNumeros():
    l = [1,2,3,4,5]
    numero = reduce(lambda x, y: str(x)+str(y), l)
    print(numero)

PassarLlistaNumeros()