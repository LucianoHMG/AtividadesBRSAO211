def calcular_gorjeta (valor_conta, percentual_gorjeta):
    gorjeta = valor_conta * (percentual_gorjeta / 100)
    valor_total = valor_conta + gorjeta
    return gorjeta, valor_total
valor = float(input("Digite o valor da conta: R$ "))
porcecertagem = float(input("Digite o percentual da gorjeta (%): "))
calcular_gorjeta(valor, porcecertagem)
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcecertagem)[0]:.2f}")