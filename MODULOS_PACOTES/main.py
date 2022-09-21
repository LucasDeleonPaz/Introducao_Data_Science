from pacotes import soma, subtracao, divisao, multiplicacao
from IMC import calculadora_imc

#POR UMA QUESTÃO ORGANIZACIONAL, É MAIS VÁLIDO SEPARAR AS DIVERSAS PARTES
#DO NOSSO ARQUIVO EM DIVERSOS PROGRAMAS, ATÉ PARA UMA MAIOR LEGIBILIDADE POSTERIOR.
#DADO ISSO, TREINAREI A MODULARIZAÇÃO, GERAÇÃO DE PACOTES E IMPORTS NO PYTHON

#MODULOS - Arquivo que contém definições, instruções e rotinas. Pode ser importado de outro arquivo.
#Para a reutilização da lógica sem a necessidade de reescrever.

som = soma.somando(1, 3)
sub = subtracao.subtraindo(10, 23)
div = divisao.dividindo(10, 2)
mul = multiplicacao.multiplicando(4, 4)
imc = calculadora_imc(65, 1.75)
print(som, sub, div, mul, imc)

