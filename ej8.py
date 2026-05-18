# Dado un dataset que tiene (estudiante, nota) con al menos 10 estudiantes, 
# Reducir calculando promedio.
from functools import reduce

# 1. Dataset inicial: Lista de tuplas (estudiante, nota)
dataset = [
    ("Ana", 8.5), 
    ("Carlos", 7.0), 
    ("Lucia", 9.0), 
    ("Martin", 6.5),
    ("Sofia", 10.0), 
    ("Pedro", 5.5), 
    ("Elena", 8.0), 
    ("Diego", 7.5),
    ("Valeria", 9.5), 
    ("Joaquin", 6.0), 
    ("Marta", 8.0)
]

# Paso MAP: Extraer solamente las notas de cada tupla (el índice 1)
notas = list(map(lambda x: x[1], dataset))

# Paso REDUCE: Sumar todas las notas extraídas
suma_notas = reduce(lambda x, y: x + y, notas)

# Calcular el promedio final
promedio = suma_notas / len(dataset)

# Mostrar los resultados de forma ordenada
print("--- Registro de Estudiantes ---")
for estudiante, nota in dataset:
    print(f"{estudiante:<10}: {nota}")

print("\n--- Resultados del Cálculo ---")
print(f"Cantidad de estudiantes : {len(dataset)}")
print(f"Suma total de notas     : {suma_notas}")
print(f"Promedio general        : {promedio:.2f}")
