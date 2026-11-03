def first_n_smallest(lista, n):

    if n == 0:
        return []

    lista_ordenada = sorted(lista)[:n]
    smallest = []

    for number in lista:
        if number in lista_ordenada:
            smallest.append(number)
            lista_ordenada.remove(number)

    return smallest


if __name__ == "__main__":
    assert first_n_smallest([1,2,3,4,5],3) == [1,2,3]
    assert first_n_smallest([5,4,3,2,1],3) == [3,2,1]
    assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
    assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
    assert first_n_smallest([1,2,3,4,5],0) == []
    assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
    assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
    assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
    assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
    assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]