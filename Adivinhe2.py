import random
#Cores no terminal PY
VERMELHO = "\033[31m]"
VERDE = "\033[32m]"
AMARELO = "\033[33m]"
AZUL = "\033[34m]"
RESET = "\033[0m]"

def escolher_nivel():
    print("\nEscolha o nível: ")
    print("1 -- Fácil (10 tentativas)")
    print("2 -- Médio (5 tentativas)")
    print("3 -- Difícil (3 tentativas)")

    while True:
        nivel_srt = input("Digite apenas números (1, 2, 3): ")
        if not nivel_srt.isdigit():
            print(VERMELHO+"Digite apenas números!"+RESET)
            continue
        nivel_srt = int(nivel_srt)
        if nivel == 1:
            return 10
        elif nivel == 2:
            return 5
        elif nivel == 3:
            return 3
        else:
            print(AMARELO+"Escolha apenas 1, 2 ou 3"+RESET)


def jogar():
    print(AZUL+'                           ***********************************'+RESET)
    print(AZUL+'                           01011000011101001010010100100101101'+RESET)
    print(AZUL+'\n                                    JOGO DE ADIVINHA \n'+RESET)
    print(AZUL+'                           01011000011101001010010100100101101'+RESET)
    print(AZUL+'                           ***********************************'+RESET)
    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,31)
    pontos = 100
    historico = []

    for rodada in range(1, total_tentativas + 1):
        print ("\nTentativa {rodada} de {total_tentativas}".format(rodada,total_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")

        if not chute_str.isdigit():
            print(VERMELHO+"Digite um número entre 1 e 100: "+RESET)
            continue

        
        print("\nSeu numero é: ", chute_str)
        chute = int(chute_str)



        if(chute < 1 or chute > 100):
            print(AMARELO+"Você deve digitar um número entre 1 e 100!"+RESET)
            continue
        historico.append(chute)

        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

