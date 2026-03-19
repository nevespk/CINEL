lista = []

for i in range(3):
    valores = int(input(f"Digite o {i+1}º valor para a lista: "))
    lista.append(valores)
    if valores == -1:
        break
    abc = tuple(lista)
print(abc)