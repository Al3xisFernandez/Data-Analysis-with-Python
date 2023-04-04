productos = [("Campera", 3500), ("Mochila", 2400), ("Zapatillas", 5200), ("Jean", 1600)]

# Ordenar productos de mayor a menor precio usando map, sorted y funciones lambda
productos_ordenados = list(map(lambda x: x[0], sorted(productos, key=lambda x: x[1], reverse=True)))

# Imprimir los productos ordenados
print(productos_ordenados)
