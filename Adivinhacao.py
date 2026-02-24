print('*****************************888')
print('**********JOGO DE ADIVINHA***********888')
print('*****************************888')

numero_secreto = 42
total_tentativas = 15
rodada = 1

while(rodada <= total_tentativas):

    chute_str = input("Digite o seu numero: ")

    print("Seu numero é: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!!")
        break
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
    rodada = rodada +1
print("Fim de jogo!")
