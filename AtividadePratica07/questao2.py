import csv

print("=== Criador de CSV (nome, idade, cidade) ===")

pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 31, "cidade": "Praia Grande"},
    {"nome": "Carla", "idade": 19, "cidade": "Santos"},
]

arquivo_saida = input("Digite o nome/caminho do CSV para salvar (ex: pessoas.csv): ").strip()

try:
    with open(arquivo_saida, "w", newline="", encoding="utf-8") as f:
        colunas = ["nome", "idade", "cidade"]
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(pessoas)

    print("Arquivo salvo com sucesso!")
    print("\nPrévia (tabular):")
    print("nome\tidade\tcidade")
    for p in pessoas:
        print(f"{p['nome']}\t{p['idade']}\t{p['cidade']}")

except PermissionError:
    print("Falha: sem permissão para salvar nesse local.")
except OSError as e:
    print(f"Falha ao salvar o arquivo: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")