#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

cont = 0

phone  = str(input("Você telefonou para a vitima? "))[0].upper()

if(phone == 'S'):
    cont+=1

local  = str(input("Esteve no local do crime? "))[0].upper()

if(local == 'S'):
    cont+=1

perto  = str(input("Mora perto da vitima? "))[0].upper()

if(perto == 'S'):
    cont+=1

divida = str(input("Devia para a vitima? "))[0].upper()

if(divida == 'S'):
    cont+=1

work = str(input("Ja trabalhou com a vitima? "))[0].upper()

if(work == 'S'):
    cont+=1


if(cont == 2):
    print("Voce eh suspeito")
else:
    if(cont >= 3 and cont <= 4):
        print("voce eh cumplice")
    else:
        print("voce eh assassino")



