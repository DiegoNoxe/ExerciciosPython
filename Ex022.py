#Contador de Vogais

palavra = input("Digite uma frase: ")
vogais = "aeiou"
cont = 0

for caractere in palavra:
    if caractere in vogais:
        cont += 1

print(f"A frase contém {cont} vogais.")
