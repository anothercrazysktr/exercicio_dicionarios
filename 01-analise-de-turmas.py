turma_a = [8, 5, 9, 6]
turma_b = [7, 8, 10, 3]
turma_c = [10, 10, 5, 6, 8, 9]

turmas = [turma_a, turma_b, turma_c]

def contar_aprovados(notas):
    aprovados = 0
    for nota in notas:
        if nota >= 7:
            aprovados += 1
    return aprovados

def calcular_media(notas):
    soma = sum(notas)
    media = len(notas)
    media_alunos = soma / media
    return media_alunos

def relatorio_turmas(notas):
    return contar_aprovados(notas), calcular_media(notas)

for indice, turma in enumerate(turmas):
    print(f"\nTurma: {indice + 1}\nAprovados: {contar_aprovados(turma)}\nMédia: {calcular_media(turma)}")
