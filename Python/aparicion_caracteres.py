#funcion con la cual puedo realizar el conteo de caracteres en un texto

def conteo_caracter(texto):
    
    if texto is None or texto == "":
        return "El texto es vacio use uno valido porfavor"
    
    texto_min = texto.lower().strip().replace(" ","") #strip solo quita los espacios de los extremos no los internos

    contador = 0
    resultado = {}
    
    for caracter in texto_min:
        if caracter not in resultado:
            resultado[caracter] = 1
        else:
            resultado[caracter] +=1
        contador +=1
    
    resultado["total caracteres"] = contador

    return resultado

resultado_funcion = conteo_caracter('Hola que estas haciendo')

print(resultado_funcion)