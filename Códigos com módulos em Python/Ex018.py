import math
angulo = int(input("Digite o ângulo para que seja dado o seno, cosseno e a tangente: "))

print(f'O ângulo dado foi de {angulo}º\nSeno: {(math.sin(math.radians(angulo))):,.3f}\n'
      f'Cosseno: {(math.cos(math.radians(angulo))):,.3f}\n'
      f'Tangente: {(math.tan(math.radians(angulo))):,.3f}')
