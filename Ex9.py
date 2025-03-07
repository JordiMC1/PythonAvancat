def potencia():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = int(input("Quina potència vols? "))
    b = [num**a for num in l]
    print(b)

potencia()