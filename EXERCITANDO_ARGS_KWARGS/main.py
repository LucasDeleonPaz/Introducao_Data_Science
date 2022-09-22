from ast import arg
from optparse import Values


def sum_args(*args: list) : return sum(args)

print(sum_args(1,2,3,4,5)) #Aqui eu envio uma lista de números como parâmetro, na função o mesmo soma e retorna o valor
print( '=' * 50)


def multiplicador_soma(multiplicador: int, *args: list) : return sum(args)  * multiplicador

print(multiplicador_soma(2, *[1,2,3])) #Aqui eu envio uma lista de números como parâmetro e o valor de multiplicação e retorno o resultado
print( '=' * 50)

def concatenador_string(*args: list) : return " ".join(args)

words = [ "Andou", "na", "prancha", "cuidado", "tubarão", "vai", "te", "pegar" ]
print(concatenador_string(*words))
print( '=' * 50)

def reversao_string_concatenada (*args: list) : return " ".join(args)[::-1]

print(reversao_string_concatenada(*words))
print( '=' * 50)

def separando_kwargs(**args: dict) : return [tuple(args.keys()), tuple(args.values())]

user = {"nome": "Naruto", "idade": 16, "comida favorita": "Ichiraku Ramen"}
print(separando_kwargs(**user))
print( '=' * 50)

def criando_dicionario(*args: list, **kwargs: dict) : return dict(zip(list(args), list(kwargs.values())))

change_keys = ["username", "password", "address"]
new_user = {"name": "Williams", "key": "1234", 'rua': "Rua 1"}

print(criando_dicionario(*change_keys,**new_user))
print( '=' * 50)

def transformando_dict__string (**kwarg): return f"{list(kwarg.values())[2]} {list(kwarg.values())[0]} por apenas R${list(kwarg.values())[1]}"

purchase = {"nome_produto": "Detergente", "preco": 6.7, "quantidade": 4}
print(transformando_dict__string(**purchase))
print( '=' * 50)

def copa_string_args(pais: str,*args: list):
    for ano in sorted(args) : pais += f" - {ano}"
    return pais

pais = "Alemanha"
anos = [2014, 1990, 1974, 1954]
print(copa_string_args(pais, *anos))

