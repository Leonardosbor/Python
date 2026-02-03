def media_segura(lista_numeros):

    soma = 0

    if len(lista_numeros) == 0:
        return 'Lista vazia'
    
    for item in lista_numeros:
        soma += item

    media = soma / len(lista_numeros)
    return media

print(media_segura([]))    