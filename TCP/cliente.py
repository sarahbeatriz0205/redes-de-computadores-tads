import socket
porta = 444
servidor = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((servidor, porta)) 
msg = input("Qual a mensagem? > ")
s.send(msg.encode("utf-8"))
resposta = s.recv(1024)
print("Resposta")