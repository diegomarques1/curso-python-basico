def printName(name = "Lucas"):
    print("Hi,", name)

printName()
printName("Diego")

def multiply(a, b = 0):
    return a * b

print(multiply(5))
print(multiply(5, 2))