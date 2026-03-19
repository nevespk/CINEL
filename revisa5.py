def extremos(palavras):
    menor = len(palavras[0])
    maior = len(palavras[0])

    for i in range(len(palavras)):
        if len(palavras[i]) < menor:
            menor = len(palavras[i])
        if len(palavras[i]) > maior:
            maior = len(palavras[i])

    return (menor, maior)

palavras = ("ana", "Aviao", "Joaquim")
print (extremos(palavras))