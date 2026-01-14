while True :
    try:
        senha = input("Digite a senha :")
        if senha.lower() == 'sair':
            print("Programa encerrado.") 
            break   
        if len(senha) < 8 :
            raise Exception("Senha deve ter no mínimo 8 caracteres.")
        tem_numero = False
        for caractere in senha:
            if caractere in '0123456789':
                tem_numero = True
                break 
        if tem_numero == False :
            raise Exception("Senha deve conter pelo menos um número.")    
        print("Senha válida.")
    except Exception as e:
        print(f"Erro: {e}")

# Validador de Senha   