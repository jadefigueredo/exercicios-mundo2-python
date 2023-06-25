# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # Conceito de acumulador - O acumulador soma ou multiplica os valores.
cont = 0 # O contador vai sontando mais um, sem somar.

for i in range (1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i # ou "Soma += 1" da no mesmo!
print ("A soma de todos os {} valores solicitados é {}".format(cont, soma))