def jogar():
    print("Bem Vindo ao jogo da forca !!")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] #list comprehensions   

    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)

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
         erros = erros + 1
         print("Você errou {} vez/vezes. Cuidado, você só possui seis chances ". format(erros))

      enforcou = erros == 6
      acertou = "_" not in letras_acertadas # underscore não está nas letras acertadas, ele encerra
      print(letras_acertadas)
   
    if(acertou): #acertou = true
       print("Você Ganhou o jogo!")
    else: #enforcou = true
       print("Você perdeu o jogo!")
    print("Fim do jogo!!")
  
if(__name__ == "__main__"):
  jogar()