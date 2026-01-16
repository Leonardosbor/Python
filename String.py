faturamento = 1000
custo = 600

lucro = faturamento - custo

texto = 'O lucro foi de ' + str(lucro) + ' e o faturamento foi de ' + str(faturamento)

print(texto)

texto = f'O lucro foi de R${lucro} e o faturamento foi de R${faturamento}'
print(texto)

email = ' EMAIL_FALSO@gmail.com '
email = email.lower() # letra minúscula
email = email.strip() # ajustar espaços vazios
print(email)
print(len(email)) # número de caracteres

posicao = email.find('@') # encontrar a posição de um caracter
print(posicao)

print(email[1]) # localizar parte do texto
print(email[1:4]) # pega pedaço do texto
print(email[1:]) # pega até o final

novo_email = email.replace('gmail.com', 'yahoo.com.br')
print(novo_email) # trocar parte de um texto

nome = 'leonardo reis'
nome = nome.capitalize() # 1ª letra maiúscula
print(nome) # Leonardo reis

nome = nome.title() # 1ª letra de cada palavra maiúscula
print(nome) # Leonardo Reis

nome = nome.upper() # todas as letras maiúsculas
print(nome) # LEONARDO REIS


# formatação numérica

faturamento = 1_000_000
custo = 60_000

lucro = faturamento - custo
margem = lucro / faturamento
texto = f'o lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de R${margem:.0%}'
print(texto)


# exercício
nome = 'Leonardo Reis'
email = 'leonardoreis2026@gmail.com'

# pegar o servidor do email
posicao = email.find('@')
servidor = email[posicao:] #[posicao+1:] → pra não pegar o @
print(servidor)

#pegar o primeiro nome do usuário
posicao_espaco = nome.find(' ')
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)