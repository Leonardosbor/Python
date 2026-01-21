lista_precos = [1000, 2000, 3000, 4000]
taxa_imposto = 0.1

#Exemplo 1
#for preco in lista_precos:
#    imposto = preco * taxa_imposto
#    print(f'Preço do produto: {preco}; Imposto de R${imposto}')

#Exemplo 2
#for preco in lista_precos:
#    if preco > 1000:
#        taxa = 0.15
#    else:
#        taxa = 0.1
#    imposto = preco * taxa
#    print(f'Preço do produto: {preco}; Imposto: {imposto}')


#Exemplo 3
#total_imposto = 0
#for preco in lista_precos:
#    if preco > 1000:
#        taxa = 0.15
#    else:
#        taxa = 0.1
#    imposto = preco * taxa
#    total_imposto += imposto
#    print(f'Preço do produto: {preco}; Imposto: {imposto}')

#print(f'Total de imposto: R${total_imposto}')


#Exemplo 4
vendas_25 = {'jan': 1000, 'fev': 2000, 'mar': 3000}
vendas_26 = {'jan': 2500, 'fev': 3500, 'mar': 4500}


for mes in vendas_25:
    valor_25 = vendas_25[mes]
    valor_26 = vendas_26[mes]
    crescimento = valor_26 / valor_25 - 1
    print(f'Mês {mes} o crescimento foi de {crescimento:.1%}')



