while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <=0:
            print("A idade deve ser maior que 0.")
        else:
            break
    except ValueError:
        print("Digite apenas números inteiros.")

print("Idade cadastrada:", idade)