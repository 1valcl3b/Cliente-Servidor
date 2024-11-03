'''
s = socket
'''

import socket
import threading

HOST = 'localhost'
PORTA_TCP = 5000
PORTA_UDP = 5001

#Thread TCP
def cliente_tcp(conexao, endereco):
    print('Conexão TCP recebida ->', endereco)
    mensagem_cliente = conexao.recv(1024).decode()
    print('Mensagem recebida (TCP) ->', mensagem_cliente)
    
    #Responde com o prefixo "TCP:"
    resposta = f"TCP: {mensagem_cliente}"
    conexao.send(resposta.encode())
    
    #Fechar a conexão
    conexao.close()

#servidor UDP
def servidor_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORTA_UDP))
    print("Servidor UDP escutando na porta 5001 !!!")

    while True:
        mensagem, endereco_cliente = s.recvfrom(1024)
        print('Mensagem recebida (UDP) ->', endereco_cliente, ':', mensagem.decode())
        
        #Responde com o prefixo "UDP:"
        resposta = f"UDP: {mensagem.decode()}"
        s.sendto(resposta.encode(), endereco_cliente)
        print("Resposta do servidor (UDP):", resposta)

# Função principal do servidor para aceitar conexões TCP
def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORTA_TCP))
    s.listen()
    print("Servidor TCP escutando na porta 5000 !!!")

    while True:
        conexao, endereco = s.accept()
        #Cria uma nova thread para cada cliente TCP
        threading.Thread(target=cliente_tcp, args=(conexao, endereco)).start()

# Inicializa o servidor UDP em uma thread 
threading.Thread(target=servidor_udp, daemon=True).start()

# Inicia o servidor TCP na thread principal
tcp_server()
