def to_camel_case(text):
    
    camel_case = ""
    
    # Recorre cada palabra numerada (i), unificando guiones bajos y normales con .replace y separando cada palabra con .split
    for i, palabra in enumerate(text.replace("_", "-").split("-")): #enumerate recorre el texto, y cada palabra que separamos nos da el indice "i" y la palabra.
        if i == 0: #Esto nos dice que es el primer paso de bucle, osea la primera palabra
            camel_case += palabra             # La primera palabra se respeta tal cual
        else:
            camel_case += palabra.capitalize() # El resto se capitalizan, se ponen en mayus con .capitalize
            
    return camel_case