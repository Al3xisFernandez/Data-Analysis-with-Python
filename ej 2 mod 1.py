def contar_elementos(iterable):
    frecuencias = {}
    for elemento in iterable:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias
    
mi_iterable = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frecuencias = contar_elementos(mi_iterable)
print(frecuencias)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
