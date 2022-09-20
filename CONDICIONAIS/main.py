entrada_nota = input("Digite sua nota: ")
nota = float(entrada_nota)

def verifica_nota (x):
    if nota >= 4 and nota <= 6:
        print(f'Sua nota foi {nota}, por isso, está de recuperação')
    elif nota < 4:
        print(f'Sua nota foi {nota}, por isso, está reprovado')
    elif nota > 6 and nota <= 8:
        print(f'Você passou, mas tome cuidado... Tente melhorar! Sua nota {nota}')
    else:
        print(f'Você foi aprovado com sucesso, sua nota foi {nota}')

print(verifica_nota(nota))
