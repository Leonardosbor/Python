def boletim(dicionario):
    
    nota = dicionario['nota']

    if nota >= 7:
        return 'APROVADO'
            
    if 5 <= nota <= 6.9:
        return 'RECUPERAÇÃO'
        
    return 'REPROVADO'
    
    
             
