# Função len()

# Calcular o comprimento de uma lista e, em seguida, imprime o resultado com comentários explicativos:

# Cria uma lista de números
numeros = [1, 2, 3, 4, 5]
# Usa a função len() para calcular o comprimento da lista
comprimento = len(numeros)
# imprime o comprimento da lista
print("O comprimento da lista é:", comprimento)


# função de soma
def soma(a, b):
    resultado = a + b
    return resultado


resultado_soma = soma(5, 3)
print("O resultado da soma é: ", resultado_soma)

# função é par


def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 6
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} não é um número par.")