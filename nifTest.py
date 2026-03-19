with open("clientes.csv", "r", encoding="utf-8") as fp:
    dados = {}
    nif_procurado = input("Introduza um NIF para consultar: ")
    if nif_procurado in dados:
        print(f"\nInformação para o NIF {nif_procurado}:")
        print(dados[nif_procurado])


        info = dados[nif_procurado]
        print(f"Nome: {info['nome']}")
        print(f"Cidade: {info['cidade']}")
        print(f"Idade: {info['idade']}")
        print(f"Zona: {info['zona']}")
    else:
        print(f"NIF {nif_procurado} não encontrado.")