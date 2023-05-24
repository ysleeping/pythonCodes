print("-"*26)
print("digite a opção de conversão")
print("-"*26)
print('a- real-> dolar\n''b  real-> euro\n''c- real-> ouro')
print('d- dolar-> real\n''e- euro-> real\n''f- ouro-> real')
print("-"*14)
moeda = input()
while moeda not in ('a', 'b', 'c','d','e','f'):
    moeda = input("por favor, digite uma alternativa correta\n")

print("quanto você quer converter ? ")

#quantidade da moeda que vai ser convertida
quantidade = float(input())

#valores de cada moeda em real.
dolar = 4.97
euro = 5.36
ouro = 315.85

if moeda == 'a':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade/dolar):,.2f} doláres")
if moeda == 'b':
    print("Você escolheu a conversão de real para euro")

if moeda == 'c':
    print("Você escolheu a conversão de real para ouro")
