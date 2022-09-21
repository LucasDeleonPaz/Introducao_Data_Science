minhas_lista = list("abc") # Retorna uma nova lista, iterando a string passada por parâmetro ["a", "b", "c"]

#Caso tente fazer o mesmo com números, retornará erro, pois, números não são iteráveis.

#LISTA COM RANGE
minha_lista2 = list(range(6)) # Retornará uma lista [0, 1, 2, 3, 4, 5]

#O Range possúi 3 condições propostas, sendo elas:
# - Intervalo inicial
# - Intervalo final
# - Passo

minha_lista3 = list(range(10, 20, 2)) # Retornará uma lista [10, 12, 14, 16, 18]

#LOOP FOR EM LISTAS

carrinho_compras = ["Biscoito", "Arroz", "Leite", "Pão", "Feijão"]

for item in carrinho_compras:
    print(item)

#Retornará o print de todos os itens da lista separadamente.

#ALTERANDO ITENS DA LISTA

carrinho_compras[4] = "Açucar"
#Trocará o valor de "Feijão" para "Açucar"

#FATIAMENTO DE LISTAS
print(carrinho_compras[0:3])
#Retornará somente os itens do índice de 0 a 3.

#MÉTODOS DE LISTA
len(carrinho_compras)
carrinho_compras.append("Feijão", "Mostarda")
carrinho_compras.clear() # Excluirá todos os itens da lista
sorted(carrinho_compras) # Sequênciará, por ordem alfabética (mas também serve para númericos) a miinha lista
carrinho_compras.sort() # Retorna NONE, porém, organiza a lista de forma sequênciar por ordem alfabética

#Também podemos orientar o sort
carrinho_compras.sort(key=len) #Orientará minha lista por ordem de tamanho da string
carrinho_compras.sort(reverse=True) #Organiza e reverte o resultado
carrinho_compras.count("Feijão") # Conta quantas vezes aparece a palavra "Feijão" na minha lista
carrinho_compras.extend("Bolo") # Mesmo que append. Adiciona na lista.
carrinho_compras.index("Açucar") # Retorna o índice da palavra passada por parâmetro
carrinho_compras.pop() # Sem parâmetro, retira o último item da lista
carrinho_compras.pop(3) # Retira o item no índice 3 da lista
carrinho_compras.remove('Bolo') # Retira da lista o item passado por parâmetro



