#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Numero A"))
b = int(input("Numero B"))
c = int(input("Numero C"))

print(f'O maior numero eh{max(a, b, c)}\n O menor numero eh{min(a, b, c)}')