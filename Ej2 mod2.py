def suma_acotados(*args, cota=None):
    if cota is None:
        return sum(args)
    else:
        return sum(arg for arg in args if -cota <= arg <= cota)

# Sumar todos los argumentos
resultado1 = suma_acotados(1, 2, 3, 4, 5)
print(resultado1)  # Output: 15

# Sumar sólo los argumentos dentro de la cota
resultado2 = suma_acotados(-2, -1, 0, 1, 2, 3, 4, cota=2)
print(resultado2)  # Output: 3
