def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
       
       chute = input("Qual a letra? ")
      
       index = 0

       for letra in palavra_secreta:
          if(chute == letra):
            print("Você acertou a letra {} na posição {}".format(letra, index))
          index = index + 1
          #else:
             #print("Você errou a letra")

       print("jogando...")
       

    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()