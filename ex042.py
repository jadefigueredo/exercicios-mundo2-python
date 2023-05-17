# Refaça o desafio 035 dos triângulos, acresentando o recurso de mostrar o tipo de triângulo formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: Todos os lados diferentes

# Leitura 

r1 = float(input("Primeiro Segmento: "))
r2 = float(input ("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 < r1 +r2:
    print("Os segmentos acima PODEM FORMAR triângulo", end = " ")

# Aqui dentro não temo como colocar elif, a solução é colocar um if dentro de outro if
# Formando uma condição alinhada:
    if r1 == r2 == r3:
        print("equilátero")
    elif r1 != r2 != r3 != r1:
        print("escaleno!")
    else:
        print("Isósceles")
else:
    print("Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!")