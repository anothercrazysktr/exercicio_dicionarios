alunos = {
    "001": {
        "nome": "Vincent",
        "idade": 17,
        "cidade": "Night City",
        "turma": "A",
        "notas": [10, 8, 6, 4]
    },
    "002": {
        "nome": "Johnny",
        "idade": 25,
        "cidade": "Night City",
        "turma": "B",
        "notas": [9, 8, 10, 7]
    },
    "003": {
        "nome": "Judy",
        "idade": 19,
        "cidade": "Night City",
        "turma": "A",
        "notas": [10, 9, 8, 10]
    }
}

def calcular_media(lista_alunos):
    soma = sum(lista_alunos)
    media = len(lista_alunos)
    media_alunos = soma / media
    return media_alunos

def contar_aprovados(lista_alunos):
    aprovados = 0
    for nota in lista_alunos:
        if nota >= 7:
            aprovados += 1
    return aprovados

id_aluno = input("Digite o ID do aluno: ")

print(f"Nome: {alunos[id_aluno]['nome']}")
print(f"Idade: {alunos[id_aluno]['idade']}")
print(f"Cidade: {alunos[id_aluno]['cidade']}")
print(f"Turma: {alunos[id_aluno]['turma']}")
print(f"Notas: {alunos[id_aluno]['notas']}")
print(f"Média: {calcular_media(alunos[id_aluno]['notas'])}")
print(f"Notas Aprovadas: {contar_aprovados(alunos[id_aluno]['notas'])}")

