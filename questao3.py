nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print("Calculadora de Média Escolar:")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media}")
if media >= 7.0:
    print("Status: Aprovado")   