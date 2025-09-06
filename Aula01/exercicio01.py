#utilizando Python para automatizar média dos alunos

Nota_1 = int(input("Digite a nota 1: "))
Nota_2 = int(input("Digite a nota 2: "))
Nota_3 = int(input("Digite a nota 3: "))
Nota_4 = int(input("Digite a nota 4: "))

#observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String

#calculando media

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

#condição para a aprovação do aluno.

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#dadas as notas, mostramos a média final e a situação do aluno.

print(f"Média: {media}")
print(f"Situação: {situacao}")
