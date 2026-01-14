#funcion con la cual se busca retornar el segundo numero mas grande dentro de un arreglo

def segundo_mas_grande(array):
    if  array is None or len(array) < 2:
        return "El array esta vacio o solo tiene 1 valor"
    
    mayor = 0
    segundo_mayor = 0
    #determinar el numero mayor
    for item in array:
        if item > mayor:
            segundo_mayor = mayor
            mayor = item

        if item < mayor and item > segundo_mayor:
            segundo_mayor = item
    
    return segundo_mayor
    
resultado = segundo_mas_grande([7,5,3,10,8])

print(resultado)
