import random

def imprimir_tauler(tauler):
    for fila in tauler:
        print(" | ".join(fila))
        print("-" * 9)

def comprovar_guanyador(tauler, jugador):
    for fila in tauler:
        if all(casella == jugador for casella in fila):
            return True
    for col in range(3):
        if all(tauler[fila][col] == jugador for fila in range(3)):
            return True
    if all(tauler[i][i] == jugador for i in range(3)) or all(tauler[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def moviments_disponibles(tauler):
    return [(f, c) for f in range(3) for c in range(3) if tauler[f][c] == " "]

def minimax(tauler, maximitzant):
    if comprovar_guanyador(tauler, "O"):
        return 1
    if comprovar_guanyador(tauler, "X"):
        return -1
    if not moviments_disponibles(tauler):
        return 0
    
    if maximitzant:
        millor_puntuacio = -float("inf")
        for moviment in moviments_disponibles(tauler):
            tauler[moviment[0]][moviment[1]] = "O"
            puntuacio = minimax(tauler, False)
            tauler[moviment[0]][moviment[1]] = " "
            millor_puntuacio = max(puntuacio, millor_puntuacio)
        return millor_puntuacio
    else:
        millor_puntuacio = float("inf")
        for moviment in moviments_disponibles(tauler):
            tauler[moviment[0]][moviment[1]] = "X"
            puntuacio = minimax(tauler, True)
            tauler[moviment[0]][moviment[1]] = " "
            millor_puntuacio = min(puntuacio, millor_puntuacio)
        return millor_puntuacio

def millor_moviment(tauler):
    millor_puntuacio = -float("inf")
    moviment = None
    for m in moviments_disponibles(tauler):
        tauler[m[0]][m[1]] = "O"
        puntuacio = minimax(tauler, False)
        tauler[m[0]][m[1]] = " "
        if puntuacio > millor_puntuacio:
            millor_puntuacio = puntuacio
            moviment = m
    return moviment

def jugar():
    tauler = [[" " for _ in range(3)] for _ in range(3)]
    mode = input("Tria mode de joc (1: vs jugador, 2: vs màquina): ")
    torn = "X"
    
    while True:
        imprimir_tauler(tauler)
        if comprovar_guanyador(tauler, "X"):
            print("El jugador X ha guanyat!")
            break
        if comprovar_guanyador(tauler, "O"):
            print("El jugador O ha guanyat!")
            break
        if not moviments_disponibles(tauler):
            print("Empat!")
            break
        
        if mode == "2" and torn == "O":
            moviment = millor_moviment(tauler)
            print(f"La màquina ha triat: {moviment}")
        else:
            fila, col = map(int, input(f"Jugador {torn}, introdueix fila i columna (0-2 0-2): ").split())
            moviment = (fila, col)
        
        if moviment in moviments_disponibles(tauler):
            tauler[moviment[0]][moviment[1]] = torn
            torn = "O" if torn == "X" else "X"
        else:
            print("Moviment invàlid, torna a intentar-ho!")

jugar()