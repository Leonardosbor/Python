def media_nota(nota1, nota2):
    
    media = (nota1 + nota2) / 2

    if media >= 7:
        return('APROVADO')
    elif media >= 5:
        return('RECUPERAÇÃO')
    else:
        return('REPROVADO')
    
resultado = media_nota(7, 5)
print(resultado)