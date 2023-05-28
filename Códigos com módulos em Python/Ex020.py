import random
alunos = []
for _ in range(5):
    while True:
        try:
            alunos.append(input('Digite o nome do aluno: '))
            break
        except ValueError:
            print('Digite algo válido')
print(f'Os alunos escolhidos para limpar a louça essa semana foram: {random.sample(alunos, 3)}')
