#LIST COMPREHENSION

#Range comum
lista = [x for x in range(11)]
print(lista)
print()

#Range com ações
lista = [x * 2 for x in range(1,11)]
print(lista)
print()

#Range com condicionais - IF
lista = [x for x in range(61) if x % 6 == 0]
print(lista)
print()

#Range com condicionais - IF e ELSE
lista = [x if x % 5 == 0 else f"{x} não múltiplo de 5" for x in [1,3,4,12,15,30,32]]
print(lista)
print()

#DICT COMPREHENSION

#Dicionário com comprehension comum
lista = ["Brasil", "Argentina", "Japão"]
dicionario = {index: pais for index, pais in enumerate(lista)}
print(dicionario)
print()

#Dicionário com comprehension com condicionais
pessoas = {"Maria": 25, "Mara": 32, "Leila": 23, "Augusto": 34}
dicionario_idade_par = {key: value for (key, value) in pessoas.items() if value % 2 == 0}
print(dicionario_idade_par)
print()

dicionario_idade_par = {key: value for (key, value) in pessoas.items() if value < 30}
print(dicionario_idade_par)
print()

#SET COMPREHENSIONS

#Set com comprehension comum
palavras = ["Gira", "Mundo", "Gira", "Gira", "Mundo", "Águas", "Claras"]
conjunto = {palavra for palavra in palavras}
print(conjunto)
print()

#Set com condicionais em comprehension
conjunto = {palavra for palavra in palavras if palavra != "Mundo"}
print(conjunto)
print()
