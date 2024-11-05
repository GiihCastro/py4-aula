lista_de_usuarios = []

while True:
    print('Boas vindas! Escolha uma das opções abaixo:')
    menu = input('''\n ------ Sistema PyLatte ------
             | 1 - Cadastrar
             | 2 - Fazer Login
             | 0 - Sair
             
             Digite sua escolha => ''')
    match menu:
        case "1":
            print("\n----- Cadastro -----")
            nickname = input("Digite seu usuário: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")

            usuario = {
                "Nickname": nickname,
                "E-mail": email,
                "Senha": senha
            }
            lista_de_usuarios.append(usuario)

        case "2":
            print("\n----- Login -----")
            email_login = input("Digite seu e-mail: ")
            senha_login = input("Digite sua senha: ")
            
            usuario_encontrado = False
            
            for usuario_da_vez in lista_de_usuarios:
                if usuario_da_vez["E-mail"] == email_login and usuario_da_vez["Senha"] == senha_login:
                    usuario_encontrado = True
                    print("Login efetuado com sucesso!")
            if usuario_encontrado == False:
                print("E-mail ou Senha inválidos")

        case "0":
            break

        case _:
            print("Opção inválida!")