# Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0

for i in range(1, 7):
    n = int(input("Digite {}° o valor: ".format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Você informou {} números inteiros e a coma entre eles é {}.".format(cont, soma))