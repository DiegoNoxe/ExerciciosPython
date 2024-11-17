#Crie um programa que exibe todos os números pares de n a x. Ambos colocados pelo o usuario.

N  = int(input("Primeiro numero: "))
X  = int(input("Segundo numero: "))

for i in range(N,X+1):
    if(i % 2 == 0):
        print(i, end=' ')