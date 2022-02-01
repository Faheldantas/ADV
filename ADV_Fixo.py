print("Bem Vindo ao jogo de Adivinhação")
print("################################")
print("DICA: Obter, para si, vantagem ilícita, em prejuízo alheio, induzindo ou mantendo alguém em erro, mediante artifício, ardil, ou qualquer outro meio fraudulento:")
print("################################")

numero_secreto = 71
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):   #Enquanto
    print("Tentativa {} de {}".format (rodada, total_de_tentativas))
    chute_str = input("digite o seu numero entre 1 e 100!: ")
    print("Você digitou" , chute_str)
    chute = int (chute_str)

    if(chute <1 or chute > 100):
        print("Vocë não digitou um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Acertou Mizeravi")
        print("VOCÊ GANHOUUU!!!!!!")
        break
    else:
        if(maior):
            print("Erouuuuuuu!!!!! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Erouuuuuuu!!!!! Seu chute foi menor que o numero secreto")
    rodada = rodada + 1
        
    print("Game Over")