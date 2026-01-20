import json

print("=== Escreve e Lê JSON ===")

dados = {
    "nome": "Luciano",
    "idade": 34,
    "cidade": "Praia Grande"
}

caminho = input("Digite o nome/caminho do JSON (ex: pessoa.json): ").strip()

# Salvar
try:
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print("JSON salvo com sucesso!")
except PermissionError:
    print("Falha: sem permissão para salvar nesse local.")
    raise SystemExit
except OSError as e:
    print(f"Falha ao salvar: {e}")
    raise SystemExit

# Ler
try:
    with open(caminho, "r", encoding="utf-8") as f:
        lido = json.load(f)

    print("\nDados lidos do JSON:")
    print(f"Nome: {lido.get('nome')}")
    print(f"Idade: {lido.get('idade')}")
    print(f"Cidade: {lido.get('cidade')}")

except FileNotFoundError:
    print("Falha: o arquivo JSON não existe para leitura.")
except json.JSONDecodeError:
    print("Falha: o JSON está corrompido ou inválido.")
except OSError as e:
    print(f"Falha ao ler: {e}")
