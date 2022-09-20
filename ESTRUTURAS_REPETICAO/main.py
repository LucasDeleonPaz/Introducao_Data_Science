string = "Lucas"

for letra in string:
    print(letra)

for letra in string:
    if letra == 'L' or letra == 'l':
        print("Lucas")
    else:
        print(letra)

for i in range(10):
    print(i)

for _ in range(5):
    print(string)

contador = 0
while contador < 10:
    print(f'{string} - {contador}')
    contador += 1

for index, item in enumerate(string):
    print(item, index)

for numero in range(10):
    if numero in [5, 6, 7, 9]:
        continue
    print(numero)

numero_teste = 0
while numero_teste <= 10:
    numero_teste += 1
    if numero == 2 or numero == 7:
        continue
    print(numero)
    