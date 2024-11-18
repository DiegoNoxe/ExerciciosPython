#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = int(input("Horas trabalhadas no mês: "))
GanhoHora = int(input("Ganho por horas trabalhadas: "))

print(f'O seu salario eh: {horas*GanhoHora}')