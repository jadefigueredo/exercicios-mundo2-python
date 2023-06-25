# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Algumas coisas que são necessárias saber antes de resolver isso:
# 1. Progressão aritmética é só uma sequência númerica
# 2. A razão é o intervalo entre elas

primeiro_termo = int(input("Primeiro termo: "))
razão = int(input("razão: "))
decimo_termo = primeiro_termo +(10-1)*razão # tem que calcular o décimo termo, de acordo com a fórmula matematica é isso aqui

for i in range(primeiro_termo, decimo_termo, razão):
    print("{}".format(i), end=" -> ")
print("Acaba aqui!")

