#pedir 10 valores e converter num tuplo

valores = []

for i in range(10):
    entradaValores = int(input(f"Digite o {i+1}º valor: "))
    valores.append(entradaValores)
tuplo = tuple(valores)
print(f"Tuplo = {tuplo}")