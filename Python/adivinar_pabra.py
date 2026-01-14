#funcion para jugar de manera simplificada adivina la palabra
import random

def adivina_palabra():

    palabras = ['Hola', 'Perro', 'Gato', 'Banana']

    palabra_seleccionada = random.choice(palabras).lower()

    progreso = ['_']* len(palabra_seleccionada)

    intentos = 0

    while '_' in progreso:
        print("\nPalabra Actual:" + "".join(progreso))
        letra_usuario = input("ingrese una letra").lower()

        if len(letra_usuario) != 1:
            print("Porfavor ingrese una letra")
            continue

        exito = False

        for i in range(len(palabra_seleccionada)):
            if palabra_seleccionada[i] == palabra_seleccionada:
                progreso[i] = letra_usuario
                exito = True

        if exito:
            print('')
        


    

            


        
