import socket

HOST = 'localhost'
PORTA = 5001


servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind((HOST, PORTA))  

print("Servidor UDP escutando na porta 5001 !!!")

while True:
    
    mensagem, endereco_cliente = servidor_socket.recvfrom(1024)
    print('Mensagem recebida (UDP) ->', endereco_cliente, ':', mensagem.decode())
    
    resposta = f"UDP: {mensagem.decode()}"
    servidor_socket.sendto(resposta.encode(), endereco_cliente)

    print("Resposta do servidor:", resposta)
