import requests

def consultar_cep(cep: str):
    cep = "".join(ch for ch in cep if ch.isdigit())  # só números

    if len(cep) != 8:
        print("Falha: CEP deve ter 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()

        if dados.get("erro"):
            print("Falha: CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        cidade = dados.get("localidade", "")
        estado = dados.get("uf", "")

        print("=== Resultado do CEP ===")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException:
        print("Falha na requisição. Verifique a conexão.")
    except ValueError:
        print("Falha ao ler a resposta da API.")

cep_digitado = input("Digite o CEP (ex: 01001000): ")
consultar_cep(cep_digitado)
