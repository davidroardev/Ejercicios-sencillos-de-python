## Algoritmo que ordena numeros en un array usando la idea de pivote

def quick_sort(arr):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elegimos el elemento central como pivote
    pivote = arr[len(arr) // 2]
    
    # Clasificamos los elementos en tres listas
    izquierda = [x for x in arr if x < pivote] # gracias a list comprehension esta linea es igual a decir esto izquierda = [] for x in arr: if x < pivote izquierda.append(x)
    centro    = [x for x in arr if x == pivote]
    derecha   = [x for x in arr if x > pivote]
    
    # Aplicamos lo mismo a las listas de los lados (recursión)
    return quick_sort(izquierda) + centro + quick_sort(derecha)

# Prueba
mi_lista = [23, 45, 16, 37, 3, 99, 22]

quick_sort(mi_lista)

def quick_sort_desc(arr):
    #caso base
    if len(arr) <= 1:
        return arr
    
    #se crea el pivote
    pivote = arr[len(arr)//2] ## el pivote siempre tiene que ser una posicion del array mas no un valor

    izquierda = [x for x in arr if x > pivote]
    centro = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x < pivote]

    return quick_sort_desc(izquierda) + centro + quick_sort_desc(derecha)

quick_sort_desc(mi_lista)

resultado_asc = quick_sort(mi_lista)
resultado_desc = quick_sort_desc(mi_lista)
print(f"lista ascendente {resultado_asc}, lista descendente: {resultado_desc}")