def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
       
      chute = input("Qual a letra? ")
      chute = chute.strip().upper() #tratamento de string - tirando espaço e padronizando letras

      if (chute in palavra_secreta):  
         index = 0
         for letra in palavra_secreta:
            if(chute == letra): 
               letras_acertadas[index] = letra   #adicionando a letra na lista de letras acertadas na posição certa         
            index += 1
      else:
         print("Você errou a letra")
         erros = erros + 1

      enforcou = erros == 6
      print(letras_acertadas)
     
       

    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()