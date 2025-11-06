import socket
porta = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind("0.0.0.0", porta)
s.listen(1)
clientesocket, address = s.accept()
print(f"Conexão com {address} estabelecida")
msg = clientesocket.recv(512)
mensagem = msg.decode("utf-8")
print(f"Recebido: {mensagem}")
resposta = "Obrigado por falar comigo!"
clientesocket.send(bytes(str(resposta), "utf-8"))
clientesocket.close()