conjunto = { 1, 2, 3, 4, 5, 6 }
print(type(conjunto))
print()

conjunto_1 = set([1, 2, 3, 4, 5, 6, 7])
print(type(conjunto_1))
print()

conjunto_2 = set(range(0, 20, 2))
print(conjunto_2)

#ADICIONANDO ELEMENTOS A UM CONJUNTO
conj = set()
conj.add(2)
conj.add("Python")
conj.add((1, 2, 3))
print(conj)
print()

conj.update([1, 2, 3])
print(conj)

#Para remoção, temos os métodos "remove" e o "discard", onde o "DISCARD" não retorna
#um erro e ou exceção caso não haja o elemento no conjunto.
#Já o "REMOVE" informa que não existe tal elemento

conj.remove(1)
print(conj)
print()

conj.discard('Hello')
print(conj)

#Para a remoção de todos os itens do conjunto, o método "CLEAR()" também funciona e retorna
# o objeto vazio

#OPERAÇÕES COM CONJUNTOS - UNIÃO

conjunto_00 = { 1, 2, 3, 4, 5}
conjunto_01 = { 1, 3, 4, 7, 9, 10}

uniao_conjunto = conjunto_00 | conjunto_01
print(uniao_conjunto)

uniao_conjunto = conjunto_00.union(conjunto_01)
print(uniao_conjunto)
print()

#OPERAÇÃO COM CONJUNTOS - INTERSECÇÃO
interserc_conj = conjunto_00 & conjunto_01
print(interserc_conj)
print()

interserc_conj = conjunto_00.intersection(conjunto_01)
print(interserc_conj)
print()

#OPERAÇÃO COM CONJUNTOS - DIFERENÇA
diferenca_conj = conjunto_00 - conjunto_01
print(diferenca_conj)
print()

diferenca_conj = conjunto_00.difference(conjunto_01)
print(diferenca_conj)
print()

#OPERAÇÃO COM CONJUNTOS - DIFERENÇA SIMÉTRICA
simetrica = conjunto_00 ^ conjunto_01
print(simetrica)
print()

simetrica = conjunto_00.symmetric_difference(conjunto_01)
print(simetrica)
print()

#OPERAÇÃO COM CONJUNTOS - CONTÉM OU NÃO CONTÉM | SUBSET
conjunto_02 = { 1, 2}
subset = conjunto_00 in conjunto_01
print(subset)
print()

subset = 1 in conjunto_00
print(subset)
print()

subset = conjunto_02.issubset(conjunto_00)
print(subset)
print()