soma_idade = 0
media_idade = 0
homem_mais_velho = 0
nome_mais_velho = 0
totmulher20 = 0

for info in range(1, 5):
    print(" ----------------- {}ª PESSOA -----------------".format(info))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]")).strip()
    
    soma_idade += idade
    
    if info == 1 and sexo in "Mm":
        homem_mais_velho = idade
        nome_mais_velho = nome
    elif sexo in "Mm" and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_mais_velho = nome
    elif sexo in "Ff" and idade < 20:
        totmulher20 += 1
        
media_idade = soma_idade / 4

print(" A média de idade do grupo é e {} anos".format(media_idade))
print("O homem mais velho tem {} anos e se chama {}".format(homem_mais_velho, nome_mais_velho))  
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))