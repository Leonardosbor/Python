def verificar_ruptura(lista_numeros):
    for item in lista_numeros:
        if item == 0:
            return True
    return False 
    

print(verificar_ruptura([10, 45, 2, 0, 15]))