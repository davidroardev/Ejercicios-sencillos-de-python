#se me pide crear una funcion que retorne true si dos palabras son anagramas y false si no lo son
#para determinar si son anagrmas las palabras deben tener la misma longitud y las mismas letras

def es_anagrama(palabra1,palabra2):
    palabra1= palabra1.strip().lower()
    palabra2 = palabra2.strip().lower()

    if len(palabra1) != len(palabra2):
        return False
    vistos1 = {}
    vistos2 = {}

    for letra in palabra1:
        if letra not in vistos1:
            vistos1[letra] = 1
        else:
            vistos1[letra] +=1

    for letra in palabra2:
        if letra not in vistos2:
            vistos2[letra] = 1
        else:
            vistos2[letra] +=1

    if vistos1 == vistos2:
        return True
    
    return False
    
resultado = es_anagrama('roma','amor')
print(resultado)


def es_anagrama_ordenado(palabra1,palabra2):
    palabra1= palabra1.strip().lower()
    palabra2 = palabra2.strip().lower()

    if len(palabra1) != len(palabra2):
        return False

    palabra1 = sorted(list(palabra1))
    palabra2 = sorted(list(palabra2))

    if palabra1 == palabra2:
        return True
    else:
        return False
    
resultado = es_anagrama('roma','amor')
print(resultado)