#Nome na vertical em escada. 

nome = str(input("Digite um nome"))
cont = len(nome)-1
i = 0

while(i <= cont):
    print(nome[:i+1])
    i += 1