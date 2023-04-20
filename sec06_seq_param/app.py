def sumAll(*numbers):
    soma = 0
    for num in numbers:
        soma += num
    return soma

s = sumAll(1, 2, 3, 4, 5)

print(s)