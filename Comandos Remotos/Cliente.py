#coding :utf-8

#criado em python 3.6.5

import socket

host = '127.0.0.1'
porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host,porta)) 
msg = ""
while True:
	msg = raw_input ("digite uma msgn ")
	print (msg)
	tcp.sendall(msg)
	if msg == 'SAIDA':
		print ("finalizando conexao")
		tcp.close()
		break
	try:
		retorno = tcp.recv(100000)
		print (retorno)
	except:
		print("nao houve retorno")
