#comandos


arqEscrita=open('nomeArquivo.txt','w')

#w= cria ou sobrescreve arquivo já criado
#a= cria ou adiciona coisas em um arquivo existente


arqEscrita.write('kk')
#conteudo dentro de '' é escrito no arquivo
#ou
meuTexto='00000'
arqEscrita.write(meuTexto) 
#escreve o conteudo da variavel no arquivo

#lembrete sempre fechar o arquivo
arqEscrita.close()

#(chr) escreve o simbolo correspondente

#(ord('A')) escreve o número que correspondente ao simbolo escolhido

#1 cifra

def cifrarMensagem(msg):
    msgCifrada=''
    for i in range(len(msg)):
        code=ord(msg[i]) -1
        msgCifrada += chr(code)
    return(msgCifrada)

#############

msg=input('digite uma mensagem: ')

msgCifrada=cifrarMensagem(msg)
print(msgCifrada)

nomeArquivo=input('digite o nome do arquivo que deseja: ')
arqEntrada=open(nomeArquivo,'w')

arqEntrada.write(msgCifrada)
arqEntrada.close()

