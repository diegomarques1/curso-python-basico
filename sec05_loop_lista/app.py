lista = [0, 0, 0] # sem append por enquanto
lista[0] = int(input("Digite o primeiro valor: "))
lista[1] = int(input("Digite o segundo valor: "))
lista[2] = int(input("Digite o terceiro valor: "))

print("Somando 10...")
for i in range(0, len(lista), 1):
    print(lista[i] + 10)

nova_lista = [] # com append agora
nova_lista.append(int(input("Digite o primeiro valor: ")))
nova_lista.append(int(input("Digite o segundo valor: ")))
nova_lista.append(int(input("Digite o terceiro valor: ")))

print("Somando 10...")
for i in range(len(nova_lista)):
    print(nova_lista[i] + 10)
