def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def operacao(a, b, f):
    return f(a, b)

sum = operacao(5, 5, soma)
mult = operacao(5, 5, multiplicacao)
print("Soma:", sum, "\nMultiplicação:", mult)