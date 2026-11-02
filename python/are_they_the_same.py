def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False
    
    i = 0
    
    cuadrados = [x ** 2 for x in array1] 
    
    array2_ordenada = sorted(array2)
    
    for num in sorted(cuadrados):
        
        if num == array2_ordenada[i]:
            i += 1
        else:
            return False
    
    return True
