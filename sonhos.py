"""exemploTxt = open("meus_sonhos.txt", "w", encoding="utf-8")
exemploTxt.write("Passar em python.\n")
exemploTxt.write("Aprender mais e mais, yes.\n")
exemploTxt.write("Vai chegar.\n")
exemploTxt.close()
print("Sucesso!")
#############################################
txtExemplo = open("meus_sonhos.txt", "r")
conteudo = txtExemplo.read()
txtExemplo.close()
print("Conteúdo:")
print(conteudo)
##################################

arq = open("meus_sonhos.txt", "r")
print("««Linha por linha (Com ciclo)»»\n")
for linha in arq:
    print(f"{linha}", end="")

arq.close()

arq = open("meus_sonhos.txt", "r")
linhas = arq.readlines()
arq.close()

print("\nLista De Linhas:", linhas)
print("primeira linha:", linhas[0])
print("segunda linha:", linhas[1])"""
"""with open("test.txt", "w", encoding="utf-8") as arq:
    arq.write("Olá,\n")
    arq.write("Tudo bem?")

with open("test.txt", "r", encoding="utf-8") as arq:
    for linha in arq:
        print(linha, end="")"""

try:
    with open("arquivo_que_nao_existe.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Ops! Esse arquivo não existe! Verifique o nome.")

