import socket

def scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conex = s.connect_ex((ip, port))
    s.close()

    if conex == 0:
        print(ip, port, "Open")
        return True
    else:
        print(ip, port, "closed")
        return False

target = input("Digite o seu alvo: ")
for c in range(1,100):
    scanner(target,c)