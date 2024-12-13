#Faça um programa que inverta a ordem dos elementos de uma lista sem usar a função reverse

Tlista = [1, 2, 3, 4, 5]
inversa = []

k = len(Tlista) - 1

while k >= 0:
    inversa.append(Tlista[k])
    k -= 1
print("Resultado: ")
print(inversa)
