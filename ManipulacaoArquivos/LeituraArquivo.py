# Automaticamente fecha o arquivo ao terminar o bloco do with
with open("./ManipulacaoArquivos/primeiro_arquivo.txt", "r") as arquivo:
    # conteudo = arquivo.read()
    # print(conteudo)
    for linha in arquivo.readlines():
        print(linha)
