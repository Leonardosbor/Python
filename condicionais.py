time = ['cruzeiro', 'boca juniors', 'river plate']
novo_time = input('Insira um novo time:' )

if novo_time in time:
    print('Time já está incluso!')
else:
    print(f'{novo_time} incluído com sucesso!')
    time.append(novo_time)

print(time)



vendas = 2000

#Exemplo 1
if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000:
        bonus = 100
   else: 
        bonus = 0
print(f'Bônus do funcionário: {bonus}')

#Exemplo 2
if vendas >= 5000:
    bonus = 500
elif vendas < 5000:
    bonus = 100
else:
    bonus = 0

print(f'Bônus do funcionário: {bonus}')


#Exemplo 3
vendas_empresa = float(input('Insira o valor: '))
meta_empresa = 100_000
vendas_funcionario = float(input('Insira o valor: '))

if vendas_funcionario >= 15_000 and vendas_empresa >= meta_empresa:
    print('Bateu todas as metas!')
    bonus = 500
elif vendas_funcionario >= 5_000 and vendas_empresa >= meta_empresa:
    print('Não bateu todas as metas!')
    bonus = 100
else:
    print('Nenhuma meta batida!')
    bonus = 0
print(f'Bônus do funcionário: {bonus}')

