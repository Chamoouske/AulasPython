import json

with open("./ManipulacaoArquivos/db.json", "r") as arquivo:
    dicionario = json.load(arquivo)
    for chave, dados in dicionario.items():
        print(chave + ": " + str(dados))

    # Como salvar informações em um arquivo JSON
    with open("./ManipulacaoArquivos/db1.json", "w") as json_file:
        json.dump(dicionario, json_file)
