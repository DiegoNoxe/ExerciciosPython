#Escreva um programa que gere um número aleatório entre 0 e 5, e permita que o usuário tente adivinhar o número, dando dicas se o número é maior ou menor a cada tentativa.

import random 
NumAleatorio = random.randint(0, 5)

i = 1
while True:
    NumMaquina   = random.randint(0, 5)
    NumUser = int(input("Digite um numero de 0 a 5\n"))

    if(NumMaquina == NumAleatorio and NumUser != NumAleatorio):
        print(f"A maquina venceu! O número era {NumAleatorio}\n")
        break  
    elif(NumUser == NumAleatorio and NumMaquina != NumAleatorio):
        print(f"O jogador venceu! O número era {NumAleatorio}\n")
        break     
    elif(NumMaquina != NumAleatorio and NumUser != NumAleatorio):
        print(f"Ambos erraram!\n")
    else:
        print("Ambos acertaram!\n")
        break     