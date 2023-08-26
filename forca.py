import random

def jogar():
   
   imprime_msg_abertura()
   palavra_secreta = carrega_txt()
   letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  
   print(letras_acertadas)

   enforcou = False
   acertou = False
   erros = 0

   while(not enforcou and not acertou):
       
      chute = pede_chute()

      if (chute in palavra_secreta):  
         marca_chute_posicao(chute, letras_acertadas, palavra_secreta)
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
       

def imprime_msg_abertura():
   print("Bem Vindo ao jogo da forca !!")  

def carrega_txt():
   arquivo= open("palavras.txt", "r")
   palavras= []  
    
   for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

   arquivo.close()

   numero = random.randrange(0,len(palavras))
   palavra_secreta = palavras[numero].upper()
   return palavra_secreta

def inicializa_letras_acertadas(palavra):
   return ["_" for letra in palavra] #list comprehensions 

def pede_chute():
   chute = input("Qual a letra? ")
   chute = chute.strip().upper()
   return chute

def marca_chute_posicao(chute, letras_acertadas, palavra_secreta):
   index = 0
   for letra in palavra_secreta:
      if (chute == letra): 
         letras_acertadas[index] = letra   #adicionando a letra na lista de letras acertadas na posição certa         
      index += 1

if(__name__ == "__main__"):
  jogar()