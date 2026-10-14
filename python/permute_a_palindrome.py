def permute_a_palindrome(palabra):
    impares = 0
    
    for letra in set(palabra): #set(palabra) transforma la cadena en un conjunto sin letras repetidas. 
        
        veces = palabra.count(letra) #count cuenta las letras que hay en la palabra.
        
        if veces % 2 == 1:
            impares += 1
            
    return impares <= 1