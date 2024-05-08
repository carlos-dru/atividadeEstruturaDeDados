class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if (self.dado == None):
            self.dado = dado
        else:
            if (dado < self.dado):
                if (self.esquerda):
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if(self.direita):
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)
    def folhas(self, lst):
        nodoAtual = self # Criando a variável "nodoAtual" com o valor do parâmetro "self"
        lst = list() # Criando a lista "lst" que será utilizada para armazenar as folhas
        lado = 'esquerdo' # Criando a variável "lado"
        while (nodoAtual != None): # Verificando se o nodo atual é diferente de None
            while (nodoAtual.esquerda != None) and (nodoAtual.direita != None): # Verificando se os nós à esquerda e à direita do nó atual estão preenchidos
                if (nodoAtual.esquerda != None) and (nodoAtual.esquerda.dado not in lst): #Verificando se o nó à esquerda está preenchido E não está na lista de folhas
                    nodoAtual = nodoAtual.esquerda # Movendo o ponteiro para o nó à esquerda
                    continue # Retornando para o início do bloco 'While'
                elif (nodoAtual.direita != None) and (nodoAtual.direita.dado not in lst): #Verificando se o nó à direita está preenchido E não está na lista de folhas
                    nodoAtual = nodoAtual.direita # Movendo o ponteiro para o nó à direita
                    continue # Retornando para o início do bloco 'While'
                elif (nodoAtual.esquerda.dado in lst) and (nodoAtual.direita.dado in lst) and (lado == 'esquerdo'): # Verificando se os nós à esquerda e à direita
                    # do nó atual estão na lista de folhas E o ponteiro está do lado esquerdo da árvore
                    nodoAtual = self.direita # Setando o nó atual como o nó do topo da árvore à direita
                    lado = 'direito' # Movendo o ponteiro "lado" para a direita da árvore
                    continue # Retornando para o início do bloco 'While'
                else: # Se não atende às condições acima, entra no else
                    nodoAtual = None # Atribui o valor None à variável "nodoAtual"
                    break # Sai do bloco While
            if (nodoAtual == None): # Verifica se o nó atual tem valor None
                break # Sai do bloco While
            elif (nodoAtual.dado not in lst) and (lado == 'esquerdo'): # Verifica se o nó atual não está na lista de folhas E está do lado esquerdo da árvore
                lst.append(nodoAtual.dado) # Adiciona o nó atual à lista de folhas
                nodoAtual = self # Setando o nó atual como o nó do topo da árvore
                continue # Retornando para o início do bloco 'While'
            elif (nodoAtual.dado not in lst) and (lado == 'direito'): # Verifica se o nó atual não está na lista de folhas E está do lado direito da árvore
                lst.append(nodoAtual.dado) # Adiciona o nó atual à lista de folhas
                nodoAtual = self.direita # Setando o nó atual como o nó do topo da árvore à direita
                continue # Retornando para o início do bloco 'While'
            else: # Se não atende às condições acima, entra no else
                nodoAtual = self # Setando o nó atual como o nó do topo da árvore
                continue # Retornando para o início do bloco 'While'
        return lst # Encerra o método retornando a lista de folhas da árvore
Teste = BST()
Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)
Teste.inserir(13)
print('Folhas: ', Teste.folhas([]))