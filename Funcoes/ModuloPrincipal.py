from Identificacoes_Funcoes import *

minhaLista = []

resp = "S"
while resp == "S":
    print("\n=====================================================================")
    print("1 - Preencher inventario")
    if len(minhaLista) != 0:
        print("2 - Exibir inventario")
        print("3 - Pesquisar um item do inventario")
        print("4 - Depreciar um item do inventario")
        print("5 - Excluir um item do inventario")
        print("6 - Resumir valores do inventario")
    else:
        print("\nLista vazia! Insira itens no inventário para o resto do menu ser exibido!")
    print("\n0 - Sair")
    opc = input("\nDigite a opção desejada: ")

    print("=====================================================================\n")

    if opc == "0":
        break
    elif opc == "1":
        preencherInventario(minhaLista)
    elif opc == "2":
        exibirInventario(minhaLista)
    elif opc == "3":
        localizarPorNome(minhaLista)
    elif opc == "4":
        depreciarPorNome(minhaLista, 20)
    elif opc == "5":
        print(excluirPorSerial(minhaLista))
        exibirInventario(minhaLista)
    elif opc == "6":
        resumirValores(minhaLista)
    else:
        print("Opção inválida!")

print("\nFINALIZADO!!!\n")
