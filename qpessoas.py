arq = open("pessoas.txt", "r", encoding="utf-8")
linhas = arq.readlines()
arq.close()

cidades = {}
total = len(linhas)

for linha in linhas:
    cidade = linha.strip().split(';')[1]
    cidades[cidade] = cidades.get(cidade, 0) + 1

for cidade in sorted(cidades, key=cidades.get, reverse=True):
    print(f"{cidade:<9} {cidades[cidade]:<7} {(cidades[cidade]/total*100):.1f}%")
