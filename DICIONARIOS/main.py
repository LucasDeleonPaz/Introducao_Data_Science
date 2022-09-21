meu_dicionario = {
    "nome": "Lucas Deleon",
    "idade": 30,
    "sobrenome": "Paz"
}

print(meu_dicionario)
print(type(meu_dicionario))
print()

#Também posso fazer o lançamento através da função dict()

meu_dicionario1 = dict([("nome", "Lucas Deleon"), ("idade", 30), ("sobrenome", "Paz")])
print(meu_dicionario1)
print()

#Existe a função zip que também serve para criar dicionários

partial_dic_chave = ["nome", "idade", "sobrenome"]
partial_dic_value = ["Lucas Deleon", 30, "Paz"]

dicionario_zip = zip(partial_dic_chave, partial_dic_value)
print(dict(dicionario_zip))
print()

#LOOP FOR EM DICIONÁRIOS

pessoa = { 
    "nome": "Lucas Deleon",
    "idade": 30,
    "sobrenome": "Paz"
}

print()
for chave, valor in pessoa.items():
    print(chave, valor)

print()
for item in pessoa:
    print(item)

#ACESSO DOS ELEMENTOS DE UM DICIONÁRIO
print()
print(pessoa["nome"])
print()
print(pessoa.get("nome"))

#ACESSO DAS CHAVES E VALORES POR MÉTODOS
print()
pessoas_keys = list(pessoa.keys()) 
#Aqui, eu acesso as chaves do dicionário, capturo-as e transformo em uma lista

pessoas_values = list(pessoa.values())
#Aqui, eu acesso os valores do dicionário, capturo-os e transformo em uma lista

print(pessoas_keys, pessoas_values)

#ATRIBUINDO NOVAS CHAVES E VALORES AO DICIONÁRIO
print()
pessoa['Cor preferida'] = "Azul"

print(pessoa)

print()
pessoa.update({"Tipo Sanguíneo": "B-"})

print(pessoa)

#EXCLUINDO ITEM DO DICIONÁRIO
print()
del pessoa["Tipo Sanguíneo"]
print(pessoa)

#Obs: Também posso excluir itens com o POP() e o POPITEM()
#Para limpar o dicionário, posso usar o método CLEAR()