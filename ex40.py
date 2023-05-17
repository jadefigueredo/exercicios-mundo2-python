# 40 Crie um programa que leia duas notas de uma aluno e calcule sua média. 
# Mostrando uma mensagem no final, de acordo com a média atingida: 
# "Média abaixo de 5. REPROVADO", "média entre 5 e 6.9: RECUPERAÇÃO", "média 7 ou superior: APROVADO"

import math

nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota:"))
media_aluno = (nota1 + nota2) / 2


if 7 > media_aluno >= 5 :
    print("Você está na recuperação! Sua média é {}.".format(media_aluno))
elif media_aluno < 5:
    print ("você está reprovada(o)! Sua média é {}.".format(media_aluno))
elif media_aluno >=7:
    print("Parabéns, você está aprovada(o)! Sua média é {}.".format(media_aluno))


