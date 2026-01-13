print("=== CONVERSOR DE TEMPERATURA ===")

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Unidade de destino (C, F ou K): ").upper()

# 1) Converte para Unidade desejada 
if unidade_origem == "C":
    celsius = temperatura
elif unidade_origem == "F":
    celsius = (temperatura - 32) * 5 / 9
elif unidade_origem == "K":
    celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# 2) Converte  para a unidade desejada
if unidade_destino == "C":
    resultado = celsius
elif unidade_destino == "F":
    resultado = (celsius * 9 / 5) + 32
elif unidade_destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"Resultado: {resultado:.2f}°{unidade_destino}")
