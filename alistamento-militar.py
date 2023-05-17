# 39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 

# 1) Se ele ainda vai se alistar ao serviço militar; 

#2) Se é a hora de se alistar; 

#3) Se já passou do tempo do alistamento. 

# Seu programa também deverá mostrar o campo que falta ou que passou do prazo.

from datetime import date #importa a biblioteca de datas

ano_atual = date.today().year #Armazena o ano 
ano_nascimento = int(input("Digite o ano em que você nasceu:"))
idade = ano_atual - ano_nascimento
print("Quem nasceu em {} tem {} anos em {}.".format(ano_nascimento, idade, ano_atual))


if idade == 18:
    print("É hora de se alistar ao serviço militar!")
elif idade < 18:
    falta = 18 - idade #Calcula a quantidade de tempo que falta
    print("Você ainda irá se alistar ao serviço militar. Ainda faltam {} anos para o alistamento.".format(falta))
else:
    falta = idade - 18
    print("Já passou da hora de você se alistar ao serviço militar! Você passou {} anos da idade de alistamento.".format(falta))
