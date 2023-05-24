print("-"*26)
print("Digite a opção de conversão")
print("-"*26)
print('a- real-> dolar\n''b  real-> euro\n''c- real-> libra')
print('d- dolar-> real\n''e- euro-> real\n''f- libra-> real')
print("-"*14)
moeda = input()
while moeda not in ('a', 'b', 'c', 'd', 'e', 'f'):
    moeda = input("Por favor, digite uma alternativa correta\n")

print("Quanto você quer converter ? ")

#quantidade da moeda que vai ser convertida
quantidade = float(input())

#valores de cada moeda em real.
dolar = 4.95
euro = 5.36
libra = 6.12

if moeda == 'a':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade/dolar):,.2f} doláres")

if moeda == 'b':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade/euro):,.2f} euros")

if moeda == 'c':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade/libra):,.2f} libras")

if moeda == 'd':
    print(f"A quantidade convertida foi de {quantidade} dólares para {(quantidade*dolar):,.2f} reais")
if moeda == 'e':
    print(f"A quantidade convertida foi de {quantidade} euros para {(quantidade*euro):,.2f} reais")
if moeda == 'f':
    print(f"A quantidade convertida foi de {quantidade} libras para {(quantidade*libra):,.2f} reais")

print("-"*62)


