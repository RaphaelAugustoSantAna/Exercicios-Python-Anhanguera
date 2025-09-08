# Vamos pensar na solução do problema apresentado no início desta aula. 
# Precisamos criar um programa que seja capaz de percorrer todos os filmes 
# (Filme 1, Filme 2, Filme 3, Filme 4 e Filme 5) e de atribuir a cada um deles uma nota de 1 a 5. 
# Repare que é importante sempre disponibilizar uma forma de a pessoa encerrar o programa, caso queira.

filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4"," Filme 5"]

#mensagem de boas vindas 
print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")

#Loop para iterar sobre cada filme na lista

for filme in filmes:
    #solicita a classificação ao usuário
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para parar): ")

    #verifica se o usuário deseja parar 
    if classificacao == '0':
        print("Que pena você não ira classificar mais os filmes.")
        break #encerra o loop principal

    #converte a classificação para um número inteiro

    classificacao = int(classificacao)

    #verifica se a classificação está dentro do intervalo válido
    if classificacao < 1 or classificacao > 5:
        print("Por favor digite uma classificação válida de 1 a 5.") 
    else:
        #exibe a classificação e passa para o proximo filme
        print(f"Você classificou'{filme}' com {classificacao} estrelas.\n")

#mensagem de agradecimento ao finalizar
print("Obrigado por classificar os filmes!")