import string  # Módulo con constantes como el alfabeto

def alphabet_position(text):
    posiciones = []  # Aquí guardaremos los números como texto

    for caracter in text.lower():  # Recorre el texto en minúsculas, letra a letra
        if caracter in string.ascii_lowercase:  # ¿Es una letra de la a a la z?
            posiciones.append(str(string.ascii_lowercase.index(caracter) + 1))# Posición en el alfabeto (+1 porque Python cuenta desde 0), a texto, y a la lista

    return " ".join(posiciones)  # Une los números con un espacio entre cada uno