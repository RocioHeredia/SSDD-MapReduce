# Dado un dataset (categoría, precio). Reducir para obtener promedio, máximo y 
# mínimo por categoría.
from functools import reduce

# 1. Dataset de ejemplo
dataset = [
    ("Electrónica", 1500.0),
    ("Ropa", 200.0),
    ("Electrónica", 800.0),
    ("Alimentos", 50.0),
    ("Ropa", 350.0),
    ("Electrónica", 1200.0),
    ("Alimentos", 80.0),
    ("Alimentos", 30.0),
    ("Ropa", 150.0)
]

# Paso REDUCE: Agrupar por categoría y acumular (suma, cantidad, max, min)
def reducer(acumulador, registro):
    categoria, precio = registro
    
    # Si es la primera vez que vemos esta categoría, la inicializamos
    if categoria not in acumulador:
        acumulador[categoria] = {
            'suma': precio, 
            'cantidad': 1, 
            'maximo': precio, 
            'minimo': precio
        }
    else:
        # Si ya existe, sumamos al acumulado e incrementamos el contador
        acumulador[categoria]['suma'] += precio
        acumulador[categoria]['cantidad'] += 1
        
        # Comparamos para actualizar máximo y mínimo si corresponde
        if precio > acumulador[categoria]['maximo']:
            acumulador[categoria]['maximo'] = precio
        if precio < acumulador[categoria]['minimo']:
            acumulador[categoria]['minimo'] = precio
            
    return acumulador

# Aplicar Reduce con un diccionario vacío como valor inicial
datos_agrupados = reduce(reducer, dataset, {})

# Paso Final: Calcular el promedio con los datos acumulados y mostrar
print("--- Resultados por Categoría ---")
for categoria, datos in datos_agrupados.items():
    # El promedio es la suma total dividida por la cantidad de elementos
    promedio = datos['suma'] / datos['cantidad']
    
    print(f"\nCategoría: {categoria}")
    print(f"  Promedio : ${promedio:.2f}")
    print(f"  Máximo   : ${datos['maximo']:.2f}")
    print(f"  Mínimo   : ${datos['minimo']:.2f}")