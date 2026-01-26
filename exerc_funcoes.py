#se o preço for maior que 100 → 10% de desconto
#se o preço for menor que 100 → não tem desconto 

def desconto_produto(preco_produto):

    if preco_produto >= 100:
        desconto = preco_produto * 0.10
        preco_final = preco_produto - desconto
        return preco_final
        
resultado = desconto_produto(120)
print(resultado)
    



    


