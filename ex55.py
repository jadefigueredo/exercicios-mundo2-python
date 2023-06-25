# Faça um programa que leia o peso de cinco pessoas e no final, mostre qual foi o maior e o menor peso lidos.

peso_maior = 0
peso_menor = 0

for i in range (1, 6):
    peso = float(input("Digite o peso da {}ª pessoa:".format(i)))
    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
            
print("O maior peso lido foi {}kg e o menor foi {}kg".format(peso_maior, peso_menor))
