from ast import arg
from optparse import Values


def sum_args(*args: list):
    resultado = sum(args)
    return resultado

print(sum_args(1,2,3,4,5)) #Aqui eu envio uma lista de números como parâmetro, na função o mesmo soma e retorna o valor
print( '=' * 50)


def multiplicador_soma(multiplicador: int, *args: list):
    resultado = sum(args) 
    return resultado * multiplicador

print(multiplicador_soma(2, *[1,2,3])) #Aqui eu envio uma lista de números como parâmetro e o valor de multiplicação e retorno o resultado
print( '=' * 50)

def concatenador_string(*args: list):
    resultado = " ".join(args)
    return resultado

words = [ "Andou", "na", "prancha", "cuidado", "tubarão", "vai", "te", "pegar" ]
print(concatenador_string(*words))
print( '=' * 50)

def reversao_string_concatenada (*args: list):
    resultado = " ".join(args)
    return resultado[::-1]

print(reversao_string_concatenada(*words))
print( '=' * 50)

def separando_kwargs(**args: dict):
    chave = tuple(args.keys())
    valor = tuple(args.values())
    return [chave, valor]

user = {"nome": "Naruto", "idade": 16, "comida favorita": "Ichiraku Ramen"}
print(separando_kwargs(**user))
print( '=' * 50)

def criando_dicionario(*args: list, **kwargs: dict):
    return dict(zip(list(args), list(kwargs.values())))

change_keys = ["username", "password", "address"]
new_user = {"name": "Williams", "key": "1234", 'rua': "Rua 1"}

print(criando_dicionario(*change_keys,**new_user))
print( '=' * 50)

def transformando_dict__string (**kwarg):
    values = list(kwarg.values())
    return f"{values[2]} {values[0]} por apenas R${values[1]}"

purchase = {"nome_produto": "Detergente", "preco": 6.7, "quantidade": 4}
print(transformando_dict__string(**purchase))
print( '=' * 50)

def copa_string_args(pais: str,*args: list):
    lista = sorted(args)
    resultado = pais
    for ano in lista:
        resultado += f" - {ano}"
    return resultado

pais = "Alemanha"
anos = [2014, 1990, 1974, 1954]
print(copa_string_args(pais, *anos))

