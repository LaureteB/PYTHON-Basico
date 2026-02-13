while True:
    try:
        saque = int(input("Digite o valor do saque: "))
        if saque >= 1000:
            print ("O limite de saque é R$1000,00.")
            continue
        elif saque <= 0:
            print("Digite apenas números positivos.")
            continue
        else:
            print("Saque efetuado")
            break
    except ValueError:
        print("Digite apenas números positivos.")

print("Seu saque foi de: ", saque)
