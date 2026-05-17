# Usando Reduce sumar los números de una lista de al menos 30 números 
from functools import reduce

# Lista con al menos 30 números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Usar Reduce para sumar los números
suma = reduce(lambda x, y: x + y, numeros)

# Mostrar el resultado
print("Lista de números:", numeros)
print("Suma:", suma)