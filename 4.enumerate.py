# Usando a função Enumerate

lista = [10, 40, 20, 30, 40]

index = 0
for i in lista:
    print(index, i)
    index += 1

# Melhorando o código

for i in enumerate(lista):
    print(i)
