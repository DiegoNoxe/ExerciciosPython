#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

User  = int(input("Escolha um numero "))
Sort  = random.randint(0,5)
Cpu   = random.randint(0,5)

if(User == Sort and Cpu != Sort):
    print("O usuario venceu!")
else:
    if(User != Sort and Cpu == Sort):
        print("A cpu venceu")
    else:
        print("Empate")

print("---------------------------------")
print(f"Numero usuario:  {User}")
print(f"Numero maquina:  {Cpu}")
print(f"Numero sorteado: {Sort}")
print("---------------------------------")