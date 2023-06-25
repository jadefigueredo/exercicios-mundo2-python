# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input("Digite qualquer número inteiro: "))
tot = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=" ")
        tot += 1
    else: 
        print('\033[31m', end=" ")
    print('{}'.format(i), end=" ")
print('\n\033[m O número {} foi divísivel {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')