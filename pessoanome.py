nome_busca = input("\nd) Digite o nome da pessoa para ver onde vive: ").strip()
cidades_nome = [p['cidade'] for p in pessoas if p['nome'].lower() == nome_busca.lower()]
if cidades_nome:
    print(f"{nome_busca} vive nas cidades: {', '.join(cidades_nome)}")
else:
    print("Pessoa não encontrada.")

    ###################################
# Abrir o ficheiro CSV
arquivo = open("dados.csv", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()

# Criar lista de pessoas
pessoas = []
for linha in linhas:
    linha = linha.strip()  # remove \n
    if linha == "":
        continue
    partes = linha.split(";")  # separar por ;
    pessoa = {
        'nome': partes[0].strip(),
        'cidade': partes[1].strip(),
        'idade': int(partes[2].strip()),
        'zona': partes[3].strip()
    }
    pessoas.append(pessoa)

# Contar pessoas por cidade
contagem_cidades = {}
for pessoa in pessoas:
    cidade = pessoa['cidade']
    if cidade in contagem_cidades:
        contagem_cidades[cidade] += 1
    else:
        contagem_cidades[cidade] = 1

# Encontrar a cidade com mais habitantes
mais_habitantes = ""
maximo = 0
for cidade in contagem_cidades:
    if contagem_cidades[cidade] > maximo:
        maximo = contagem_cidades[cidade]
        mais_habitantes = cidade

print(f"A cidade com mais habitantes é {mais_habitantes} ({maximo} pessoas)")

