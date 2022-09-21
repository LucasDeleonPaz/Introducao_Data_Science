#CRIANDO LISTA DE 6 A 20 
lista = list(range(6,21))
print(lista)

#IMPRIMINDO SOMENTE O ÚLTIMO ITEM DA LISTA
print(lista[len(lista)-1])

#ALTERANDO O VALOR DO ITEM NO ÍNDICE 1 DA LISTA
lista[1] = 'Lucas'
print(lista)

#IMPRIMINDO SOMENTE OS ITENS DA POSIÇÃO 2, 3 E 4 DA LISTA
print(lista[2:5])

#ADICIONANDO UM ITEM NA LISTA
lista.append("Deleon")
print(lista)

#CRIANDO LISTA DE 20 A 6
lista_2 = list(range(20, 5, -1))
print(lista_2)

#IMPRIMINDO O TAMANHO DAS LISTAS
print(len(lista), len(lista_2))

#LIMPANDO AMBAS AS LISTAS
lista.clear()
lista_2.clear()
print(lista, lista_2)