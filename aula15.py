def divide(x, y):
    assert y != 0, "Divisão por zero!"
    return x / y


result = divide(6, 0)
print(result)

# O assert nos mostra o erro e ajuda a detectar o que pode ser uma avaria no código


def calcular_media(notas):
    assert len(notas) > 0, "A lista de notas não pode ser vazia"

    soma = sum(notas)
    media = soma / len(notas)
    return media


# Exemplo 1: Lista de notas vazias
notas_vazias = []
media = calcular_media(notas_vazias)  # Isso lançará um Assertion Error
# Exemplo 2: Lista de notas válida
notas_validas = [8, 7, 9, 6, 8]
media = calcular_media(notas_validas)  # Isso funcionará corretamente
print(media)

###########################################################3

import doctest


def square(x):
    """
    Retorna o quadrado de um número

    Exemplos:
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x
    doctest.testmod()


# O doctest permite escrever exemplos de uso dentro da docstring do código (usando >>>).
# Quando você roda doctest.testmod(), ele:
# Executa os exemplos da documentação como testes.
# Compara a saída obtida com a saída esperada.
# Se tudo bater, não mostra nada.
# Se houver erro, mostra onde a saída foi diferente
