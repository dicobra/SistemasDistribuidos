#coding :utf-8

import socket
import subprocess
from time import sleep

host = '127.0.0.1'
porta = 5000
msg = ""
tamanho=0
while True:
	try:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.connect((host,porta))
	except:
		print ('\033[0;31;40mNao conectado no servidor\033[m')
	msg = input("digite uma msgn ")
	if msg == 'SAIDA' or msg == 'saida':
		print ("finalizando conexao")
		tcp.close()
		break
	print (msg)
	try:
		tcp.sendall(bytes(msg, 'utf-8'))
		tamanho = tcp.recv(10)
		tamanho = int(tamanho.decode('utf-8'))
		if tamanho > 0:
			retorno = tcp.recv(tamanho)
			retorno = retorno.decode('utf-8')
		print ('\033[0;31;40mExecutado do servidor!!!!\033[m')
		print (retorno)
		tcp.close()
		sleep(1.5)
	except:
		print ('\033[0;31;40mExecutado local!!!!\033[m')
		retorno = subprocess.getoutput(msg)
		print (retorno)
