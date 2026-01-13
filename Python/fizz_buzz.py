#algoritmo que imprime fizz si un numero es multiplo de 3 y buzz si un numero es multilpo de 5

def fizz_buzz(n):
    for i in range(1, n+1):
        salida = ""
        if i%3 == 0:
            salida += "fizz"
        if i%5 == 0:
            salida += "buzz"
        
        print(salida or f"el numero {i} no es multiplo de  3 o 5")

fizz_buzz(100)