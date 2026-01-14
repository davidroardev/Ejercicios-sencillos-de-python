#funcion con la cual se busca eliminar los duplicados de un array entregado

def eliminar_duplicados(arr):
    if arr is None or len(arr) == 0:
        return "El array esta vacio"
    if len(arr) == 1 :
        return 'solo hay un elemento en el array', arr
    
    result_arr = []

    for num in arr:
        if num not in result_arr:
            result_arr.append(num)
        else:
            continue
    
    return result_arr

mi_lista = [2,6,2,4,6,4,7,8,9,9,10]

resultado = eliminar_duplicados(mi_lista)

print(resultado)