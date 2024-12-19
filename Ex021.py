#Números Pares em um Intervalo:

cont = 0
a = int(input("Primeiro num do intervalo"))
b = int(input("Segundo num do intervalo"))

for i in range(a, b+1):
    if(i % 2 == 0):
        cont+=1

print(f"Quantidade de numeros pares no intervalo: {cont}")