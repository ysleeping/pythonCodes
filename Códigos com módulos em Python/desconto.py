ValorDoProduto = float (input("Digite o valor do produto: "))
frase = 'curso em video python'
frase.upper()
desconto = 0.05 * ValorDoProduto
ValorComDesconto = ValorDoProduto - desconto
print('A loja está com uma promoção de 5% de desconto !!!')
print(f'Por conta disso o valor do seu produto passou de {ValorDoProduto:,.2f} reais para {ValorComDesconto:,.2f} reais, seu desconto foi de {desconto:,.2f} reais')
print(frase)

print(len(frase))
print('')
print(frase.count('o'))
print('')
print(frase.count('o', 0, 14))
print('')
print(frase.find('deo'))





