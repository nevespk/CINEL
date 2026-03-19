with open("FalaFacil.txt", "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

linhas = texto.count("\n") + 1
quebrasL = texto.count("\n")

vogais_lista = "aeiouAEIOU"
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

vogais = 0
consoantes = 0

for letra in texto:
    if letra in alfabeto:  # verifica manualmente se é letra
        if letra in vogais_lista:
            vogais += 1
        else:
            consoantes += 1

print("Linhas:", linhas,"- Vogais:", vogais,"- Consoantes:", consoantes,"- Quebras de Linha \\n:", quebrasL)