def maior_numero(a, b):
    if a == b:
        return 'São iguais!'
    return a if a > b else b
    
print(maior_numero(7, 7))