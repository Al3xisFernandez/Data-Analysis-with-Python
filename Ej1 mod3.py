#!/usr/bin/env python
import numpy as np

# Lista simple con valores enteros
simple_list = [1, 2, 3, 4, 5]

# Lista anidada con valores de punto flotante
nested_list = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

# Convertir la lista simple en un array de enteros
int_array = np.array(simple_list, dtype=int)

# Convertir la lista anidada en un array de punto flotante
float_array = np.array(nested_list, dtype=float)

# Imprimir los arrays resultantes
print(int_array)
print(float_array)


# Crear un array lineal de 36 elementos
linear_array = np.arange(36)

# Cambiar el shape para tener 3 filas y 12 columnas
reshaped_array_1 = linear_array.reshape(3, 12)

# Imprimir el array con 3 filas y 12 columnas
print("Array con 3 filas y 12 columnas:")
print(reshaped_array_1)

# Cambiar el shape nuevamente para tener 4 columnas
reshaped_array_2 = reshaped_array_1.reshape(-1, 4)

# Imprimir el array con 4 columnas
print("Array con 4 columnas:")
print(reshaped_array_2)
