import random
print('                           ***********************************')
print('                           01011000011101001010010100100101101')
print('\n                                    JOGO DE ADIVINHA \n')
print('                           01011000011101001010010100100101101')
print('                           ***********************************')


print("\n1- Facil")
print("2- Médio")
print("3- Dificil")

opcao = int (input("Escolha a dificuldade:"))

print("Você escolheu: ", opcao)
if (opcao ==1):
    total_tentativas = 15
    numero_secreto = random.randrange(1,50)
elif (opcao ==2):
    total_tentativas = 10
    numero_secreto = random.randrange(1,80)
elif (opcao ==3):
    total_tentativas = 6
    numero_secreto = random.randrange(1,100)
else:
    print("Essa opçâo não existe. Escolha uma opção valida.")

for rodada in range(1, total_tentativas + 1):
    print ("\nTentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite o seu numero: ")
    print("\nSeu numero é: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!!\n")
        break
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto\n")
        elif(menor):
            print("O seu chute foi menor que o número secreto\n")

print("Fim de jogo! O número secreto era: ", numero_secreto)

