produto_a = ["Camisa", "Rosa", 25.62]
produto_b = ["Bermuda", "Marrom", 113.90]
produto_c = ["Casaco", "Bege", 200.00]

lista_produtos = [produto_a, produto_b, produto_c]

print("Lista de produtos:", lista_produtos)

for produto in lista_produtos:
    print("O produto é %s, tem cor %s e custa R$%.2f" % (produto[0], produto[1], produto[2]))

