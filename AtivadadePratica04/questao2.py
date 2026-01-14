def media_turma():
    print("=== Média da Turma ===")
    notas = []

    while True:
        entrada = input("Digite uma nota (ou 'fim' para terminar): ").strip().lower()

        if entrada == "fim":
            break

        try:
            nota = float(entrada.replace(",", "."))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")

    if len(notas) == 0:
        print("Nenhuma nota registrada.")
        return

    media = sum(notas) / len(notas)
    print(f"Total de alunos: {len(notas)}")
    print(f"Média da turma: {media:.2f}")

media_turma()
