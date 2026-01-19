import requests

def cotacao_para_brl(moeda: str):
    moeda = moeda.strip().upper()
    par = f"{moeda}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Erro: moeda não encontrada ou formato inválido.")
            return

        info = dados[chave]

        atual = info.get("bid")
        maxima = info.get("high")
        minima = info.get("low")
        atualizado_em = info.get("create_date")

        if not all([atual, maxima, minima, atualizado_em]):
            print("Erro: resposta incompleta da API.")
            return

        print(f"=== Cotação {moeda}/BRL ===")
        print(f"Valor atual: {float(atual):.4f}")
        print(f"Máxima:      {float(maxima):.4f}")
        print(f"Mínima:      {float(minima):.4f}")
        print(f"Atualizado:  {atualizado_em}")

    except requests.exceptions.RequestException:
        print("Erro na requisição. Verifique sua internet ou tente mais tarde.")
    except (ValueError, TypeError):
        print("Erro ao processar os valores retornados.")

moeda = input("Digite a moeda (ex: USD, EUR, BTC): ")
cotacao_para_brl(moeda)