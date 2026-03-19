cores = {"Preto", "Branco", "Azul", "Verde", "Vermelho",
    "Amarelo", "Castanho", "Rosa", "Laranja", "Cinzento"}

dCores = {}

for cor in cores:
    corIngles = input(f"Qual a cor correspondente em inglês para {cor}? ").title()
    dCores[cor] = corIngles

print(dCores)
