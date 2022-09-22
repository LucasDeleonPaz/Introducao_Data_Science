from pacotes.mutabilidade import imutabilidade, mutabilidade
import copy

#No exemplo abaixo, podemos perceber a imutabilidade da string, onde passamos para a função o valor de linguagem
#Alteramos na função o valor da mesma, porém, no terceiro retorno, a mesma volta para o valor inicial.
#Primeiro retorno = Valor inicial, Segundo retorno = Valor da função, Teceiro retorno = Valor inicial. 

def main_imutabilidade ():
    linguagem = "A linguagem é Python"
    print(linguagem)
    imutabilidade(linguagem)
    print(linguagem)

main_imutabilidade()

#Já no exemplo abaixo, podemos perceber a mutabilidade da lista, onde passamos para função a lista com 3 valores,
#na função adicionamos um novo elemento à lista. O que faz com que a lista passe a conter um novo valor.
#Primeiro retorno = Valor inicial, Segunto retorno = Valor alterado, Terceiro retorno = Valor alterado.

def main_mutabilidade ():
    lista = [ "Python", "JavaScript", "R"]
    print(lista)
    mutabilidade(lista)
    print(lista)

main_mutabilidade()

#String, Inteiros, Decimais, Tuplas e Booleanos são imutáveis em Python!
#Listas, Dicionários, Sets (conjuntos) são mutáveis. 
#Porém, Tuplas aceitam itens mutáveis em sí, como listas. Por isso, os itens mutáveis dentro de um item imutável, são mutáveis.

#SOBRE CÓPIAS RASAS E PROFUNDAS

lista = [1, 2, 3, ["a", "b", "c"], 4, 5, 6]
lista_copy = lista.copy()

lista_copy[3][0] = "A"
lista_copy[0] = 0

print(lista)
print(lista_copy)
print()

#Nos prints acima, posso ver que os valores da lista interna alteraram tanto na lista "lista_copy" quanto na "lista"
#Isso acontece por causa da memória, onde a alteração acontece por conta da memória lançada e as localidade iguais.
#Para resolução disso, se faz necessário usar a cópia profunda, como pode ser visto abaixo

lista_deep_copy = copy.deepcopy(lista)
lista_deep_copy[0] = "Olá"
lista_deep_copy[3][1] = "Olá"

print(lista)
print(lista_deep_copy)
print(lista is lista_deep_copy)
