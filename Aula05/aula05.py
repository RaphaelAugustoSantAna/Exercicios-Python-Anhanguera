# exemplo de operação de sequência

texto = "Explorando a diversidade de linguagens de programação com Python."

print(f"{f"Tamanho do texto = {len(texto)}"}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são: {texto[:5]}")

# exemplo de lista

cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
for cor in cores:
    print(f"Posição = {cores.index(cor)}, cor = {cor}")
