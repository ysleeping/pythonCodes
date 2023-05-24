import time
print("olá mundo")
print("???: Se você iniciou esse programa agora, digite enter para continuar...")

input(" ")
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

resposta1 = input("Você: ")

if resposta1 =="o que está acontecendo ?":
    print("\n???: Eu sou você no futuro, assim como todos ja imaginam, as máquinas realmente venceram.\n"
          "No fim nós tivemos que evoluir também e agora estamos numa simbiose com as máquinas que ainda podemos controlar, a internet se torno a rachadura no espaço tempo,\n"
          "por esse motivo é muito fácil transmitir pensamentos do futuro ou interagir com outras pessoas\n")
else:
    print("\n???: Você parece não querer saber muito, talvez tenha duvidas sobre o que está ou vai acontecer,\nnessa época eu estava depressivo pois minha vida não se tornou o que eu imaginava,\n"
          "mas se quiser um spoiler, vai dar tudo certo, mesmo que não seja perfeito ainda vai dar tudo certo !\n")

resposta2 = input("Você: ")

if resposta2 == "isso é real ?":
    print("\n???: O que é real ? Como se define o real \nVocê saberia diferenciar algo real e inreal simplesmente pelo toque ?\n")

elif resposta2 == "como posso saber se você está falando a verdade ?":
    print("\n???: Sei que você tem 25 anos, vai completar 26 esse ano,\ne que no dia de hoje desceu para fumar e encontrou uma gata perto do local e foi fazer carinho nela,\n"
          "ela mordeu você e arranhou sua mão e hoje você irá sair com seus amigos pois é dia da marcha pró descriminalização da maconha")
else:
    print("\n???: Você até agora não consegue comprender a verdade")

