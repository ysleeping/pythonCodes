import math
angulo = int(input("Digite o ângulo para que seja dado o seno, cosseno e a tangente: "))

print(f'O ângulo dado foi de {angulo}º\nSeno: {math.sin(math.radians(angulo))}\n'
      f'Cosseno: {math.cos(math.radians(angulo))}\n'
      f'Tangente: {math.tan(math.radians(angulo))}')
