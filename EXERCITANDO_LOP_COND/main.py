def verifica_parentesis(str: str):
    abertura = str.count('(')
    fechamento = str.count(')')
    if abertura == fechamento:
        return ''
    elif abertura > fechamento:
        return (abertura - fechamento)*'('
    else:
        return (fechamento - abertura)*')'

print(verifica_parentesis("))(("))

def verifica_repeticao(text: str):
    result = []

    for index, word in enumerate(text):
        if text[index - 1].lower() != word.lower() or text[index - 2].lower() != word.lower():
            result.append(word)

    return "".join(result)

print(verifica_repeticao('Oooiiiiieeeeeee Luuuuuccaaaaasssss'))