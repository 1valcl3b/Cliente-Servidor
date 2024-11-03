import socket

HOST = 'localhost'
PORTA_TCP = 5000
PORTA_UDP = 5001


protocolo = input("(TCP / UDP): ").upper()
mensagem = input('Mensagem: ')

if protocolo == "TCP":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria um socket tcp usando ipv4
    s.connect((HOST, PORTA_TCP))  # Conecta ao servidor TCP na porta 5000
    s.send(mensagem.encode())  # Envia a mensagem
    resposta = s.recv(1024).decode()  # Recebe e decodifica a resposta
    s.close()  # Fecha o socket

elif protocolo == "UDP":
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(mensagem.encode(), (HOST, PORTA_UDP))
    resposta, _ = s.recvfrom(1024)  # Recebe a resposta
    resposta = resposta.decode()  # Decodifica a resposta
    s.close()

print("Resposta do servidor:", resposta)
