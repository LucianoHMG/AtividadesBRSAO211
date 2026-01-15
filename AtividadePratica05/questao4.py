import datetime
def calcular_idade(data_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - data_nascimento
    return idade * 365
data_nascimento = int(input("Digite o ano de nascimento: "))
dias_vividos = calcular_idade(data_nascimento)
print(f"Você já viveu aproximadamente {dias_vividos} dias.")