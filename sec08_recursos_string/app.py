palavra = "Teste"
print(list(palavra))

lista = ["Olá", "mundo"]
print(" ".join(lista))
print(", ".join(lista))

frase = "Oi, tudo bem?"
print(frase.startswith("Oi"))
print(frase.endswith("bem?"))

frase = frase.upper()
print(frase)
frase = frase.lower()
print(frase)

print("tudo" in frase)
print("Olá" in lista)

redundante = "Essa frase é uma frase, pois, caso contrário, não seria uma frase"
print(redundante.count("frase"))

print(redundante.find("frase"))
print(redundante.find("arroz"))

info = "Twitter, Diego, 22/05/2015"
info_list = info.split(", ")
print(info_list)

print(redundante.replace("frase", "sentença"))
print(redundante.replace("frase", "sentença", 2))

num = "12345"
print(num.isdigit())
print(redundante.isdigit())
num2 = "123.5"
print(num2.isdigit())
num2 = num2.replace(".", "")
print(num2.isdigit())