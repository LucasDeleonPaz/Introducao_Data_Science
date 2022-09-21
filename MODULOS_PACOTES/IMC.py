peso = input("Qual o seu peso: ")
altura = input("Qual a sua altura: ")

def calculadora_imc(x, y):
    return int(x) / float(y)**2

print(calculadora_imc(peso, altura))