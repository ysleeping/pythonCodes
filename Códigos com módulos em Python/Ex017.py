import math

catOP = float (input("Digite o valor do cateto oposto: "))
catAD = float (input("Digite o valor do cateto adjacente: "))
hip =  math.sqrt((math.pow(catOP,2)) + (math.pow(catAD,2)))
print(f'O valor da hipotenusa é : {hip} cm')

