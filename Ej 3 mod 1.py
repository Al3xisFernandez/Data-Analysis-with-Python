lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [3, 5, 7, 9]
lista3 = []

for elem in lista1:
    if elem not in lista2:
        lista3.append(elem)

print(lista3)
lista1 = [1, 2, 3, 4, 5, 6, 7, 10, 20]
lista2 = [3, 5, 7, 9]
lista3 = [elem for elem in lista1 if elem not in lista2]

print(lista3)
