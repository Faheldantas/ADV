import forca
import adv

def escolha_jogo():

    print("################################")
    print("BEM VINDO A GALERIA DE JOGOS!!!!")
    print("################################")

    print("Escolha seus jogos a baixo:")

    print("(1)Forca  (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Você escolheu o jogo da FORCA")
        forca.jogar()
    elif(jogo == 2):
        print("Você escolheu o jogo da ADIVINHAÇÃO")
        adv.jogar()
        
if(__name__ == "__main__"):
    escolha_jogo()