def duplicate_encode(word):
    
    nueva_cadena = {} #Creamos una lista
    
    for caracter in word.lower():  #Buscamos el caracter en el texto en minusculas con .lower
        if word.lower().count(caracter) == 1: #Si word.lower que es el texto en minusculas cuenta los caracteres y solo hay uno.
            nueva_cadena[caracter] = "("
        else:
            nueva_cadena[caracter] = ")" #Si no hacemos esto.

    cadena = ""

    for caracter in word.lower():
        cadena += nueva_cadena.get(caracter)

    return cadena

if __name__ == "__main__":
    assert(duplicate_encode("din") == "(((")
    assert(duplicate_encode("recede") == "()()()")
    assert(duplicate_encode("Success") == ")())())")
    assert(duplicate_encode("(( @") == "))((")
    print(duplicate_encode("Success") == ")())())")