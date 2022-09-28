# List Comprehensions

lista = [50, 30, 20, 60, 20, 40]

nova_lista = []

for i in lista:
    nova_lista.append(i*2)

print('Usando for loop           ', nova_lista)

# Melhorando o código

lista_simplificada = [i*2 for i in lista]
print('Usando List Comprehensions', lista_simplificada)
