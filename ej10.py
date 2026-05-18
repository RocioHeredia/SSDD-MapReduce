# Dado un Dataset con los datos (IP, recurso, tiempo) reducir contando los 
# accesos por IP. Detectar cual es la IP más activa
from functools import reduce

dataset = [
    ("192.168.1.1", "/index.html", "2023-01-01 10:00:00"),
    ("192.168.1.2", "/about.html", "2023-01-01 10:05:00"),
    ("192.168.1.1", "/contact.html", "2023-01-01 10:10:00"),
    ("192.168.1.3", "/index.html", "2023-01-01 10:15:00"),
    ("192.168.1.2", "/services.html", "2023-01-01 10:20:00"),
    ("192.168.1.1", "/products.html", "2023-01-01 10:25:00")
]
# 1️⃣ Usamos map para extraer solo las IPs
ips = list(map(lambda x: x[0], dataset))

# 2️⃣ Usamos reduce para acumular los conteos en un diccionario
conteo_ips = reduce(
    lambda acc, ip: {**acc, ip: acc.get(ip, 0) + 1},
    ips,
    {}
)
# 3️⃣ Detectar la IP más activa
ip_mas_activa = max(conteo_ips, key=conteo_ips.get)

print("Conteo de accesos por IP:", conteo_ips)
print("IP más activa:", ip_mas_activa, "con", conteo_ips[ip_mas_activa], "accesos")
