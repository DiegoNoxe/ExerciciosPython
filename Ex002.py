#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: – Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO – Média 7.0 ou superior: APROVADO

FirstNota  = float(input("Digite a sua primeira nota"))
SecondNota = float(input("Digite a sua segunda nota"))
media = (FirstNota+SecondNota)/2

if(media >= 7):
    print(f"A sua media eh {media}! voce esta APROVADO")
else:
   if(media <= 5):
    print(f"A sua media eh {media}! voce esta REPROVADO")
   else:
    print(f"A sua media eh {media}! voce esta de RECUPERACAO")