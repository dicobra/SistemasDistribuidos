#coding :utf-8

import socket
import subprocess
import time

porta = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(("",porta))
tcp.listen(1)
while True:
	con, cliente = tcp.accept()
	while True:		
		print ("Cliente conectado:",cliente)
		cmd = con.recv(1024)
		cmd= cmd.decode('utf-8')
		if cmd == 'SAIDA' or cmd == 'saida':
			print ("finalizando conexao")
			con.close()
			break
		print ("Comando --->",cmd)
		retorno = subprocess.getoutput(cmd)
		tamanho = len(retorno)
		if tamanho == 0:
			retorno = 'Comando sem retorno'
			tamanho = len(retorno)		
		con.send(bytes(str(tamanho).zfill(10), 'utf-8'))
		con.send(bytes(retorno,'utf-8'))
		break
tcp.close()
