""""
Esses são os tipos de dados do python

1 - String (str)
2 - Inteiros (int)
3 - Decimais (float)
4 - Booleanos (bool)
5 - Lista (list)
6 - Objetos/Dicionários (dict)
7 - Vazio (none)

"""

## Representação

minha_string = "Hello"

print(type(minha_string)) # Saída <class 'str'>

meu_numero_inteiro = 333

print(type(meu_numero_inteiro)) # Saída <class 'int'>

meu_numero_decimal = 0.14

print(type(meu_numero_decimal)) # Saída <class 'float'>

meu_booleano = True

print(type(meu_booleano)) # Saída <class 'bool'>

minha_lista = [1, 2, '3']

print(type(minha_lista)) # Saída <class 'list'>

meu_objeto = { "Lista": [1, 2, 3] }

print(type(meu_objeto)) # Saída <class 'dict'>

vazio = None

print(type(vazio)) # Saída <class 'NoneType'>

def minha_funcao ():
    valor = 123
    return valor

print(minha_funcao()) # Saída 123
print(type(minha_funcao)) # Saída <class 'function'>

def funcao(a, b, c):
    if a== 1:
        return b + c
    elif a == 2:
        return b - c
    elif a == 3:
        return b * c
    else:
        return b / c

print(funcao(2, 4, 2))

#INTERPOLAÇÃO DE STRING | TAMPLATE STRING

minha_string_teste = "Olá mundo..."
adicao_string = "Tudo bem?"

string_final_interpolada = f"{minha_string_teste} {adicao_string}"

print(string_final_interpolada)

# CONCATENANDO STRING

concatenar_string1 = "treina"
concatenar_string2 = "mento"

string_concatenada = concatenar_string1+concatenar_string2

# ACESSANDO CARACTERE DA STRING

string_acesso = "Lucas Deleon"
string_acesso[0] #Saída deve ser - "L" | Acesso da primeira letra
string_acesso[-1] #Saída deve ser - "n" | Acesso da última letra
string_acesso[-2] #Saída deve ser - "o" | Acesso da penúltima letra

#FATIAMENTO DA STRING
# Também existe o slice de string no python, porém, a forma de o fazer é diferente

string_slice = "Lucas Deleon"
print(string_slice[6:len(string_slice)]) #Saída deve ser - "Deleon"

# Também funciona sem alocar o valor final, onde entende-se que o valor final seria o fim da strin
print(string_slice[6:]) #Saída deve ser - "Deleon"

# O mesmo serve para quando quero cortar do início até certo número...
print(string_slice[:5]) #Saída deve ser - "Lucas"

# Também posso fatiar a string de mais vezes, adicionando a condição final
print(string_slice[6:len(string_slice):2]) #Saída deve ser - "Dlo"

#FUNÇÕES BUILT-IN PARA MANIPULAÇÃO DE STRING

len() #Determina a largura de uma string 
string_slice.capitalize() #Altera para maiúsculo o primeiro caractere e o restante deixa em minusculo
string_slice.count() #Conta a quantidade de itens de uma string
string_slice.count('l') #Conta a qauntidade de "L" tem dentro da string
string_slice.split() #Secciona a string e a transforma em uma lista de strings
" ".join(['Olá', 'Mundo', 'Tudo', 'bem?']) #Concatena a lista de string deixando espaços no meio

#MÉTODOS DE VERIFICAÇÃO

verify_string = '!@#$%'
verify_string.isalnum() #Retorno booleano | Confere se a string é alfanumérico

verify_string2 = "Olá mundo"
verify_string2.isalpha() #Retorno booleano | Confere se a string possui apenas conteúdo alfabético

verify_string3 = "Olá mundo" 
verify_string3.islower() #Retorno booleano | Confere se a todos as letras da string estão minúsculas

verify_string4 = "Olá mundo" 
verify_string4.isupper() #Retorno booleano | Confere se a todos as letras da string estão maiúsculas

verify_string5 = "Olá mundo" 
verify_string5.startswith('Olá') #Retorno booleano | Confere se a string inicía com o valor passado por parâmetro

verify_string6 = "Olá mundo" 
verify_string6.endswith('mundo') #Retorno booleano | Confere se a string finaliza com o valor passado por parâmetro

#MÉTODOS AUXILIÁRES

string_auxiliar = "Lucas Deleon"
string_auxiliar.replace('Lucas', 'Meu nome é ') #Altera na string original o valor de "Lucas", para "Meu nome é "

string_auxiliar.lower() #Deixa todas as letras em minúsculo

string_auxiliar.upper() #Deixa todas as letras em maiúsculo

string_auxiliar.swapcase() #Inverte o case de cada letra da string (se maiúsculo, fica minúsculo e vice e versa)

string_auxiliar.title() #Converte as primeiras letras das palavras da string para maiúsculo e as demais em minúsculo

string_auxiliar.center(50, "#") #Retorna a string centralizada entre 50 "#"




