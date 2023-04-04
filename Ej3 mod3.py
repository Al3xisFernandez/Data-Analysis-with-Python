import numpy as np

# Crear un vector con diez números, todos ceros.
vector_ceros = np.zeros(10)

# Crear un vector con diez números al azar.
vector_azar = np.random.rand(10)

# Crear una matriz de 2x3 y multiplicarla por su traspuesta.
matriz = np.array([[1, 2, 3], [4, 5, 6]])
resultado = matriz.dot(matriz.T)

# Imprimir los resultados
print("Vector con diez números, todos ceros:")
print(vector_ceros)

print("Vector con diez números al azar:")
print(vector_azar)

print("Multiplicación de la matriz por su traspuesta:")
print(resultado)
