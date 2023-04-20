renda = float(input("Digite sua renda: "))
limite = 0

if renda < 2000:
    limite = 1000
elif renda >= 2000 and renda < 4000:
    limite = 2000
elif renda >= 4000 and renda <= 10000:
    limite = 3000
elif renda > 10000:
    print("Fale com o gerente")
    limite = 3000

print("Seu limite é de", limite, "reais")