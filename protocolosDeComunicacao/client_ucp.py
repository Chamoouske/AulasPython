from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

msg = bytes(input("Digite algo: "), "utf-8")
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = "X"

while saida != "X":
    msg = input("Digite algo: ")
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(655365)
    print("Resposta do servidor: ", dados.decode())
    saida = input("Digite <X> para sair: ")

obj_socket.close()
