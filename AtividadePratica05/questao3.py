def calcular_preco_com_desconto(preco, desconto):
    valor_desconto = preco * desconto / 100
    preco_final = preco - valor_desconto
    return preco_final


print("=== Calculadora de Desconto ===")

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))

preco_final = calcular_preco_com_desconto(preco, desconto)

print("Preço final:", round(preco_final, 2))
