#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;



A = int(input("Digite o Lado A"))
B = int(input("Digite o Lado B"))
C = int(input("Digite o Lado C"))

if(A != B and A != C and C != B):
    print("O triangulo eh Escaleno")
else:
    if(A == B and B == C):
        print("O tringulo eh um Equilatero")
    else:
        print("O tringulo eh um Isoceles")
