# Utilizando Map y Reduce. Dada una lista de palabras de diferente longitud, 
# obtener el promedio de longitud 
from functools import reduce

# Lista con al menos 30 palabras de diferente longitud
palabras = ["manzana", "banana", "cereza", "durazno", "fresa", "uva", "naranja", "kiwi", "mango",
            "papaya", "piña", "sandía", "melón", "coco", "limón", "lima", "arándano", "frambuesa", "grosella", "higo",
            "guayaba", "maracuyá", "nectarina", "ciruela", "albaricoque", "avellana", "castaña", "nuez", "pistacho", "almendra"]

# Usar Map para obtener la longitud de cada palabra
longitudes = list(map(len, palabras))

# Usar Reduce para sumar las longitudes
suma_longitudes = reduce(lambda x, y: x + y, longitudes)

# Calcular el promedio
promedio = suma_longitudes / len(palabras)

# Mostrar el resultado
print("Lista de palabras:", palabras)
print("Longitudes:", longitudes)
print("Suma de longitudes:", suma_longitudes)
print("Promedio de longitud:", promedio)