salario = float(input("Digite o valor do salário: "))
porcentagem = int(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print("Salário após aumento: %.2f" % novo_salario)