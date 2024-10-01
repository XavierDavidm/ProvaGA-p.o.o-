# Lista de exercicíos 1

# .1-Utilizando o OnlineGDB, pesquise e implemente um programa que escreva na tela “Olá
#Mundo!” em 3 linguagens de programação diferentes. Qual é o comando de saída de
#dados nestas 3 linguagens?
# o comando em java é print
# o comando em go é fmt.println
# o comando em c# é Console.writeLine

# .2-Escreva um programa em linguagem Python que solicite o nome do usuário e, em seguida,
#imprima uma mensagem de boas-vindas na tela, utilizando o nome fornecido.
nome = input('Digite seu Nome:')
print('Bem vindo',nome)

# .3-Escreva um programa em Python que realize o seguinte procedimento:
#a. Imprima na tela a seguinte questão: Qual é o verdadeiro nome do super-herói
#Batman?
#b. Apresente cinco alternativas para o usuário, cada uma em uma linha: a) Bruce
#Wayne b) Clark Kent c) Peter Parker d) Tony Stark e) Steve Rogers
#c. Armazene a letra correspondente à resposta correta (‘a’) em uma variável.
#d. Solicite ao usuário que digite sua resposta, e a armazene em uma variável.
#e. Ao final, o programa deve exibir na tela a resposta do usuário e a resposta correta.
#Por exemplo, se o usuário digitou como resposta a alternativa ‘d’, a mensagem
#seria esta:
#Você respondeu alternativa d. A resposta correta é a alternativa a

print('Qual é o verdadeiro nome do super-herBatman?')
print('A)Bruce Wayne')
print('B)Clark Kent')
print('C)Peter Parker')
print('D)Tony Stark')
print('E)Steve Rogers')
resposta = input('qual é a resposta correta? ')
print('a resposta correta é A) e voce respondeu', resposta)

# .4-Como poderíamos tornar o programa acima mais genérico, de maneira que pudéssemos
#registrar qualquer questão objetiva com 5 alternativas?]
 
#COLOCANDO PERGUNTAS COMO VARIAVEIS exemplo 5 

pergunta = '7+3 é igual a?' 
resposta1 = '10'
resposta2 = '11'
resposta3 = '9'
resposta4 = '5'
resposta5 = '-10'
correta = resposta1
print(pergunta)
print(resposta1)
print(resposta2)
print(resposta3)
print(resposta4)
print(resposta5)
respostaDoUsuario = input('qual é a resposta correta? ')
print('a resposta correta é ',correta,'e voce respodeu: ',respostaDoUsuario)

#fim lista 1