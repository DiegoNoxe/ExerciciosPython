#Crie uma função que receba dois números e retorne a soma deles. Use essa função para somar dois números fornecidos pelo usuário.

def soma(a, b):
    return a+b  

num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
print(f'A soma entre {num1} + {num2} = {num1+num2}')