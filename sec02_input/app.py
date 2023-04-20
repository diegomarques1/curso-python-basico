company = input("Você trabalha em qual empresa?\n")
salary = float(input("Qual o seu salário?\n"))
months = int(input("Você trabalha na empresa há quantos meses?\n"))

print("Empresa: {}\nSalário: R${:.2f}\nTempo na empresa: {} meses".format(company, salary, months))