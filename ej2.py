# Dada una lista de al menos 30 palabras de diferente longitud. Usar Map para 
# obtener una lista con sus longitudes 

# Lista con al menos 30 palabras de diferente longitud
palabras = ["manzana", "banana", "cereza", "durazno", "fresa", "uva", "naranja", "kiwi", "mango",
            "papaya", "piña", "sandía", "melón", "coco", "limón", "lima", "arándano", "frambuesa", "grosella", "higo",
            "guayaba", "maracuyá", "nectarina", "ciruela", "albaricoque", "avellana", "castaña", "nuez", "pistacho", "almendra"]

# Usar Map para obtener una lista con sus longitudes
longitudes = list(map(len, palabras))

# Mostrar la lista resultante
print("Lista original:", palabras)
print("Longitudes:", longitudes)