#coding: utf-8

server_port = 19198

from socket import *
import moduloservidor

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)

tm_buffer = 2048

dic_operacoes = { 
	'som':moduloservidor.soma,
	'sub':moduloservidor.subtracao,
	'div':moduloservidor.divisao,
	'mul':moduloservidor.multiplicacao
}

while True:
	
	
	
	print ("Server pronto para aceitar conexao")
	
	conexao, cliente = serverSocket.accept()
	print ("Conexao aceita")
	
	while True:
		try:
			message = conexao.recv(tm_buffer).decode('utf-8')
			if(message=="EXIT"):
				print ("Conexao encerrada")
				conexao.close()
				break
				
			print ("Mensagem recebida:",message)
			msg_split = message.split('#') 
			operacao = msg_split[0]
			num1 = int(msg_split[1])
			num2 = int(msg_split[2])
			resultado = dic_operacoes[operacao](num1,num2)
		except:
			resultado = "ERRO NO SERVIDOR"
		
		conexao.send(bytes(str(resultado), 'utf-8'))
		conexao.close()
		break
		
	
serverSocket.close()
