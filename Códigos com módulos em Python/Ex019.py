import random
turma = []
aluno = input('Digite o nome do aluno: ')
turma.append(aluno)
aluno1 = input('Digite o nome do aluno: ')
turma.append(aluno1)
aluno2 = input('Digite o nome do aluno: ')
turma.append(aluno2)

elemento = random.choice(turma)

print(f'O aluno escolhido para limpar a louça da vez foi: {elemento}')