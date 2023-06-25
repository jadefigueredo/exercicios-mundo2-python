# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. 
# Desconsidere os espaços.

frase = str(input("Digite qualquer frase: ")).strip().upper() # Recebe a frase do usuário
palavras = frase.split() # separa e gera uma lista
junto = ''.join(palavras) # junto tudo e elimina os espaços tornando uma string só
'''inverso = ' '

for letra in range(len(junto) - 1, -1, -1): # vai da última letra até a primeira
    inverso += junto[letra]
print ("O inverso de {} é {}".format(junto, inverso ))

if inverso == junto:
        print("Temos um palíndromo!")
else:
        print("Não temos um palíndromo!")'''

# outra forma de fazer

inverso = junto[::-1]

print ("O inverso de {} é {}".format(junto, inverso ))

if inverso == junto:
        print("Temos um palíndromo!")
else:
        print("Não temos um palíndromo!")




