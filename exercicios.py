def boletim_aluno(aluno):

    if aluno['nota'] >= 7:
        return 'APROVADO'
    
    if 5 <= aluno['nota'] <= 6.9:
        return 'RECUPERAÇÃO'

    return 'REPROVADO'



def resumo_turma(lista_alunos):

    contador = {
        'Aprovados': 0,
        'Recuperação': 0,
        'Reprovados': 0
    }


    for aluno in lista_alunos:
        situacao = boletim_aluno(aluno)

        if situacao == 'APROVADO':
            contador['Aprovados'] += 1
        
        elif situacao == 'RECUPERAÇÃO':
            contador['Recuperação'] += 1
        
        else:
            contador['Reprovados'] += 1
        
    return contador


turma = [
    {'nome': 'Ana', 'nota': 8},
    {'nome': 'Carlos', 'nota': 5.5},
    {'nome': 'João', 'nota': 3},
    {'nome': 'Maria', 'nota': 9}
]

print(resumo_turma(turma))






    