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

# exemplo listcomp

linguagens = ["Python", "Java", "Javascript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("Depois da listcomp = ", linguagens)

#função map
#aplica a uma função em toda sequência
#map(função, sequência)

precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)