produtos = {'arroz': 5, 'feijão': 10, 'macarrão': 7}

#pegar um item
print(produtos['feijão'])

#adicionar e editar um item
produtos['arroz'] = 7 #alteração de valor de item existente

produtos['carne'] = 15 #inclusão de item novo
print(produtos)

#remover item
produtos.pop('arroz')

#verificar se existem um item
print('feijão' in produtos)
print('carne' in produtos.keys())
print(15 in produtos.values())


produtos = {'arroz': 1, 'feijão': 2, 'macarrão': 3}

produto_buscado = input('Digite o nome do produto: ')
produto_buscado = produto_buscado.strip() #remover espaço vazio
produto_buscado = produto_buscado.lower() #remover qualquer caracter maiúsculo  

if produto_buscado in produtos:
    preco = produtos[produto_buscado]
    print('Produto encontrado!')
    print(f'Produto: {produto_buscado}, Preço: {preco}')
else:
    print('Produto não encontrado!')



