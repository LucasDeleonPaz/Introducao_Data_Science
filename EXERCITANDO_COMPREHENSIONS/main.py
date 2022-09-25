lista = [numero for numero in range(11)]
print(lista)
print("=" * 50)

lista = [numero for numero in range(22) if numero % 2 == 0 or numero % 3 == 0]
print(lista)
print("=" * 50)

lista = [numero for numero in range(-5,31) if numero % 2 != 0 and numero % 5 != 0]
print(lista)
print("=" * 50)

def exercicio_4 ():
    lista = [numero**2 for numero in range(11)]
    print(lista)
    return lista
exercicio_4()
print("=" * 50)

texto = "O Rato Rui Gosta De QueiJo FresQuiNhoZz"
def exercicio_5(sentenca: str):
    lista = [letra for letra in sentenca if ord(letra) >= 65 and ord(letra) <=90 ]
    print(lista)
    return lista
exercicio_5(texto)
print("=" * 50)

texto = "o rato rui roeu a roupa do rei de roma"
def exercicio_6(texto: str):
    lista = [palavra for palavra in texto.split(' ') if palavra.startswith('r') and len(palavra) >= 4]
    print(lista)
    return lista
    
exercicio_6(texto)
