# Aplicação Cliente-Servidor com Sockets TCP e UDP

Este projeto implementa um sistema de comunicação entre cliente e servidor usando sockets TCP e UDP em Python. O servidor é capaz de gerenciar conexões TCP e UDP simultaneamente em diferentes portas e utiliza threads para atender múltiplos clientes TCP ao mesmo tempo.

Estrutura dos Arquivos
servidor.py: Código do servidor que escuta as portas TCP (5000) e UDP (5001). O servidor usa threads para atender múltiplos clientes TCP e responde a mensagens UDP.
cliente.py: Código do cliente que permite enviar mensagens para o servidor usando TCP ou UDP, com resposta recebida e exibida na tela.
Pré-requisitos
Python 3 instalado na máquina.
Clonar ou baixar os arquivos servidor.py e cliente.py.
Instruções para Execução
Passo 1: Iniciar o Servidor
Abra um terminal ou prompt de comando na pasta onde está localizado o arquivo servidor.py.

Execute o seguinte comando para iniciar o servidor:

bash
Copiar código
python3 servidor.py
O servidor deve exibir mensagens indicando que está escutando conexões TCP na porta 5000 e conexões UDP na porta 5001.

Passo 2: Executar o Cliente
Em um novo terminal ou prompt de comando, navegue até a pasta onde o arquivo cliente.py está salvo.

Execute o cliente com o comando:

bash
Copiar código
python3 cliente.py
O cliente solicitará que você escolha o protocolo (TCP ou UDP) e insira uma mensagem.

Após enviar a mensagem, o cliente exibirá a resposta do servidor com o prefixo "TCP:" ou "UDP:" de acordo com o protocolo escolhido.

Exemplo de Funcionamento
1. Executando o Servidor
No terminal do servidor, você deve ver algo semelhante ao seguinte:

plaintext
Copiar código
Servidor TCP escutando na porta 5000!
Servidor UDP escutando na porta 5001!
Quando um cliente se conecta, o servidor exibe a mensagem recebida e a resposta enviada.

2. Enviando uma Mensagem do Cliente
Ao executar cliente.py, digite o protocolo desejado (TCP ou UDP) e a mensagem que deseja enviar. Por exemplo:

plaintext
Copiar código
Digite o protocolo (TCP ou UDP): TCP
Digite a mensagem a ser enviada: Olá, servidor!
O cliente exibirá a resposta do servidor, como:

plaintext
Copiar código
Resposta do servidor: TCP: Olá, servidor!
Observações
Para testar o sistema com múltiplos clientes, você pode abrir várias janelas de terminal e executar cliente.py em cada uma, selecionando protocolos e enviando mensagens.
Certifique-se de que o servidor (servidor.py) esteja em execução antes de iniciar o cliente (cliente.py).
