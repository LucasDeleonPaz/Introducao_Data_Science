# Primeira calculadora escrita somente com o IF, ELIF e ELSE.

tipo_operacao = input("Qual o tipo da operação? 1 - SOMA | 2 - SUBTRAÇÃO | 3- MULTIPLICAÇÃO | 4 - DIVISÃO: ")
primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")

if int(tipo_operacao) == 1:
    print(int(primeiro_numero)+int(segundo_numero))
elif tipo_operacao == 2:
    print(int(primeiro_numero)-int(segundo_numero))
elif tipo_operacao == 3:
    print(int(primeiro_numero)*int(segundo_numero))
else:
    print(int(primeiro_numero)/int(segundo_numero))

#Calculadora escrita com função

tipo_operacao1 = input("Qual o tipo da operação? 1 - SOMA | 2 - SUBTRAÇÃO | 3- MULTIPLICAÇÃO | 4 - DIVISÃO: ")
primeiro_numero1 = input("Digite o primeiro número: ")
segundo_numero1 = input("Digite o segundo número: ")

def calculadora1(a, b, c):
    if a== "1":
        return int(b) + int(c)
    if a == "2":
        return int(b) - int(c)
    if a == "3":
        return int(b) * int(c)
    if a == "4":
        return int(b) // int(c)

print(calculadora1(tipo_operacao1, primeiro_numero1, segundo_numero1))