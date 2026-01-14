#funcion para jugar de manera simplificada adivina la palabra
import random

def adivina_palabra():

    palabras = ['Hola', 'Perro', 'Gato', 'Banana']

    palabra_seleccionada = random.choice(palabras).lower()

    progreso = ['_']* len(palabra_seleccionada) # Arreglo que siempre tendra la misma longitud que la palabra seleccionada por el sistema

    intentos = 1

    while '_' in progreso:
        print("\nPalabra Actual: " + "".join(progreso))
        letra_usuario = input("ingrese una letra o palabra: ").lower()

        if len(letra_usuario) != 1:
            if letra_usuario == palabra_seleccionada:
                print(f'Seleccionaste la palabra correcta: {letra_usuario}')
                break
            else:
                print("la palabra no es correcta intenta de nuevo")
                continue
        
        exito = False

        for i in range(len(palabra_seleccionada)):
            if palabra_seleccionada[i] == letra_usuario:
                progreso[i] = letra_usuario
                exito = True

        if exito:
            print(f'Seleccionaste una letra correcta{letra_usuario}')
        else:
            print('la letra no se encuentra en la palabra')
            intentos +=1
    
    print(f'¡Felicidades encontraste la palabra palabra: {palabra_seleccionada} en {intentos} intentos!')


adivina_palabra()


        
