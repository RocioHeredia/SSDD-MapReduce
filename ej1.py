# Lista con al menos 20 números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Aplicar map para calcular el cuadrado de cada número
cuadrados = list(map(lambda x: x**2, numeros))

# Mostrar la lista resultante
print("Lista original:", numeros)
print("Cuadrados:", cuadrados)
