import string


def imutabilidade (linguagem: str):
    linguagem = "A linguagem é JavaScript"
    print(linguagem)

def mutabilidade (lista: list):
    lista.append('Java')
    print(lista)
