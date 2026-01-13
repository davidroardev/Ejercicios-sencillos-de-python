#algoritmo que me permite determinar si una palabra es palindromo

def es_palindromo(palabra):
    palabra_limpia = palabra.replace(" ","").lower()
    invertida = ""
    for letra in palabra_limpia:
        invertida = letra + invertida
    
    if palabra_limpia == invertida:
        return f'la palabra {palabra} es palindromo'
    
    return f'la palabra no es palindromo'

resultado = es_palindromo("anita lava la tina")

print(resultado)


def es_palindromo2(p):
    p = p.replace(" ", "").lower()
    return p == p[::-1] # Devuelve True o False

resultado2 = "la palabra es palindromo" if es_palindromo2("ojo rojo") else "no es palindormo"

print(resultado2)