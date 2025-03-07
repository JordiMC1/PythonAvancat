def pregunta():
    divisor = int(input("Diguem el divisor: "))
    dividendo = int(input("Diguem el dividendo: "))
    print(divisor/dividendo)

try: 
    pregunta()
except ZeroDivisionError:
    print("No es pot dividir entre 0!! Intenta-ho de nou.")

pregunta()