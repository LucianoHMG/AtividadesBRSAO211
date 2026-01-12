valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar = round(valor_reais / taxa_dolar, 2)
euro = round(valor_reais / taxa_euro, 2)

print("Conversor de Moeda:")
print(f"R$ {valor_reais:.2f} = US$ {dolar:.2f} (taxa R${taxa_dolar})")
print(f"R$ {valor_reais:.2f} = € {euro:.2f} (taxa R${taxa_euro})")
