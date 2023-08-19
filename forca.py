def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
       
       chute = input("Qual a letra? ")
       chute = chute.strip() #tratamento de string - tirando espaço

       index = 0

       for letra in palavra_secreta:
          if(chute.upper() == letra.upper()): #tratamento de string- igualando o chute com a palavra secreta
            print("Você acertou a letra {} na posição {}".format(chute, index))
          index = index + 1
          #else:
             #print("Você errou a letra")

       print("jogando...")
       

    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()