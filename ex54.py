'''Crie um programa que leia o ano de nascimento de 7 pessoas, 
no final, mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores.'''

from datetime import date
ano_atual = date.today().year 

cont_maior_idade = 0
cont_menor_idade = 0

for pessoas in range (1, 8):
    ano_nascimento = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(pessoas)))
    calcula_idade = ano_atual - ano_nascimento
    
    if calcula_idade >= 18:
        cont_maior_idade +=1
    else:
        cont_menor_idade +=1
        
print ("{} pessoas ainda não atingiram a maioridade.".format(cont_menor_idade))
print ("{} pessoas atingiram a maioridade.".format(cont_maior_idade))
