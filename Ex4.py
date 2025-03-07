def encadenar():
    l1 = ["David","Marc"]
    l2 = ["Jordi","Bruno"]
    cadena = list(map(lambda x,y: x+"-"+y, l1,l2))
    print(cadena)

encadenar()