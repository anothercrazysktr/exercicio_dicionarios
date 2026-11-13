alunos = {"001":{
        "nome": "Vincent",
        "idade": 17,
        "cidade": "Night City",
        "turma": "A",
        "notas": [10, 8, 6, 4]}}

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
    aprovados = contar_aprovados(notas)
    return len(notas), aprovados, calcular_media(notas), len(notas) - aprovados

    print(f"Nome:{alunos["001"]["nome"]}")
    print(f"Idade:{alunos["001"]["idade"]}")
    print(f"Turma:{alunos["001"]["turma"]}")
    print(f"Cidade:{alunos["001"]["cidade"]}")
