import string
import secrets

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""

    for _ in range(tamanho):
        senha += secrets.choice(caracteres)

    return senha


print("=== Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da senha: "))

if tamanho < 4:
    print("Tamanho mínimo recomendado é 4.")
else:
    senha = gerar_senha(tamanho)
    print("Senha gerada:", senha)
    salvar = input("Deseja salvar a senha em um arquivo? (s/n): ").strip().lower()
    if salvar == 's':
        with open("senha.txt", "w") as arquivo:
            arquivo.write(senha)
        print("Senha salva em 'senha.txt'.")