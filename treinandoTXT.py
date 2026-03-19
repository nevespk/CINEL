with open("meuteste.txt", "w", encoding="utf-8") as fp:
    fp.write("Vamos ver se funciona\n")
    fp.write("Tenho que analisar com calma")

with open("meuteste.txt", "r", encoding="utf-8") as fp:
    leitura = fp.readlines()
print(leitura)

with open("meuteste.txt", "r", encoding="utf-8") as fp:
    for linha in fp:
        if "ver" in linha:
            print("hello, world!\n\n", "posicção 0: ", linha)