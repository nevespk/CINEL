coresPt = ['Preto', 'Branco', 'Azul', 'Amarelo', 'Rosa',
         'Castanho', 'Cinzento', 'Laranja', 'Verde']

i = 0
coresDict = {}
while i < len(coresPt):
    corIngles = input(f"Qual a cor correspondente em ingles para {coresPt[i]}?")
    coresDict[coresPt[i]] = corIngles
    i += 1
print(coresDict)