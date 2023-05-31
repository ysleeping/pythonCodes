import time

print("olá mundo")
print('                                           The F*cking End                                                     ')
print('Esse é um programa de teste do meu conhecimento em python, estou me baseando em um rpg de multiplas escolhas e '
      'multiplos caminhos e tentar conseguir criar isso ao máximo e mais próximo de um rpg de mesa ou algo do tipo'
      'espero que gostem ou aproveitem, o desenvolvimento é lento graças a minha falta de vergonha na cara'
      'Bom "Jogo" kkkkkk')
print("???: Se você iniciou esse programa agora, digite enter para continuar...")
input(" ")
name = input('Digite teu nome, jovem padawan: ')
level = 1
hp = 100
time.sleep(5)

print("???: talvez você tenha duvidas do que está acontecendo, sei que pode ser estranho mas temos que conversar...\n")
time.sleep(5)
print('a- perguntar "Quem é você ?"'
      '\nb- Não responder'
      '\nDigite uma das opções...')
resposta = input()

if resposta == "a":
    print("???: Eu sou você e ao mesmo tempo sou algo diferente")
    time.sleep(5)
    print("???: Mas não tenha medo, sou mais confiante do que você imagina\n")

if resposta == "b":
    print("???: Talvez você ainda não tenha coragem de interagir, mas não tenha medo, sou mais confiante do que você imagina!\n")

time.sleep(5)
print('a- O que está acontecendo?'
      '\nb- Mas que porra é essa?'
      '\nc- Continuar sem responder'
      '\nDigite uma das opções...')

resposta1 = input("Você: ")
time.sleep(5)
if resposta1 == "a":
    print("\n???: Eu sou você no futuro, assim como todos ja imaginam, as máquinas realmente venceram.\n"
          "No fim nós tivemos que evoluir também e agora estamos numa simbiose com as máquinas que ainda podemos controlar, a internet se torno a rachadura no espaço tempo,\n"
          "por esse motivo é muito fácil transmitir pensamentos do futuro ou interagir com outras pessoas\n")

if resposta1 == "b":
    print("\n???: Eu sou você no futuro, assim como todos ja imaginam, as máquinas realmente venceram.\n"
          "No fim nós tivemos que evoluir também e agora estamos numa simbiose com as máquinas que ainda podemos controlar,"
          " a internet se torno a rachadura no espaço tempo,\n"
          "por esse motivo é muito fácil transmitir pensamentos do futuro ou interagir com outras pessoas\n")
else:
    print("\n???: Você parece não querer saber muito, talvez tenha duvidas sobre o que está ou vai acontecer,"
          "\nnessa época eu estava depressivo pois minha vida não se tornou o que eu imaginava,\n"
            "mas se quiser um spoiler, vai dar tudo certo, mesmo que não seja perfeito ainda vai dar tudo certo !\n")

time.sleep(5)
print('a- isso é real ?'
      '\nb- como posso saber se você está falando a verdade ?'
      '\nc- Porra, isso não é de um filme ? Matrix ?'
      '\nDigite uma das opções...')
resposta2 = input("Você: ")
time.sleep(5)
if resposta2 == "a":
    print("\n???: O que é real? Como você define o real? Se você está falando sobre o que você pode sentir, o que você pode cheirar, "
          "o que você pode saborear e ver, o real são simplesmente sinais elétricos interpretados pelo seu cérebro.")

if resposta2 == "b":
    print("\n???: Hahahaha, como assim ? eu posso ser apenas um delírio da sua mente, "
          "você não pode considerar nada disso ou qualquer outra coisa como real seu idiota.")
else:
    print("\n???: Você deveria fazer as perguntas certas e não perder tempo supondo as coisas...")

print('???: Eu realmente estou sem paciência para continuar tal coisa, então vamos adicionar uma coisinha nessa brincadeira, '
      'você irá receber um número de hp(valor de vida) e um nível, seu hp ira começar em 100 e seu nível será 1,'
      ' cada vez que você fiz uma pergunta errada vai ')

print(f'Dados do jogador: \nNome do jogador: {name}\nLevel do jogador: {level}\nHP do jogador: {hp}')
print('???: Agora irá ficar divertido hahahahaha')
