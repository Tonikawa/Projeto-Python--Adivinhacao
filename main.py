import forca 
import adivinhação
print("Escolha seu jogo!")

print("(1) Forca (2)Adivinhação")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
  print("Você escolheu o jogo da Forca")
  forca.jogar()
elif(jogo == 2):
  print("Você escolheu o jogo de Adivinhação")
  adivinhação.jogar()
  