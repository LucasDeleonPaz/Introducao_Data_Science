# FUNÇÕES PARA CONVERSÃO DE DADOS

x = bool(0)
print(x) #Resultado será False

y = str(400)
print(y) #Resultado será '400'

z = float(7)
print(z) #Resultado será 7.0

w = int("14")
print(w) #Resultado será 14

#FUNÇÕES PARA PROCESSAMENTO DE DADOS

a = [1, 2, 3, 4, 5]
print(sum(a)) #Retornará a soma de todos os elementos da tupla - 15

b = [True, False, True, True]
print(all(b)) #Verifica se todos os elementos da tupla são verdadeiros - Retorno False

c = [True, False, True, True]
print(any(c)) #Verifica se algum elemento da tupla é verdadeiro - Retorno True

d = [11, 14, 22, 2, 16, 64]
print(min(d)) #Verifica e retorna o elemento de menor valor da tupla - 2

e = [11, 14, 22, 2, 16, 64]
print(max(d)) #Verifica e retorna o elemento de maior valor da tupla - 64

f = ["Lucas", "Carlos", "João"]
f_1 = [30, 29, 32]

f_2 = zip(f, f_1) #Parea os elementos e gera um objeto composto zipado

print(list(f_2)) #Imprime uma lista pareada das tuplas f e f_1 [("Lucas", 30), ("Carlos", 29), ("João", 32)]

g = ["a", "b", "a", "b", "c"]
print(len(g)) #Retorna a largura da tupla - 5

