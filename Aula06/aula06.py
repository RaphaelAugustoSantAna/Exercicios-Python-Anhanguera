# add(), e remove()

# criando um conjunto vazio
meu_conjunto = set()

# adicionando elementos ao conjunto

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
# imprimindo o conjunto
print("Conjunto após adicionar elementos:", meu_conjunto)
# verificando se um elemento está no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto")
else:
    print(f"{elemento} não está no conjunto")
# removendo um elemento do conjunto
meu_conjunto.remove(20)
# imprmindo o conteudo atualizado
print("conjunto após remover o elemento 20:", meu_conjunto)

# Exemplo 1 - Criação de um dicionário vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1["nome"] = "Maria"
dici_1["idade"] = 25
# Exemplo 2 - Criação de um dicionário com pares chave: valor
dici_2 = {"nome": "Maria", "idade": 25}
# Exemplo 3 - Criação de um dicionário com uma lista de tuplas representando pares chave: valor
dici_3 = dict([("nome", "Maria"), ("idade", 25)])
# Exemplo 4 - Criação de um dicionário usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores.
dici_4 = dict(zip(["nome", "idade"], ["Maria", 25]))
# Teste se todas as construções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4)  # Deve imprimir True
print(dici_1)

# Exemplo com NumPy
# Importe a biblioteca NumPy
import numpy as np

# Crie um array NumPy de números inteiros
my_array = np.array([1, 2, 3, 4, 5])
# Imprima o array
print("Array original:")
print(my_array)
# Realize operações matemáticas com array
squared_array = my_array**2  # Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array)  # Calcula a soma de todos os elementos
# Imprima os resultados
print("\nArray ao quadrado:")
print(squared_array)
print("\nSoma dos elementos:")
print(sum_of_elements)
# Acesse elementos do array
element_at_index_2 = my_array[2]  # Acessa o elemento no índice 2
print("\nElemento no índice 2:", element_at_index_2)
