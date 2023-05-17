# 44) Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal 
# condição de pagamento: à vista dinheiro ou 
# cheque: 10% de desconto
# a vista no cartão: 5% de desconto, 
# em até 2x no cartão: preço normal, 
# 3x ou mais no cartão: 20% de juros

preco = float(input("Preço das compras: R$ "))
print ('''Formas de pagamento
[ 1 ] à vista em dinheiro ou cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual a opção que você escolhe?"))

if opcao == 1: #Calcula à vista dinheiro ou cheque
    total = preco - (preco * 10/100) 

elif opcao == 2:  #calcula à vista no cartão
    total = preco - (preco * 5/100)
    print("Sua compra de R$ {:.2f} vai custar R$ {} no final.".format(preco, total))

elif opcao == 3:
    total = preco
    parcela = total/2
    print("Você irá pagar o valor de {} em duas parcelas de {}.".format(total, parcela))

elif opcao == 4:
    total = preco + (preco * 20/100) # Calcula a porcentagem de juros
    total_parcelas = int(input("Quantas parcelas?")) 
    parcela = total / total_parcelas
    print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS".format(total_parcelas, parcela))

else: # caso o usuário digite a opção errada, cria um else para registrar o erro
    total = 0
    print("Opção inválida de pagamento. Tente novamente!")
print("Sua compra de R$ {:.2f} vai custar R${:.2f} no final." .format(preco, total))
