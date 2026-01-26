#se o preço for maior que 100 → 10% de desconto
#se o preço for menor que 100 → não tem desconto 

def desconto_produto(preco_produto):

    desconto = preco_produto * 0.10
    preco_final = preco_produto - desconto

    if preco_produto >= 100:
        return preco_final
    else:
        return preco_produto
    
resultado = desconto_produto(80)
print(resultado)
    



    


