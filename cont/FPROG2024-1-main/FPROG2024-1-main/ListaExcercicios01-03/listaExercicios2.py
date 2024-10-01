#.1- Faça um algoritmo que leia uma quantidade de tempo em minutos e escreva o tempo equivalente 
#em segundos na tela.
#float(numeros reais) e int(numeros inteiros) convertem o input para valores logicos possibilitando contas
minutos = float(input('quantos minutos? '))
segundos = minutos*60
print(minutos, 'minutos equivalem','a',segundos,'segundos')

#.2- Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a 
#cotação do dólar para real, a quantidade de dólares que o turista deseja comprar, e calcule o valor 
#total em reais que ele precisará pagar.

dolarcotacao=4.97 
print('a atual cotação do dolar para real é',dolarcotacao)
quantidade = float(input('quantos dolares deseja comprar? '))
total=dolarcotacao*quantidade
print('você precisa pagar',total,'reais para ter',quantidade,'dolares!')

#.3- Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso 
#do prato do cliente e calcule o valor a ser pago.

porquilo=40.00
peso=float(input('informe o peso do prato: '))
valorbuffet=peso*porquilo
print('você devera pagar',valorbuffet,'reais por',peso,'quilos de comida')

#.4- Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau
#A e do grau B e escreva o resultado na tela. Lembrando que o Grau A vale 1/3 e o Grau B 2/3

mediaA=float(input('digite sua nota do grau A: '))
mediaB=float(input('digite sua nota do grau B: '))
mediaFinal= round(mediaA*1/3 + mediaB*2/3)
print('sua media A foi ',mediaA,'sua media B foi ',mediaB,'então sua media final é',mediaFinal)

#.5- Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
#preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
#litros ele conseguiu colocar no tanque e exiba na tela.
precoLitroGasolina=5.50
dinheiroMotorista=float(input('digite o valor disponivel: '))
totalLitros=round(dinheiroMotorista/precoLitroGasolina)
print('você colocou',totalLitros,'Litros de gasolina no tanque')

#.6- A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
#de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
#do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
#um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
#arrecadado.
precosmartphone=1000
precotablet=1500
smartphonesVendidos=int(input('quantos smartphones vendemos hoje? '))
tabletsVendidos=int(input('quantos tablets vendemos hoje? '))
totalvendastechmundo= (smartphonesVendidos*precosmartphone)+(tabletsVendidos*precotablet)
print('vendemos',smartphonesVendidos,'smartphones e',tabletsVendidos,'tablets hoje e obtivemos',totalvendastechmundo,'de lucro')

#.7-Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus
#pássaros. Cada pássaro consome 30 gramas de ração por dia. Escreva um programa que leia o
#número de pássaros que o criador possui e calcule a quantidade total de ração necessária por dia.
racao=30
numeroDePassaros=int(input('quantos passáros você possui? '))
totalRacaoDiaria=racao*numeroDePassaros
print('para alimentar',numeroDePassaros,'passáros você precisa de',totalRacaoDiaria,'gramas de ração por dia')

#.8-Um usuário deseja converter a temperatura de Celsius para Fahrenheit. Escreva um programa que
#leia a temperatura em Celsius e exiba a temperatura equivalente em Fahrenheit.
celsius=float(input('quantos graus celsius: '))
fahrenheit=celsius*1.8+32
print(celsius,'graus celsius são',fahrenheit,'graus na escala fahrenheit de temperatura')

#.9-Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas
#pelos clientes. Faça um programa que leia o valor da compra e escreva o valor da compra com o
#desconto.
valorCompra=float(input('digite o valor da compra: '))
desconto=1-0.15
valorFinalDaCompra=valorCompra*desconto
print('a sua compra de',valorCompra,'reais recebeu um desconto de 15%, o total fica',valorFinalDaCompra,'reais')

#.10-O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que
#você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
#e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
#valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
#desconto e o valor da compra.
camiseta=float(input('informe o numero de camisetas compradas: '))
calça=float(input('informe o numero de calças compradas: '))
cinto=float(input('informe o numero de cintos comprados: '))
valorCamiseta=25.00 * camiseta
valorCalça=100.00 * calça
valorCinto=40.00 * cinto
totalLoja=valorCamiseta+valorCalça+valorCinto
descontoRoupas=1-0.10
ValorFinalRoupas=totalLoja*descontoRoupas
print('você comprou',totalLoja,'reais em roupas e recebeu um desconto de 10%, o valor final com desconto ficou',ValorFinalRoupas,'reais')
