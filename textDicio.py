# Primeiro, carregar os dados do ficheiro
dados = {}

with open("clientes.csv", "r", encoding="utf-8") as fp:
    conteudo = fp.read().split("\n")
    for linha in conteudo:
        if linha.strip():  # Ignorar linhas vazias
            info = linha.split(";")
            nif = info[0]
            dados[nif] = info[1:]

print("Dados originais:")
print(dados)
print("\n")

dados_completos = {}
for nif, info in dados.items():
    dados_completos[nif] = {
        "nome": info[0],
        "cidade": info[1],
        "idade": int(info[2]),
        "zona": info[3]
    }
print("dados2")
print(dados_completos)