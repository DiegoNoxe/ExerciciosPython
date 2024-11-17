#Faça um programa que pergunte ao usuario a sua idade e mostre-o se ele é maior ou menor de idade


#Obtendo a idade do usuario
idade = int(input("Digite a sua idade: "))
print(f"Você tem {idade} anos!\n")

#If e else para informa-lo se ele é maior de idade ou não
if(idade >= 18):
    print("Voce eh maior de idade\n")
else:
    print("Voce eh menor de idade\n")
    

#Fazendo a mesma coisa acima, porém de um jeito um pouco diferente
print(idade >= 18 and "voce eh maior de idade" or "voce eh menor de idade")