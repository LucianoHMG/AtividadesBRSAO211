def eh_palindromo(texto: str) -> bool:
    """
    Verifica se um texto é palíndromo.
    Ignora espaços, pontuação e diferenças entre maiúsculas/minúsculas.
    """
    texto_formatado = ""

    for caractere in texto:
        if caractere.isalnum():
            texto_formatado += caractere.lower()

    return texto_formatado == texto_formatado[::-1]


entrada = input("Digite uma palavra ou frase: ").strip()

if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")
