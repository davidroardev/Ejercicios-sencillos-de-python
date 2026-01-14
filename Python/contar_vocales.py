#algotitmo sencillo que me permiter determinar cuantas vocales hay en un texto

def contar_vocales(texto):
    contador = 0
    vocales = "aeiouAEIOU"
    resultado = {}
    

    for letra in texto:
        if letra in vocales:
            contador += 1
            if letra not in resultado:
                resultado[letra] = 1
            else:
                resultado[letra] +=1

    return resultado

print_consola = contar_vocales('Hola Como estas')

print(print_consola)