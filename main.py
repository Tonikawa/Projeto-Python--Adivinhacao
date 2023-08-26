#Fabio Silveira Tanikawa--- Terminado em 26 de agosto
import forca 
import adivinhação
print("Escolha seu jogo!")

print("(1) Forca (2)Adivinhação")

#jogo = int(input("Qual o jogo?"))

while True:
  jogo = int(input("Qual o jogo?"))
  if(jogo == 1):
    print("Você escolheu o jogo da Forca")
    forca.jogar()
    break
  elif(jogo == 2):
    print("Você escolheu o jogo de Adivinhação")
    adivinhação.jogar()
    break
  else:
    print("Pare de zoar, proxima vez escolha um número certo!")
    