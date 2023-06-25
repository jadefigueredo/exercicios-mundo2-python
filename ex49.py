# Refaça o exercício desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input("Digite um número do qual você gostaria de saber a tabuada: "))

for i in range (1, 11):
    resultado = n * i
    print("{} x {} = {}".format(n, i, resultado))
    
# Outra forma de resolver / resolução do professor

num = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))