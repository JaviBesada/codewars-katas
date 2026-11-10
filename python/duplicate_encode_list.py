def duplicate_encode(word):
    
    nueva_cadena = []
    
    for caracter in word.lower():
        if word.lower().count(caracter) == 1:
            nueva_cadena.append("(")
        else:
            nueva_cadena.append(")")
    
    return "".join(nueva_cadena)