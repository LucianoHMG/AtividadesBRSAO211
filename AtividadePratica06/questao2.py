import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()  # dispara erro se status != 200

        dados = resp.json()
        user = dados["results"][0]

        nome = f'{user["name"]["first"]} {user["name"]["last"]}'
        email = user["email"]
        pais = user["location"]["country"]

        print("=== Usuário Fictício ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print("Falha na conexão ou na requisição. Tente novamente mais tarde.")
    except (KeyError, ValueError):
        print("Falha ao processar a resposta da API.")

buscar_usuario()