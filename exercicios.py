def filtrar_pares(lista_numeros):
    
    nova_lista = []

    for item in lista_numeros:
        if item % 2 == 0:
            nova_lista.append(item)
    return nova_lista
    
print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9]))