import socket

HOST = 'localhost'
PORTA = 5000


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um socket IPV4/tcp

socket_servidor.bind((HOST, PORTA))
socket_servidor.listen()
print('Escutando conexões TCP')

while True:
    # Aceita uma conexão
    conexao, endereco = socket_servidor.accept()
    print('Conexão recebida de ->', endereco)

    # Recebe a mensagem
    mensagem_cliente = conexao.recv(1024).decode()
    print('Mensagem recebida (TCP) ->', mensagem_cliente)

    # Envia a resposta para o cliente
    resposta = f"TCP: {mensagem_cliente}"
    conexao.send(resposta.encode())

    # Fecha a conexão com o cliente
    conexao.close()
