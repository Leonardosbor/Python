def filtrar_pares(lista_numeros):
    
    return [item for item in lista_numeros if item % 2 == 0]
    
print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9]))