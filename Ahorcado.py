import random
import os

palabras = ["TALPA","MAZAMITLA","TEQUILA","MASCOTA","TAPALPA","TLAQUEPAQUE","CHAPALA"]

palabra = list(random.choice(palabras))

horca =     ["              !========N",
             "                       N",
             "                       N",
             "                       N",
             "            ___________N"]

ahorcado =  ["              !========N",
             "              O        N",
             "             /|\       N",
             "             / \       N",
             "            ___________N"]

letras_todas = []
fallos = 1

resultado = []

for i in range(len(palabra)):
    resultado.append("_")

while True:
    os.system("cls")

    print("---El Ahorcado---")

    for i in range(fallos):
        print(ahorcado[i])
    for i in range(len(horca)-fallos):
        print(horca[i+fallos])

    print()

    print("  ",end=" ")
    for i in resultado:
        print(i,end=" ")
    print()
    print()

    if resultado == palabra:
        print("Felicidades has Ganado...")
        break
    if fallos > 3:
        print("La palabra era:","".join(palabra))
        print("Mejor suerte para la proxima...")
        break

    while True:
        letra_usuario_sin_formato = input("Dime una letra: ")
        letra_usuario = letra_usuario_sin_formato.upper()
        if len(letra_usuario)!= 1:
            print("Introduce una letra")
        elif letra_usuario in letras_todas:
            print("Esa letra ya ha sido introducida...")
        elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUWXYZ":
            print("Valor no valido, Introduce una letra")
        else:
            letras_todas.append(letra_usuario)
            break
    for i in range(len(palabra)):
        if palabra[i] == letra_usuario:
            resultado[i] = letra_usuario
    if letra_usuario not in palabra:
        fallos += 1

    print()
    print()
