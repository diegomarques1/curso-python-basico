num = int(input("Digite um número: "))
div = 0
count = num

while count > 0:
    if num % count == 0:
        div += 1

    count -= 1

if div == 2:
    print("O número {} é primo!".format(num))
else:
    print("O número {} não é primo!".format(num))