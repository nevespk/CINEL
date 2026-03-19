def par_impar(tup):
    par = []
    impar = []
    for i in range(len(tup)):
        if tup[i] % 2 == 0:
            par.append(tup[i])
        else:
            impar.append(tup[i])
    return (tuple(par), tuple(impar))

resultado = par_impar((1, 2, 7, 9, 11))
print("Par | Ímpar")
print(resultado)