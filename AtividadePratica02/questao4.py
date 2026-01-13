distancia = 300
combustivel = 25

consumo = round(distancia / combustivel, 2)

print("Calculadora de Consumo:")
print(f"Distância: {distancia} km")
print(f"Combustível: {combustivel} L")
print(f"Consumo médio: {consumo} km/l")     
# Adicionei a condição para verificar se o consumo é eficiente
if consumo >= 12:
    print("Consumo eficiente")  