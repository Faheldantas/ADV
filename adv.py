import random

print("################################")
print("Bem Vindo ao jogo de Adivinhação")
print("################################")

numero_secreto = random.randrange (1,101)
total_de_tentativas = 0
rodada = 1
pontos = 1000

print("Qual é o nivel de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

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
        print("Você fez {}".format(pontos))
        break
    else:
        if(maior):
            print("Erouuuuuuu!!!!! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Erouuuuuuu!!!!! Seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    rodada = rodada + 1
 
    print("Tente outra vez")