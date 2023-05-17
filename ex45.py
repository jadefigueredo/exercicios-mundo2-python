# 45) Crie um programa que faça o computador jogar Jonkepô com você.

from random import randint # Importando biblioteca random
from time import sleep #Importando biblioteca time para fazer o computador escrever Jô Ken Pô com intervalos de 1 segundo.

itens = ("Pedra", "Papel", "Tesoura") #Armazenando itens em uma array
computador = randint(0,2) # Fazendo o computador escolher entre itens de dentro da array

print("="*15)
print("E aí, Vamos jogar Pedra, papel e tesoura?")
print("="*15)
print("JÔ")
sleep(1)
print ("KEN")
sleep(1)
print("PÔ!!!")
print("="*15)
print('''
Esolha uma das opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print("="*15)

jogador = int(input("Qual é a sua jogada?".format(itens[computador])))
print("O computador escolheu {}.".format(itens[computador])) # Adiciono a posição dentro da variável itens para que apareça a opção com o nome e não a posição em que ocupa dentro da array
print("Jogador jogou {}.".format(itens[jogador]))

if computador == 0: # Computador joga pedra
    if jogador == 0: #testa todas as possibilidades de inputs dentro do if
        print ("Vocês empataram!")
    elif jogador == 1:
        print ("Jogador venceu!")
    elif jogador == 2:
        print ("Computador venceu!")
    else:
        print("Jogada inválida!")

elif computador == 1: # Computador joga papel
    if jogador == 0:
        print ("Computador vence!")
    elif jogador == 1:
        print ("Empataram!")
    elif jogador == 2:
        print ("Jogador vence!")
    else:
        print("Jogada inválida!")

elif computador == 2: # Computador joga tesoura
    if jogador == 0:
        print ("O jogador vence!")
    elif jogador == 1:
        print ("Compuatdor vence!")
    elif jogador == 2:
        print ("Vocês empataram!")
    else:
        print("Jogada inválida!")