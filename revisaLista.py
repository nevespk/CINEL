#. Faça um script, recorrendo a funções, que dado um tuplo, retorne os elementos primos que aí existem.
def retorna_primos(tp):
    primos = ()
    for i in tp:
        if (tp[i]) % 2 == 0:
            return False
        if (tup[i]) == 1:
            return False
        if (tup[i]) == 2:
            return True
    return ("É Primo")

tup = (1, 2, 3, 4, 5, 6 ,7, 8, 9, 10)
resp = retorna_primos(tup)
print(tup)