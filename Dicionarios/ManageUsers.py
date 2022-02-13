from Dicionarios.Funcoes import inserir
from Funcoes import perguntar

usuarios = {}

opcao = "I"
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    opcao = perguntar()

    if opcao == "I":
        inserir(usuarios)
