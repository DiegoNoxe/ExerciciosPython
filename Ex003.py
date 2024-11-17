#Faça uma função que leia três números e exiba o maior entre eles.

def comparacao(a, b, c):
  return max(a, b, c)  

a = 4
b = 3
c = 5

print(f"O maior é: {comparacao(a,b,c)}")