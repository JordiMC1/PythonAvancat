def llistaindex():
    l = [5,2,4,3,7]
    a = []
    for i,e in enumerate(l):
        if e == i:
            a.append(e)
    return a

print(llistaindex())