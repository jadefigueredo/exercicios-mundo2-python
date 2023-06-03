# Faça um programa que receba o número de camisetas que devemos mandar fazer para o PyLadies, e 
# imprima quanto de entrada teremos que pagar.Considere que cada camiseta custa R$25.00, e a entrada para o fabricante é de 50% do valor total.

custo_camiseta = 25

numero_de_camisetas = (int(input("Insira a quantidade de camisetas que você precisa:")))

valor_entrada = custo_camiseta + ((numero_de_camisetas)*100)/50                     

print("Você irá pagar R${:.2f}".format(valor_entrada))