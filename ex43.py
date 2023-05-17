# 43) Desenvolva uma lógica que leia o peso e a altura da pessoa. 
# Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# Abaixo de 18.5: abaixo do peso;
# entre 18.5 e 25: peso ideal 
# 25 até 30: sobrepeso 
# 30 até 40: obesidade 
# acima de 40: obesidade mórbida.

peso = (float(input("Digite seu peso atual: ")))
altura = (float(input("Digite sua altura atual: ")))
IMC = peso / (altura**2)
print("Seu IMC É igual a {:.1f}.".format(IMC)) 

if IMC < 18.5:
    print("Você está abaixo do peso ideal estabelecido pela OMS!")
elif 18.5 <= IMC < 25:
    print("Parabéns, você está em seu peso ideal, de acordo com a OMS!")
elif 25 <= IMC <= 30:
    print("Cuidado, você está na faixa de sobrepeso, de acordo com a OMS")
elif 30 <= IMC <= 40:
    print("Cuidado, você está dentro da faixa considerada obesidade, de acordo com os parâmetros da OMS!")
elif IMC > 40:
    print("Muito cuidado! Você já está dentro da faixa considerada obesidade mórbida, de acordo com os parâmetros da OMS!")
