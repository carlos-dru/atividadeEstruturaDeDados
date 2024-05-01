class ElementoDaListaSimples:
    def __init__(self,dado,cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None

    def inserirNoFinal(self, nodo):
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return 
    
    def inserirPrioridade(self, nodo):
    #insira aqui seu código
        nodo_atual = self.head # Identificando o topo da lista encadeada
        if (self.head.cor == 'V'): # Se o topo é verde, insere o amarelo no topo
            nodo.proximo = self.head # Movendo o nó do topo para a segunda posição
            self.head = nodo # Incluindo o nó amarelo no topo
        elif (self.head.cor == 'A'): # Verifica se o topo é amarelo
                if (nodo.dado < self.head.dado): # Verifica se o nó atual é menor que o nó do topo
                    nodo.proximo = self.head # Movendo o nó do topo para a segunda posição
                    self.head = nodo # Incluindo o nó atual no topo
                else: # Se o nó atual é maior que o nó do topo, entra no else
                    while (nodo_atual.dado < nodo.dado) and (nodo_atual.proximo.cor != 'V') and (nodo_atual.proximo != None): # Verifica se o nó da lista é 
                        #menor que o nó atual, se o próximo nó da lista é diferente de verde, e se não é o último nó da lista
                        nodo_atual = nodo_atual.proximo # Move o ponteiro para o próximo nó da lista 
                    if (nodo_atual.proximo.cor == 'V'): # Verifica se a cor do próximo nó é verde
                        nodo.proximo = nodo_atual.proximo # Move o nó da cor verde para a próxima posição
                        nodo_atual.proximo = nodo # Insere o nó atual antes do nó verde
        return # Fim do método
    
    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
        return

#programa principal
filaPacientes = ListaEncadeadaSimples() #cria a lista que ira receber os dados dos pacientes
filaPacientes.inserir(1, "V") #insere um paciente com senha "V" 1
filaPacientes.inserir(2, "V") #insere um paciente com senha "V" 2
filaPacientes.inserir(101, "A") #insere um paciente com senha "A" 101
filaPacientes.inserir(3, "V") #insere um paciente com senha "V" 3
filaPacientes.inserir(102, "A") #insere um paciente com senha "A" 102
filaPacientes.inserir(103, "A") #insere um paciente com senha "A" 103
filaPacientes.inserir(4, "V") #insere um paciente com senha "V" 4
filaPacientes.inserir(104, "A") #insere um paciente com senha "A" 104
filaPacientes.inserir(105, "A") #insere um paciente com senha "A" 105
nodo_atual = filaPacientes.head
while nodo_atual is not None:
    print(f"Cartão: {nodo_atual.cor}, Senha: {nodo_atual.dado}")
    nodo_atual = nodo_atual.proximo 