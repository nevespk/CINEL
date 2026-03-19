#guardar o nome de 5 cidade numa lista

listaCidades = []

for i in range(5):
    nomesCidades= input(f"Digite a {i+1}ª cidade: ")
    listaCidades.append(nomesCidades)
print(f"Cidades = {listaCidades}")