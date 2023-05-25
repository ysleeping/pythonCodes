print("-"*26)
print("Digite a opção de conversão")
print("-" * 26)
print('a- real-> dolar\n''b  real-> euro\n''c- real-> libra')
print('d- dolar-> real\n''e- euro-> real\n''f- libra-> real')
print("-" * 14)

# coin é a moeda que vai ser convertida
coin = input()
while coin not in ('a', 'b', 'c', 'd', 'e', 'f'):
    coin = input("Por favor, digite uma alternativa correta\n")

print("Digite a quantidade que você irá converter: ")

# quantidade da moeda que vai ser convertida
quantidade = float(input())

#valores de cada moeda em real.
dol = 4.95
euro = 5.36
libra = 6.12

if coin == 'a':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade / dol):,.2f} doláres")

if coin == 'b':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade / euro):,.2f} euros")

if coin == 'c':
    print(f"A quantidade convertida foi de {quantidade} reais para {(quantidade / libra):,.2f} libras")

if coin == 'd':
    print(f"A quantidade convertida foi de {quantidade} dólares para {(quantidade*dol):,.2f} reais")

if coin == 'e':
    print(f"A quantidade convertida foi de {quantidade} euros para {(quantidade*euro):,.2f} reais")

if coin == 'f':
    print(f"A quantidade convertida foi de {quantidade} libras para {(quantidade*libra):,.2f} reais")

print("-"*62)


