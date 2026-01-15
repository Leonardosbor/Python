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

