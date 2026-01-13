#algotitmo sencillo que me permiter determinar cuantas vocales hay en un texto

def contar_vocales(texto):
    contador = 0
    vocales = "aeiouAEIOU"

    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador