def loose_change(cents):
    monedas = {
        "Quarters": 0,
        "Dimes": 0,
        "Nickels": 0,
        "Pennies": 0
    }

    valores = { 
        "Quarters": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennies": 1
    }
    
    if cents == 0 or cents < 0:
        return monedas

    resto = int(cents)          # Aqui hacemos una variable resto que inicie con cents, y lo convertimos a int.  

    valores = valores.items()   # Usamos .items para poder iterar sobre cada valor, sino con el diccionario no deja, porque solo nos deja recorrer las claves, y asi nos da tuplas (nombre, valor) que si podemos reccorrer.
    
    for nombre, valor in valores:
        monedas[nombre] = resto // valor    # Añadimos la division entera entre resto(que son los cents que nos quedan) y valor(que es el valor de cada 1)
        resto = resto - (valor * monedas[nombre])   # Modificamos la variable resto, resto es lo que tenemos de esa moneda y valor es el valor de cada moneda por el numero de monedas que hemos cogido, para que nos quede lo que sobra.
        
        
    return monedas



if __name__ == "__main__":

    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    print(loose_change(3.9))