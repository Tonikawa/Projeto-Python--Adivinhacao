def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
       
       chute = input("Qual a letra? ")
       chute = chute.strip() #tratamento de string - tirando espaço

       index = 0

       for letra in palavra_secreta:
          if(chute.upper() == letra.upper()): #tratamento de string- igualando o chute com a palavra secreta
             letras_acertadas[index] = letra   #adicionando a letra na lista de letras acertadas na posição certa         
          index = index + 1
          #else:
             #print("Você errou a letra")

       print(letras_acertadas)
     
       

    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()