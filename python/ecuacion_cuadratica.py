def roots(a,b,c):
    
    discriminante = b**2 - 4*a*c
    
    suma = -b/a
    
    if discriminante < 0:
        return None
    else:
        return round(suma, 2)