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
