def tabuada (x : int):
    resultado = [n for n in range(1,(x * 10 + 1)) if n % x == 0]
    return resultado

tabuada_5 = tabuada(5)
a, b, c, *d = tabuada_5
print(a, b, c, d)

*primeiros, penultimo, ultimo = tabuada_5
print(primeiros, penultimo, ultimo)

#UTILIZANDO ARGS - EMPACOTADOR E DESEMPACOTADOR DE LISTAS E TUPLAS.
def usando_args (*args):
    return f'o tipo do parâmetro é {type(args)}, e o argumento gerou: {args}'

print(usando_args(10, "String", True, [1, 2, 3, 4]))

lista_frutas = ["Banana", "Maçã", "Uva", "Pêra"]
update_lista_frutas = [*lista_frutas, "Limão", "Laranja"] #Aqui, é como se fizéssemos um "spread" de uma lista em outra lista e adicionasse.

print(lista_frutas, update_lista_frutas)

def print_fruta (*lista_fruta):
    for fruta in lista_fruta:
        print(f"Essa é a fruta da vez {fruta}")
print(print_fruta(*lista_frutas, *update_lista_frutas))

#UTILIZANDO O KWARGS - EMPACOTADOR E DESEMPACOTADOR DE DICIONÁRIOS
def usando_kwargs(**kwargs):
    return f'O tipo do parâmetro é {type(kwargs)}, e o argumento gerou: {kwargs}'

print(usando_kwargs(nome="José da Silva", idade= "35")) #Crio um dicionário passando por parâmetro as chaves e valores relativos ao mesmo.

pessoas = {"Nome": "Lucas Deleon", "Email" : "deleon_lucas@hotmail.com"}
update_pessoas = {**pessoas, 'Idade': 30} #Adiciono mais uma chave e valor ao dicionário
print(update_pessoas)

outras_informacoes = { "Profissão": "Programador" }

pessoa_completa = {**update_pessoas, **outras_informacoes}

print(pessoa_completa)