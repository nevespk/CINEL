aluno = {
    "nome": "joao",
    "idade": 20,
    "curso": "CET Sistemas de Informação"
}
'''print (aluno["nome"])
aluno["nome"] = "Elin"
print(aluno["nome"])
print(aluno["idade"])

print(aluno)'''

for chave in aluno:
    print(chave, ":", aluno[chave])

if "email" in aluno:
    print("email:", aluno["email"])
else:
    print("\nEmail nao encontrado")

del aluno["idade"]
print(aluno)

if "idade" not in aluno:
    print("A idade não está aqui :(")

notas = {
    "mat": 8,
    "pt":10,
    "geo": 9
}

soma = 0

for disciplinas, valor in notas.items():
        print(disciplinas, ":", valor)
        soma += valor
media = soma/len(notas)

print("média: ", media)