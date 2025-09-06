# Quebrando a maldição !
print('Hello World!')

# Variáveis e tipos de dados

# O interpretador Python consegue estabelecer o tipo de dado observando seu valor. Confira alguns exemplos:

x = 10

nome = "aluno"

nota = 8.75

fez_inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))

# Melhorando o "hello world" com a função input
nome = input()
print(nome)

#formatadores de caractere
print("Olá, %s, bem vindo à disciplina de programação. Parabéns pelo seu primeiro hello world" %(nome))

#F-string
print(f"{nome}, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world")