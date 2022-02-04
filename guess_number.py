"""
Creado por: Gonzalo Perez 
Programa: Juego de adivinar el numero de la maquina 
"""

import random

while True:
    print("Adivina el numero de la maquina")
    print("==================")
    print("Solo tienes 5 intentos")
    print("==================")
    number_m = random.randint(1,100)

    #Creamos un ciclo for que le pregunte un numero entre 1 al 100
    for vidas in range(5):
        # print(number_m)
        number_user = int(input("Ingresa un numero entre el 1 al 100:"))
        

        if number_user == number_m: 
            print(f"Felicidades, el numero {number_user} era el correcto")
            print(f"Total de vidas: {vidas+1}")
            break

        else: 
            if number_user > number_m: 
                print("El numero que ingresaste es mayor al de la maquina")
        
            elif number_user < number_m: 
                print("El numero que ingreso es menor al de la maquina")

    #Mensaje si el usuario no adivina el numero
    if number_m != number_user: 
        print("Ups, vuelve intentarlo para la otra")

    #Preguntamos al jugador si quiere volver a jugar el juego
    replay = input("Desea volver a jugar(s/n):")
    if replay.lower() == "n":
        print("Hasta luego")
        break


