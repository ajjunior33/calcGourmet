from functions import *
lista1=[] #Somente IP ordenado com os pontos
lista2=[] #Somente as Mascaras ordenadas com os pontos
lista3=[] #Somente as mascaras sem ordem de pontos
ip = [] #Lista de IP sempardos pelo split
ipBin = []#Lista de IP em binario sempardos
mascara = []#Lista de Mascaras sempardas pelo split
mascaraBin = [] #Lista de Mascaras separadas
enderecoRede = [] #Endereço de rede de cada ip e mascara separados
enderecoBroadcast = [] #Endereço de Broadcast de cada ip e mascara separados
arq = open("ip.txt", "r") #Ler o arquivo ip.txt atraves da variavel arq
tam = 0 #verifica o tamanho, quantidade de IP E Mascaras que contem no arquivo
for i in arq: #começa uma contagem dentro do arq
	a = limpar(i) #pega aquela posição do arquivo e retira a quebra de linha e as pontuacoes
	if(tam % 2 == 0): #verifica se a posicao e par
		ip.append(a) #se for par cadastra dentro da lista de ip
		lista1.append(juntar(a, 1)) # se for par cadastra o ip dentro da lista1
	else:
		mascara.append(a) #se for impar cadastra como mascara
		lista2.append(juntar(a, 1))#se for impar cadastra como mascara separdas
		lista3.append(juntar(a, 0))#se for impar cadastra como mascara juntas
	tam = tam + 1 #pega o tamanho atual e soma mais um
arq.close() #termina com o arquivo


trans(ip, ipBin) #pega o ip cadastrado na lista de ip, converte para binario e salva na lista de ip em binario
trans(mascara, mascaraBin) #pega a mascara cadastrada na lista de mascara, converte para binario e salva na lista de mascara em binario

arq = open("arq.txt", "w") #atraves da variavel arq abre e cria um novo arquivo e escreve nele
arq.write("Calculadora IPv4\n") # escreve Calculadora IPv4 no topo do arquivo
("-------------------------------\n") #espaçamento
x = 0 #contador utilizado para verificar o andamento do programa
tam = tam/2 #pega o tamanho da lista e divide por dois.'
while(x != tam): #enquanto a variavel x estiver diferente da variavel tam faça
	ip1 = list(''.join(ipBin[x])) #pega o ip cadastrado na lista ipBin e agrupa
	mascara = list(''.join(mascaraBin[x])) #pega a mascara cadastrada na lista mascaraBin e agrupa
	a = endRede(ip1, mascara, 0, enderecoRede) #pega os ips e mascaras separados zera e salva na lista
	b = endRede(ip1, mascara, 1, enderecoBroadcast)#pega os ips e mascaras separados unza e salva na lista

	arq.write("IP: {}\n".format(lista1[x])) #escreve o IP, naquela posicao no arquiv
	arq.write("MASCARA {}\n".format(lista2[x]))#escreve a Mascara, naquela posicao no arquiv
	arq.write("IP Binario: {}\n".format(juntar(ipBin[x],1))) #Escreve Ip em binario
	arq.write("Mascara Binario: {}\n".format(juntar(mascaraBin[x],1))) #Escreve Mascara em binario
	arq.write("Hosts {}\n".format(calcHost(mascaraBin, x))) #escreve a quantidade de hosts
	arq.write("Hosts Disponiveis {}\n".format(calcHost(mascaraBin, x)-2)) #escreve a quantidade de hosts disponiveis.

	
	arq.write("Sub-Rede Binario: {}\n".format(a)) #escreve o endereço de sub-rede em binario
	arq.write("Broadcast Binario: {}\n".format(b)) #escreve o endereço de Broadcast em binario
	arq.write( "Sub-Rede Decimal: {} \n".format( rede(enderecoRede, x) ) ) #escreve o endereço de sub-rede em decimal
	arq.write( "Broadcast Decimal: {} \n".format( rede(enderecoBroadcast, x) ) ) #escreve o endereço de Broadcast em decimal
	arq.write("-------------------------------\n") #quebra de linha
	x+=1 #contador do enquanto
print("Tudo certo!") #avisa que tudo correu certo!
arq.close() #fecha o arquivo

'''
Trabalho interdisciplinar entre as disciplinas: Redes TCP/IP e Técnicas de
Programação
Data: 26/05/2019
Número do grupo: 2
Membros do grupo:

Josué Ramos Souza
Bianca Elizandra Fonseca Neto
André Amorim Gomes
Davi Carvalho Amorim
Matheus Souza Cordeiro
André Souza de Oliveira Junior

Bibliografia consultada: N/A
'''