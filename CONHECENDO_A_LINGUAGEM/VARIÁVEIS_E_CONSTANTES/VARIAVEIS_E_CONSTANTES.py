age = 30
name = "Lucas"
end = "Rua Antônio Olinto Ferreira"
num = 334
city = "Contagem"
state = "Minas Gerais"

print(f'Olá {name}, você ainda mora na {end}, {num} - {city}/{state}?')

##Para se usar o tamplate string (variáveis com o texto), precisamos usar
## da seguinte maneira " f'' " - f | trás as sitações das variáveis,
## '' | Trás o contexto que será alocado as variáveis.

age, name, end, num, city, state = (30, 'Deleon', 'Rua 2', 334, 'BH', 'MG')
## Acima, vemos um outro formato para se declarar uma variável
print(f'Olá {name}, você ainda mora na {end}, {num} - {city}/{state}?')

##OBS: Python não tem CONSTANTE! Não existe uma palavra reservada para tal declaração
##Porém, existe maneiras de instar que uma declaração é uma constante, sendo isso uma 
## CONVENSÃO.

STATES = ['SP', 'RJ', 'MG'] ##Declarar com LETRA MAIÚSCULA, é a forma tida por convensão
##Que o item declarado é uma constante.

#Boas Práticas 
##O padrão de nomes deve seguir o padrão snake case. | name_user, age_user, end_user
##Sempre escolher nomes sugestivos para declarar uma variável ou uma constante
##Nomes de CONSTANTES sempre em maiúsculo.

STATES.append('SC')