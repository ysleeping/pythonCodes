name = input("Digite um nome válido com mais de 3 caracteres: ")

while len(name) <= 3:
    name = input("Digite um nome válido com mais de 3 caracteres: ")


print(f'Nome: {name}')