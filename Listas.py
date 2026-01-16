lista_vendas = [100, 50, 1000, 800, 35]
print(lista_vendas[0]) #pegar um item da lista
print(len(lista_vendas)) #tamanho da lista
print(sum(lista_vendas)) #somar todos os itens
print(max(lista_vendas)) #maior valor da lista
print(min(lista_vendas)) #menor valor da lista

total_vendas = sum(lista_vendas)
qtde_vendas = len(lista_vendas)
print(total_vendas / qtde_vendas) #média de vendas


#encontrar um elemento (posição)
lista_produtos = ['computador', 'video game', 'guitarra', 'contrabaixo']
print('computador' in lista_produtos)

posicao = lista_produtos.index('guitarra')
print(posicao)

pedaco_lista = lista_produtos[posicao:]
print(pedaco_lista)


#editar um item
lista_preco = [100, 200, 300, 400, 500]
novo_preco = lista_preco[0] * 1.1
lista_preco[0] = novo_preco
print(lista_preco)


#remover um item da lista
lista_produtos.remove('guitarra') #edita a lista original
print(lista_produtos)

item_removido = lista_produtos.pop(0) #edita a lista pelo índice
print(item_removido)