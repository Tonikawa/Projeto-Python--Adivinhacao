import random 

print("Bem Vindo ao jogo de adivinhação!!")

numero_secreto = (random.randrange(1,101))
total_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade ?")
print("(1) Fácil (2) Médio (3) Díficil")

nivel = int(input("Defina o nível:"))
if(nivel==1):
  total_tentativas=20
elif(nivel==2):
  total_tentativas=10
else:
  total_tentativas=5
  print("Nível definido para Díficil")

# pode  ser usado o while também while(rodada < total_tentativas)
for rodada in range (1, total_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada, total_tentativas))
  
    chute = int(input("Digite o um número entre 1 e 100: "))
    print("Você digitou o número:", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!!")
        continue
    
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto   
    
    if (acertou):
        print("Você acertou o número!! Total de pontos {} nesta rodada".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número certo!")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número certo!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
if (total_tentativas==0):
  print("O número certo é {}".format(numero_secreto))
  
print("Fim de Jogo!")