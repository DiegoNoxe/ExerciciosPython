#Faça um programa que calcula a média de uma lista.

#Metodo 1

L = [5,5,5,2,3,9,10,1]
media = 0
final = len(L)

for i in range(0, final):
        media+=L[i]

print(f'A media final eh {media/final}!')


#Metodo 2

media = sum(L)/len(L)
print(f'A media final eh {media}!')