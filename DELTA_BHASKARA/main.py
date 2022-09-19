import math


def delta_funcao (a, b, c):
    x = (b**2) - (4 *a *c)
    return x


def bhaskara(a, b, c):
    delta = delta_funcao(a, b, c)

    if delta < 0:
        return "Delta negativo"
    
    raiz = round(math.sqrt(delta), 2)
    
    x_1 = round(((-b + raiz)/(2*a)), 2)
    x_2 = round(((-b - raiz)/(2*a)), 2)
    
    return f"x' = {x_1}, x'' = {x_2} "

print(bhaskara(1, 5, 2))
print(bhaskara(3, 10, 2))