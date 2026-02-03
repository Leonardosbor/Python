def media_lista(lista_numeros):
    
    soma = 0

    for item in lista_numeros:
        soma += item
    
    media = soma / len(lista_numeros)
    return media

print(media_lista([5, 10, 15]))