def llista():
    l = ["mica", "dit", "marca", "peu"]
    p = list(filter(lambda x: x[0] == "p", l))
    print(p)

llista()