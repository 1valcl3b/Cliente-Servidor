# Projeto Cliente-Servidor com Sockets TCP e UDP

Este projeto é uma aplicação básica de cliente-servidor em Python que usa conexões TCP e UDP para comunicação. O servidor consegue lidar com várias conexões TCP ao mesmo tempo usando threads, além de responder a mensagens enviadas por UDP.

## Estrutura dos Arquivos

- **`servidor.py`**: Servidor combinado (Threads) que escuta conexões TCP na porta 5000 e UDP na porta 5001.
- **`servidor_tcp.py`**: Versão do servidor TCP.
- **`servidor_udp.py`**: Versão do servidor UDP
- **`cliente.py`**: Cliente que permite escolher entre os protocolos TCP e UDP para enviar mensagens ao servidor e exibir a resposta.

## Pré-requisitos

- Python 3 deve estar instalado na máquina.
- Baixe todos os arquivos (`servidor.py`, `servidor_tcp.py`, `servidor_udp.py`, `cliente.py`) para a mesma pasta.

## Instruções para Execução

### Opção 1: Executando o Servidor com Threads (TCP e UDP)

1. Abra um terminal na pasta onde os arquivos estão salvos.
2. Inicie o servidor com o comando:

   ```bash
   python3 servidor.py

O servidor agora estará escutando conexões TCP na porta 5000 e UDP na porta 5001.

### Opção 2: Executando Servidores Separados (TCP e UDP)

1. Abra dois terminais, um para cada servidor.
2. No primeiro terminal, execute o servidor TCP:

   ```bash
   python3 servidor_tcp.py

3. No segundo terminal, execute o servidor UDP:

   ```bash
   python3 servidor_udp.py

### Executando o Cliente

1. Abra um novo terminal para o cliente.
2. Execute o cliente com o comando:

   ```bash
   python3 cliente.py

3. O cliente solicitará que você escolha o protocolo (TCP ou UDP) e digite uma mensagem para enviar ao servidor. Após enviar, a resposta será exibida com o prefixo do protocolo escolhido.


### Exemplo

Após iniciar o servidor, você verá mensagens indicando que ele está escutando nas portas:

   ```bash
Servidor TCP escutando na porta 5000!
Servidor UDP escutando na porta 5001!
```

Quando o cliente envia uma mensagem, o servidor exibe o conteúdo e o endereço do cliente.

### No Cliente
Ao executar o cliente, selecione o protocolo e insira uma mensagem. Exemplo:

   ```bash
Digite o protocolo (TCP ou UDP): TCP
Digite a mensagem a ser enviada: Olá, servidor!
Resposta do servidor: TCP: Olá, servidor!
```
