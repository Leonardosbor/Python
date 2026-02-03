def calcular_media_notas(n1, n2,  n3):
    
    soma_notas = n1 + n2 + n3
    media_notas = soma_notas / 3

    if media_notas >= 7:
        return 'APROVADO'
    
    if 5 <= media_notas <= 6.9:
        return 'RECUPERAÇÃO'
    return 'REPROVADO'
    

print(calcular_media_notas(1, 1, 1))



