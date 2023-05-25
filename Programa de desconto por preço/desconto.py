ValorDoProduto = float (input("Digite o valor do produto: "))
desconto = 0.05 * ValorDoProduto
ValorComDesconto = ValorDoProduto - desconto
print('A loja está com uma promoção de 5% de desconto !!!')
print(f'Por conta disso o valor do seu produto passou de {ValorDoProduto:,.2f} reais para {ValorComDesconto:,.2f} reais, seu desconto foi de {desconto:,.2f} reais')