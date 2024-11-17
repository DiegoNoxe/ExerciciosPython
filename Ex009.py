#Solicite uma palavra ou frase ao usuário e mostre o texto invertido.

palavra = str(input("Digite a palavra: "))
i = len(palavra)-1

while(i >= 0):
    print(palavra[i], end='')
    i-=1