faturamento = input('Preencha com o faturamento: ')
faturamento = faturamento.replace('R$', ' ').replace(',', '.')
faturamento = float(faturamento) 
custo = 600

lucro = faturamento - custo
print(lucro)


vendas_dia1 = float(input('Vendas dia 1: '))
vendas_dia2 = float(input('Vendas dia 1: '))

print(vendas_dia1 + vendas_dia2)


