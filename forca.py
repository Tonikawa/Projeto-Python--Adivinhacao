def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
       
       chute = input("Qual a letra? ")
       
       for letra in palavra_secreta:
          if(chute == letra):
            print("Você acertou a letra")
            print(chute)
          else:
             print("Você errou a letra")
             
       print("jogando...")
       

    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()