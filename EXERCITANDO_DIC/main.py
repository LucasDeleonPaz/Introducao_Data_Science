dicionario = {
    "nome" : "Lucas Deleon",
    "cidade": "Contagem",
    "estado": "Minas Gerais"
}

print(type(dicionario))
print()

print(dicionario["nome"])
print()

print(dicionario["cidade"])
print()

print(dicionario["estado"])
print()

print(dicionario.get("telefone", "Telefone não existe"))
print()

print(dicionario.keys())
print()

print(dicionario.values())
print()

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["31 9 9999-9999", False, 30]
concat_listas = zip(lista_1, lista_2)
print(dict(concat_listas))
print()

dicionario_2 = dict(zip(lista_1, lista_2))
keys_dic_2 = list(dicionario_2.keys())
values_dic_2 = list(dicionario_2.values())

for chave, value in dicionario_2.items():
    dicionario[chave] = value

print(dicionario)

del dicionario['casado']
print(dicionario)
