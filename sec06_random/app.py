import random

def megasena():
    resultado = []
    for i in range(6):
        resultado.append(random.randint(1, 60))
    return resultado

print("Resultado da mega:", megasena())