# Usando Map y Reduce. Resolver el problema de contar palabras
from functools import reduce

texto= "Hola mundo, este es un ejemplo de contar palabras usando Map y Reduce en Python. Map y Reduce son funciones de orden superior que se utilizan para procesar colecciones de datos. Map aplica una función a cada elemento de una colección, mientras que Reduce aplica una función acumulativa a los elementos de una colección para reducirla a un solo valor."

# Limpiar el texto de signos de puntuación y convertirlo a minúsculas
texto_limpio = texto.lower().replace(",", "").replace(".", "").replace("¿", "").replace("?", "") 

# Dividir el texto en palabras y guardar en una lista
palabras = texto_limpio.split()

# Usar Map para contar cada palabra
pares= list(map(lambda x: (x, 1), palabras))

# Usar Reduce para sumar los conteos de cada palabra
def reducer (acumulador, elemento):
    palabra, conteo = elemento
    acumulador[palabra] = acumulador.get(palabra, 0) + conteo
    return acumulador

conteo_palabras = reduce(reducer, pares, {})

# Imprimir el resultado
print("Texto original: ", texto)
print(" \n Lista de palabras: ", palabras)
print(" \n Conteo de palabras: ")

for palabra, conteo in sorted(conteo_palabras.items()):
    print(f"{palabra}: {conteo}")
