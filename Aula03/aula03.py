#exemplo com for

numeros = [1,2,3,4,5]

for num in numeros:
    print(num)


#exemplo com while

numero = int(input("Digite um número (ou 0 para sair): "))

while numero != 0:
   if numero % 2 == 0:
       print("O número é par.")
   else:
       print("O número pe ímpar.")
   numero = int(input("Digite outro numero (ou 0 para sair): "))



# Controle de repetição: range, break e continue


# * Repetição por Quantidade:

for x in range(5):
    print(x)
    
# * Limites Inicial e Superior:

for y in range(2, 7):
    print(y)
    
# * Com Incremento:

for z in range(1, 11, 2):
    print(z)