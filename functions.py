def juntar(pos, tipo): #pega a posicao e o tipo
	if(tipo == 1): #se o tipo for 1 você separa por pontos
		a = "" #cria uma variavel vazia
		for i in range(4):
			if(i > 0): # se a posicao for maior que zero colorque o ponto apos o a
				a = a +"."+str(pos[i])
			else: #se nao pega a posicao e coloca em primeiro
				a = a + str(pos[i])
		return a #retorna a junção
	else:		
		a = ""
		for i in range(4):
			a = a + str(pos[i])
		return a
def junt(dado): #pega um dado
	a = dado[0:8:] #pega posicao de 0 a 8
	b = dado[8:16:] #pega posicao de 8 a 16
	c = dado[16:24:] #pega posicao de 16 a 24
	d = dado[24:32:] #pega posicao de 24 a 32
	z = str(a+"."+b+"."+c+"."+d) #junta todas as variaveis
	return z #retorna a junção

def converter(n): #pega a posicao
	binario = "" #cria uma variavel em branco
	while(True): #enquanto for verdadeiro
		binario = binario + str(n%2) #pega a veraiavel soma com ela mesmo e o resto da posicao por 2
		n = n//2 
		if n == 0: # se a posicao for igual a zero
			break; #para
	binario = binario[::-1] #transfere as posicoes de trás pra frente
	binario = int(binario) #tranforma em inteiro
	return binario #retorna a variavel

def verificacao(n): #Essa função verifica se o IP informado tem 8 bits
	generico = len(n) #verifica a quantidade de letras na posicao
	if(generico < 8): #se for manor que oito
		soma = 8 - generico #verifica o resto de oito pelo total que ja existe
		n = str("0"*soma) + n #coloca a quantidade de 0 da soma anterior
		return n
	else: #se tiver os 8 bits 
		return n #retorna a variavel

def trans(vetor1, vetor2): #transforma 
	for i in vetor1: #para o vetor informado 
		b=[] #crie uma lista
		for j in i: #para as posicoes do vetor
			vCOn = converter(int(j)) #converte a posicao
			zero = verificacao(str(vCOn)) #faz a verificação 
			b.append( zero ) #salva na lista
		vetor2.append(b) #salva a lista em outra lista

def limpar(p): #pega a posicao para limpar
	a = p.replace('\n', '') #retira a quebra de linha
	a = a.split(".") #retira as pontuacoes da posicao
	return a #retorna a variavel
	
def calcHost(vetor, posicao): #calcula hosts
	x= juntar(vetor[posicao], 0).count("0") #junta o vetor na posicao e conta a quantidade de zero
	x = 2**x #eleva por dois a quantidade de zero encontrada
	return x #retorna a variavel


def endRede(ip, mask, tipo, vetor): #verifica o endereço da redde 
	for i in range(len(ip)): #para o range da defragação do ip 
		if(tipo == 0): #se o tipo for para zerar
			if mask[i] == '0': #pegue a posicao da mascara onde for zero
				ip[i] = '0' #coloque um zero na mesma posicao do ip
		elif tipo == 1: #se o tipo for para unzar
			if mask[i] == '0': #pegue a posicao da mascara onde for zero
				ip[i] = '1' # e coloque 1 no lugar.
	x = ''.join(ip) #agura o resutado
	x = junt(x) #junta atraves da funcao junt
	vetor.append(x.split(".")) #salva no vetor informado 
	return x #retorna o resultado da variavel x

def decimal(n): #transforma em decimal
	decimal = 0 #decimal igual a zero
	n = str(n) #a transforma o valor informado em string
	n = n[::-1] #pega o valor de tras para frente
	tam = len(n) #verifica o tamanho do dos bits informados
	for i in range(tam): #para o tamanho informado
		if n[i] == "1": #if a posicao for igual a 1
			decimal = decimal + 2**i #pega a variavel do decimal repete e a elva a posicao por 2
	return decimal #retorna o resultado


def rede(vet, pos): #para o vetor e sua posicao
	b = [] #crie uma lista
	for i in vet[pos]: #navegue sobre as posicoes do vetor
		a = decimal(i) #converta para decimal
		b.append(a) #salve na lista criada
	return (juntar(b,1)) #retorne a junção do arquivo criado com pontuações