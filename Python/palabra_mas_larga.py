#algoritmo que me permite determinar cual es la palabra mas larga de una oracion

def palabra_mas_larga(oracion):
    palabras = oracion.split(" ")
    palabra_mas_larga =""
    print(palabras)
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return f'la palabra mas larga es: {palabra_mas_larga} con {len(palabra_mas_larga)} letras'


resultado = palabra_mas_larga('hola como estas')
print(resultado)