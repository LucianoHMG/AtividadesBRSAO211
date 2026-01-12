produto = "Camiseta"
preco_original = 50.00
desconto_pct = 20

desconto_val = round(preco_original * (desconto_pct / 100), 2)
preco_final = round(preco_original - desconto_val, 2)

print("Calculadora de Desconto:")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_pct}% (R$ {desconto_val:.2f})")
print(f"Preço final: R$ {preco_final:.2f}")
