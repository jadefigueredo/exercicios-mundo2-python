# 41 A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade: 
# "Até 9 anos: MIRIM", "Até 14 anos: Infantil", 
# "Até 19 anos: Junior", "Até 25 anos: senior", "acima: master"

from datetime import date

ano_nascimento = int(input("Digite o ano em que você nasceu:"))
ano_atual = date.today().year 
idade = ano_atual - ano_nascimento

if idade <= 9:
    print ("Você está na categoria MIRIM!")
elif idade <= 14:
    print ("você está na categoria INFANTIL!")
elif idade <= 19:
    print("Você está na categoria JÚNIOR!")
elif idade <= 25:
    print("você está na categoria senior!")
else:
    print("Você está na categoria master!")
