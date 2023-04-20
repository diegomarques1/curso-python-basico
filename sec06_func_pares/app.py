def pares(lista):
    lista_pares = []
    for elem in lista:
        if elem % 2 == 0:
            lista_pares.append(elem)
    return lista_pares

lista_pares = pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(lista_pares)