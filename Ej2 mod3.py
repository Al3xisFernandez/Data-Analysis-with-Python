import numpy as np

# Definir los vectores de peso y altura
pesos = np.array([50, 65.5, 89.2, 100])
alturas = np.array([1.6, 1.7, 1.8, 1.75])

# Calcular el IMC para cada persona
imc = pesos / alturas ** 2

# Imprimir el vector de IMC
print("El vector de IMC es:")
print(imc)

