def boletim_aluno(aluno):

    if aluno['nota'] >= 7:
        return 'APROVADO'
    
    if 5 <= aluno['nota'] <= 6.9:
        return 'RECUPERAÇÃO'

    return 'REPROVADO'



def boletim_turma(lista_alunos):
    
    resultado = []

    for aluno in lista_alunos:
        situacao = boletim_aluno(aluno)
        texto = f"{aluno['nome']} - {situacao}"
        resultado.append(texto)
        
    return resultado


turma = [
    {'nome': 'Ana', 'nota': 8},
    {'nome': 'Carlos', 'nota': 5.5},
    {'nome': 'João', 'nota': 3}
]

print(boletim_turma(turma))
    