# Usando Reduce Multiplicar una lista de al menos 10 números enteros, por un número entero
from functools import reduce

# Lista con al menos 10 números enteros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Número entero por el cual multiplicar
multiplicador = 2

resultado = reduce(lambda acc, x: acc + [x * multiplicador], numeros, [])

# Mostrar resultados
print("Lista original:", numeros)
print(f"Multiplicados por {multiplicador}:", resultado)