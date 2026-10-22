def duplicate_encode(word):
    
    nueva_cadena = [] #Creamos una lista
    
    for caracter in word.lower():  #Buscamos el caracter en el texto en minusculas con .lower
        if word.lower().count(caracter) == 1: #Si word.lower que es el texto en minusculas cuenta los caracteres y solo hay uno.
            nueva_cadena.append("(")
        else:
            nueva_cadena.append(")") #Si no hacemos esto.
    
    return "".join(nueva_cadena)