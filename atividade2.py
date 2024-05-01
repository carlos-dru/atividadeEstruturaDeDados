import random #Importando a biblioteca "random" que será usada para sortear as cartas
def embaralhaCartas(baralho): #Criando a função "embaralhaCartas" que será usada para embaralhar as cartas do baralho
    pilhaCartas = [] #Criando a pilha de cartas
    while len(baralho) > 0: #Verificando se o baralho ainda está preenchido
        cartaSelecionada = random.choice(baralho) #Selecionando uma carta aleatória do baralho
        pilhaCartas.append(cartaSelecionada) #Adicionando a carta selecionada ao topo da pilha de cartas
        baralho.remove(cartaSelecionada) #Removendo a carta selecionada do baralho para evitar duplicidade
    return pilhaCartas #Retornando a pilha de cartas após ter percorrido todo o baralho
def compraCartas(pilhaCartas): #Criando a função "compraCartas" que será usada para comprar uma carta do baralho
    cartaComprada = pilhaCartas.pop() #Removendo a carta do topo da pilha e adicionando à variável "cartaComprada"
    print(f"Comprou a carta: {cartaComprada}") #Imprimindo no terminal a carta que foi comprada
baralho = ["A-Copas","A-Paus","A-Espadas","A-Ouros","2-Copas","2-Paus","2-Espadas","2-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "3-Copas","3-Paus","3-Espadas","3-Ouros","4-Copas","4-Paus","4-Espadas","4-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "5-Copas","5-Paus","5-Espadas","5-Ouros","6-Copas","6-Paus","6-Espadas","6-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "7-Copas","7-Paus","7-Espadas","7-Ouros","8-Copas","8-Paus","8-Espadas","8-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "9-Copas","9-Paus","9-Espadas","9-Ouros","10-Copas","10-Paus","10-Espadas","10-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "J-Copas","J-Paus","J-Espadas","J-Ouros","Q-Copas","Q-Paus","Q-Espadas","Q-Ouros", #Criando a lista "baralho" com todas as cartas do baralho
           "K-Copas","K-Paus","K-Espadas","K-Ouros"] #Criando a lista "baralho" com todas as cartas do baralho
pilhaCartas = embaralhaCartas(baralho) #Invocando o método "embaralhaCartas" e armazenando a pilha de cartas na variável "pilhaCartas"
compraCartas(pilhaCartas) #Invocando o método "compraCartas", enviando a pilha de cartas como parâmetro
compraCartas(pilhaCartas) #Invocando o método "compraCartas", enviando a pilha de cartas como parâmetro
compraCartas(pilhaCartas) #Invocando o método "compraCartas", enviando a pilha de cartas como parâmetro