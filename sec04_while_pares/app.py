number = int(input("Digite um número qualquer: "))
i = 0

print("Imprimindo os números pares de %d até %d" % (i, number))
while i <= number:
    if i % 2 == 0:
        print(i)
    i += 1