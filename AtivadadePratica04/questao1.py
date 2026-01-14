def calculadora():
    print("=== Calculadora Básica ===")
    try:
        a = float(input("Digite o 1º número: ").replace(",", "."))
        op = input("Digite a operação (+, -, *, /): ").strip()
        b = float(input("Digite o 2º número: ").replace(",", "."))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = a / b
    else:
        print("Operação inválida. Use +, -, * ou /.")
        return

    print(f"Resultado: {a} {op} {b} = {resultado}")

calculadora()
