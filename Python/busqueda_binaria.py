# funcion con la cual recibien un array ordenado puedo entrontrar un valor con un N numero de iteraciones

def busqueda_binaria(array, objetivo):
    inicio = 0
    fin  = len(array) - 1
    
    while inicio <= fin:
        mitad = (inicio + fin )//2
        
        if array[mitad] == objetivo:
            print("El objetivo", objetivo ,"esta en la pocision:", mitad)
            return mitad
        elif array[mitad] < objetivo:
            inicio = mitad +1
        else:
            fin = mitad -1

    return 'El numero no se encuentra en el array'

array = [3,6,7,13,14,17,18,19,21,24,26,27,28,29,35,37,39,43,45,48,52,57,59]

busqueda_binaria(array, 21)