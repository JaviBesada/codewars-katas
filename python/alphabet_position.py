import string

def alphabet_position(text):
    posiciones = []
    for caracter in text.lower():
        if caracter in string.ascii_lowercase:
            posiciones.append(str(string.ascii_lowercase.index(caracter) + 1))
    return " ".join(posiciones)