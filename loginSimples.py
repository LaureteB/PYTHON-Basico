while True:
    try:
        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ")

        if nome == "":
            print("O nome não pode ser vazio.")
            continue  # Volta para o início do loop se o nome for vazio
        
        # Verifica se a senha tem pelo menos 6 caracteres
        if len(senha) >= 6:
            print(f"Usuário {nome} cadastrado com sucesso!")
            break  # Sai do loop principal
        else:
            print("A senha deve ter no mínimo 6 caracteres.")
            
    except ValueError:
        print("Ocorreu um erro inesperado. Tente novamente.")

print("Fez login!")