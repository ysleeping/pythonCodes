import random
alunos = []
for _ in range(3):
    while True:
        try:
            alunos.append(input('Digite o nome do aluno: '))
            break
        except ValueError:
            print('Digite algo válido')

print(f'O aluno escolhido para limpar a louça da vez foi: {random.choice(alunos)}')
