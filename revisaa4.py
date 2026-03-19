def soma_lista(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

valores = [2,3, 4, 5, 6, 9]
resp = soma_lista(valores)
print(resp)