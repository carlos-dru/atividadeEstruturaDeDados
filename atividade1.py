def mergeSort(dados): #definindo a função "mergeSort"
 if len(dados) > 1: #verificando se o vetor "dados" possui mais de um elemento
    meio = len(dados)//2 #encontrando a posição central do vetor "dados" pegando a parte inteira da divisão por 2
    esquerda = dados[:meio] #armazenando os elementos que estão à esquerda do meio do vetor na variável "esquerda"
    direita = dados[meio:] #armazenando os elementos que estão à direita do meio do vetor na variável "direita"
    mergeSort(esquerda) #invocando a funcao "mergeSort" recursivamente para o subvetor "esquerda"
    mergeSort(direita) #invocando a funcao "mergeSort" recursivamente para o subvetor "direita"
    i = j = k = 0 #definindo as variáveis "i", "j" e "k" com o valor 0
    while i<len(esquerda) and j<len(direita): #verificando se as variáveis "i" e "j" são menores que os tamanhos dos 
                                              #vetores "esquerda" e "direita", respectivamente. Enquanto forem menores, entra no loop
        if esquerda[i]>direita[j]: #verificando se o elemento do subvetor à esquerda na posição "i" 
                                   #é maior que o da direita na posição "j"
            dados[k]=esquerda[i] #atribuindo o valor do elemento à esquerda para a posição "k" do vetor "dados"
            i=i+1 #incrementando a variável "i" em 1 unidade
        else: #tratando caso o elemento do subvetor à esquerda seja menor que o da direita
            dados[k]=direita[j] #atribuindo o valor do elemento à direita para a posição "k" do vetor "dados"
            j=j+1 #incrementando a variável "j" em 1 unidade
        k=k+1 #incrementando a variável "k" em 1 unidade
    while i<len(esquerda): #verificando se a variável "i" é menor que o tamanho do vetor "esquerda". Enquanto for menor, entra no loop
        dados[k]=esquerda[i] #atribuindo à posição "k" do vetor "dados" o elemento da posição "i" do vetor "esquerda"
        i=i+1 #incrementando a variável "i" em 1 unidade
        k=k+1 #incrementando a variável "k" em 1 unidade
    while j<len(direita): #verificando se a variável "j" é menor que o tamanho do vetor "direita". Enquanto for menor, entra no loop
        dados[k]=direita[j] #atribuindo à posição "k" do vetor "dados" o elemento da posição "j" do vetor "direita"
        j=j+1 #incrementando a variável "j" em 1 unidade
        k=k+1 #incrementando a variável "k" em 1 unidade
dados = [54, 26, 93, 17, 77, 31, 44, 55] #atribui à variável "dados" o vetor de entrada da função
mergeSort(dados) #invoca a função "mergeSort", enviando o vetor "dados" como parâmetro
print(f"Saída: {dados}") #imprimindo o vetor "dados" na saída do terminal ordenado de forma decrescente