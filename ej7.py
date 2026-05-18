# Usando Map y Reduce. Resolver el problema de contar palabras



from collections import defaultdict

# Función map

def map_function(text):
    resultado = []

    # Separar palabras y pasarlas a minúsculas
    words = text.lower().split()

    # (palabra, 1)
    for word in words:
        resultado.append((word, 1))

    #Ordenar por palabra
    resultado.sort(key=lambda x: x[0])
    
    return resultado

# Función reduce

def reduce_function(mapped_data):
    grouped = defaultdict(list)

    # Agrupar valores por clave
    for word, count in mapped_data:
        grouped[word].append(count)

    reduced = {}

    # Sumar los valores de cada palabra
    for word, counts in grouped.items():
        reduced[word] = sum(counts)

    return reduced

# Ejemplo de uso
Texto = "hola mundo hola python hola map reduce desde python"

mapped_results = map_function(Texto)

print("\n ")
print("Resultado al aplicar Map:")
print(mapped_results)

final_result = reduce_function(mapped_results)

print("\nResultado al aplicar Reduce:")
for word, total in final_result.items():
    print(word, "->", total)
print("\n ")