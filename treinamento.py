cores = ['preto', 'branco', 'verde']
corDicio = {}

for cor in cores:
    corIng = input(f"Qual a cor correspondente em ingles para {cor}?")
    corDicio[cor]= corIng
print(corDicio)

with open('verificaCor.txt','w', encoding='utf-8') as fp:
    for corPt, corIng in corDicio.items():
        fp.write(f"{corPt}; {corIng}\n")