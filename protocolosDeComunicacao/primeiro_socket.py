import socket

resp = "S"
while resp == "S":
    url = input("Digite a URL: ")
    ip = socket.gethostbyname(url)
    print("IP address: ", ip)
    resp = input("Digite <S> para continuar: ").upper()
