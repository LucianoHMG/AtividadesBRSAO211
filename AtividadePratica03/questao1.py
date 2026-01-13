idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança (0-12 anos)")
elif 13 <= idade <= 17:
    print("Adolescente (13-17 anos)")
elif 18 <= idade <= 59:
    print("Adulto (18-59 anos)")
else:
    print("Idoso (60 anos ou mais)")            