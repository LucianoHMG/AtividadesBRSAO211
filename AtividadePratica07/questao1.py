import pandas as pd

print("=== Analisador de CSV (tempo_execucao) ===")

caminho = input("Digite o caminho do arquivo CSV (ex: dados.csv): ").strip()

try:
    df = pd.read_csv(caminho)

    if "tempo_execucao" not in df.columns:
        print("Erro: a coluna 'tempo_execucao' não existe no CSV.")
        raise SystemExit

    # Converte para número (caso tenha texto), e remove valores inválidos (NaN)
    tempos = pd.to_numeric(df["tempo_execucao"], errors="coerce").dropna()

    if tempos.empty:
        print("Erro: a coluna 'tempo_execucao' não tem valores numéricos válidos.")
        raise SystemExit

    media = tempos.mean()
    maximo = tempos.max()

    print(f"Média (tempo_execucao): {media:.2f}")
    print(f"Máximo (tempo_execucao): {maximo:.2f}")

except FileNotFoundError:
    print("Erro: arquivo CSV não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: o CSV está vazio.")
except pd.errors.ParserError:
    print("Erro: não foi possível ler o CSV (formato inválido).")
except Exception as e:
    print(f"Erro inesperado na leitura: {e}")
