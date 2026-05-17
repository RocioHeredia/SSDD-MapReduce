# Dada una lista de palabras en minúscula pasar  la primera letra en mayúscula 
# con Map. 
# Lista con al menos 30 palabras de diferente longitud
palabras = ["manzana", "banana", "cereza", "durazno", "fresa", "uva", "naranja", "kiwi", "mango",
            "papaya", "piña", "sandía", "melón", "coco", "limón", "lima", "arándano", "frambuesa", "grosella", "higo",
            "guayaba", "maracuyá", "nectarina", "ciruela", "albaricoque", "avellana", "castaña", "nuez", "pistacho", "almendra"]

# Usar Map para pasar la primera letra en mayúscula
palabras_mayuscula = list(map(lambda x: x.capitalize(), palabras))

# Mostrar la lista resultante
print("Lista original:", palabras)
print("Lista con primera letra en mayúscula:", palabras_mayuscula)